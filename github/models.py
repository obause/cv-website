from django.db import models
from .github import Stats
from asgiref.sync import sync_to_async

import aiohttp
import asyncio


def default_stats():
    stats = UserStats()
    stats.save()
    return stats.pk


class GitHubUser(models.Model):
    username = models.CharField(max_length=50)
    access_token = models.CharField(max_length=200)
    excluded_repos = models.CharField(max_length=200, blank=True, null=True)
    excluded_langs = models.CharField(max_length=200, blank=True, null=True)
    exclude_forked_repos = models.BooleanField(default=False)
    stats = models.OneToOneField('UserStats', on_delete=models.CASCADE, default=default_stats)

    def __str__(self):
        return self.username

    async def update_userstats(self):
        print("update_userstats")
        access_token = self.access_token
        user = self.username
        if access_token is None or user is None:
            raise RuntimeError(
                "ACCESS_TOKEN and GITHUB_USER environment variables cannot be None!"
            )
        exclude_repos = self.excluded_repos
        excluded_repos = (
            {x.strip() for x in exclude_repos.split(",")} if exclude_repos else None
        )
        exclude_langs = self.excluded_langs
        excluded_langs = (
            {x.strip() for x in exclude_langs.split(",")} if exclude_langs else None
        )
        # Convert a truthy value to a Boolean
        raw_ignore_forked_repos = self.exclude_forked_repos
        ignore_forked_repos = (
            not not raw_ignore_forked_repos
            and raw_ignore_forked_repos.strip().lower() != "false"
        )
        print(f"ignore_forked_repos: {ignore_forked_repos}")

        async with aiohttp.ClientSession() as session:
            s = Stats(
                user,
                access_token,
                session,
                exclude_repos=excluded_repos,
                exclude_langs=excluded_langs,
                ignore_forked_repos=ignore_forked_repos,
            )
            print("Updating stats...")
            await self.stats.update_stats(s)


class UserStats(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    stars = models.IntegerField(blank=True, null=True)
    forks = models.IntegerField(blank=True, null=True)
    contributions = models.IntegerField(blank=True, null=True)
    repositories = models.IntegerField(blank=True, null=True)
    loc_added = models.IntegerField(blank=True, null=True)
    loc_deleted = models.IntegerField(blank=True, null=True)
    # loc_changed = models.IntegerField(blank=True, null=True)
    page_views = models.IntegerField(blank=True, null=True)

    # def __str__(self):
    #     return self.name

    async def update_stats(self, s):
        self.name = await s.name
        self.stars = await s.stargazers
        self.forks = await s.forks
        self.contributions = await s.total_contributions
        self.repositories = len(await s.repos)
        # self.loc_added = await s.lines_changed[0]
        # self.loc_deleted = await s.lines_changed[1]
        self.page_views = await s.views
        print("Saving stats...")
        await sync_to_async(self.save())


class Language(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    occurences = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=100, blank=True, null=True)
    prop = models.FloatField(blank=True, null=True)
    stat = models.ForeignKey(UserStats, on_delete=models.CASCADE, blank=True, null=True, related_name="language")

    def __str__(self):
        return self.name

    def update_lang(self, s):
        pass
