from django.contrib import admin
from .models import GitHubUser, UserStats, Language


# Register your models here.
class UserStatsAdmin(admin.ModelAdmin):
    list_display = ("name", "stars", "forks", "repositories")


class LanguageAdmin(admin.ModelAdmin):
    list_display = ("name", "size", "occurences", "prop", "color")


admin.site.register(GitHubUser)
admin.site.register(UserStats, UserStatsAdmin)
admin.site.register(Language, LanguageAdmin)
