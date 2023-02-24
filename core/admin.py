from django.contrib import admin
from .models import Contact, Education, SocialMedia, FunFact, Interests, WorkExperience, Skill, SkillCategory, Certificate, Message


class ContactAdmin(admin.ModelAdmin):
    list_display = ("forename", "lastname")


class EducationAdmin(admin.ModelAdmin):
    list_display = ("title", "start_date", "end_date")


class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ("title", "start_date", "end_date")


class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "percentage")


admin.site.register(Contact, ContactAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(SocialMedia)
admin.site.register(FunFact)
admin.site.register(Interests)
admin.site.register(WorkExperience, WorkExperienceAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(SkillCategory)
admin.site.register(Certificate)
admin.site.register(Message)
