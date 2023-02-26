from django.shortcuts import render
from django.conf import settings

from .github import Stats, Queries
from .models import GitHubUser, UserStats, Language

import aiohttp
import asyncio


# Create your views here.
async def get_stats(github_user):
    access_token = github_user.access_token
    user = github_user.username
    if access_token is None or user is None:
        raise RuntimeError(
            "ACCESS_TOKEN and GITHUB_USER environment variables cannot be None!"
        )
    exclude_repos = github_user.excluded_repos
    excluded_repos = (
        {x.strip() for x in exclude_repos.split(",")} if exclude_repos else None
    )
    exclude_langs = github_user.excluded_langs
    excluded_langs = (
        {x.strip() for x in exclude_langs.split(",")} if exclude_langs else None
    )
    # Convert a truthy value to a Boolean
    raw_ignore_forked_repos = github_user.exclude_forked_repos
    ignore_forked_repos = (
        not not raw_ignore_forked_repos
        and raw_ignore_forked_repos.strip().lower() != "false"
    )

    data = {}
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
            # "languages_proportional": await s.languages_proportional,
            # "total_contributions": await s.total_contributions,
            # "lines_changed": await s.lines_changed,
            "views": await s.views,
        }
    print(f"data: {data}")
    return data


def github_test(request):
    github_user = GitHubUser.objects.first()
    # stats = asyncio.run(get_stats(github_user))
    # context = {"stats": stats}
    print(f"github_user: {github_user}")

    stats = github_user.stats
    print(f"stats: {stats.name}")

    asyncio.run(github_user.update_userstats())
    context = {"done": True}
    return render(request, "github/github.html", context)
