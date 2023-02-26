from django.contrib import admin
from .models import GitHubUser, UserStats, Language

# Register your models here.
admin.site.register(GitHubUser)
admin.site.register(UserStats)
admin.site.register(Language)
