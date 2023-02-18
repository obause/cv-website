from django.contrib import admin
from .models import Contact, Education, SocialMedia, FunFact, Interests, WorkExperience


class ContactAdmin(admin.ModelAdmin):
    list_display = ("forename", "lastname")


admin.site.register(Contact)
admin.site.register(Education)
admin.site.register(SocialMedia)
admin.site.register(FunFact)
admin.site.register(Interests)
admin.site.register(WorkExperience)
