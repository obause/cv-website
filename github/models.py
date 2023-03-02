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
    contact = models.ForeignKey('core.Contact', on_delete=models.CASCADE, related_name='github_user')

    def __str__(self):
        return self.username

    def update_userstats(self):
        data = asyncio.run(self.fetch_userstats())
        print(f"data: {data}")
        self.stats.update_stats(data)
        for language, values in data['languages'].items():
            print(f"language: {language}, values: {values}")
            self.stats.language.update_or_create(
                name=language, defaults={
                    'size': values['size'],
                    'occurences': values['occurrences'],
                    'color': values['color'],
                    'prop': values['prop']
                }
            )

    async def fetch_userstats(self):
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
            data = {
                "name": await s.name,
                "stars": await s.stargazers,
                "forks": await s.forks,
                "contributions": await s.total_contributions,
                "repositories": await s.repos,
                "languages": await s.languages,
                "languages_proportional": await s.languages_proportional,
                "total_contributions": await s.total_contributions,
                # "lines_changed": await s.lines_changed,
                "views": await s.views,
            }
            return data


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
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.name is None:
            return "No name"
        return self.name

    def update_stats(self, s):
        self.name = s['name'] if s['name'] is not None else self.name
        self.stars = s.get("stars") if s.get("stars") is not None else self.stars
        self.forks = s.get("forks") if s.get("forks") is not None else self.forks
        self.contributions = s.get("contributions") if s.get("contributions") is not None else self.contributions
        self.repositories = len(s.get("repositories")) if s.get("repositories") is not None else self.repositories
        self.loc_added = s.get("lines_changed")[0] if s.get("lines_changed") is not None else self.loc_added
        self.loc_deleted = s.get("lines_changed")[1] if s.get("lines_changed") is not None else self.loc_deleted
        self.page_views = s.get("views") if s.get("views") is not None else self.page_views
        print("Saving stats...")
        self.save()

    def get_loc_changed(self):
        return self.loc_added + self.loc_deleted


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
