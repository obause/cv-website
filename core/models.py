import datetime
from django.db import models

GENDER_TYPES = (("F", "Female"), ("M", "Male"))

SKILL_CATEGORY = (
    ("Technical", "Technical"),
    ("Soft", "Soft"),
    ("Other", "Other"),
    ("Languages", "Languages"),
    ("Tools", "Tools"),
    ("Frameworks", "Frameworks"),
)


# Create your models here.
class Contact(models.Model):
    forename = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(choices=GENDER_TYPES, max_length=10, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    address = models.TextField(max_length=1000, blank=True, null=True)
    nationality = models.CharField(max_length=100, blank=True, null=True)
    social_media = models.ManyToManyField("SocialMedia")
    website = models.CharField(max_length=100, blank=True, null=True)
    profile_image = models.ImageField(upload_to="images/profile_pics", blank=True, null=True)
    description = models.TextField(max_length=2000, blank=True, null=True)
    slogan = models.CharField(max_length=100, blank=True, null=True)
    skills = models.ManyToManyField("Skill")

    def full_name(self):
        return f"{self.forename} {self.lastname}"

    def age(self):
        return int((datetime.date.today() - self.birthdate).days / 365.25)

    def __str__(self):
        return self.full_name()


class Education(models.Model):
    title = models.CharField(max_length=100)
    institute = models.CharField(max_length=100)
    institute_url = models.URLField(blank=True, null=True)
    institute_logo = models.ImageField(upload_to="images/logos", blank=True, null=True)
    course_of_study = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
    final_grade = models.CharField(max_length=10, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    major_field = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=2000, blank=True, null=True)
    is_current = models.BooleanField(default=False)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name="education")

    def start_year(self):
        return self.start_date.year

    def end_year(self):
        return self.end_date.year

    def __str__(self):
        return self.title


class SocialMedia(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    add_to_menu = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class FunFact(models.Model):
    title = models.CharField(max_length=100)
    value = models.IntegerField()
    icon = models.CharField(max_length=100)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name="fun_facts", blank=True, null=True)


class Interests(models.Model):
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    description = models.TextField(max_length=2000, blank=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name="interests")
    image = models.ImageField(upload_to="images/icons", blank=True, null=True)

    def __str__(self):
        return self.title


class WorkExperience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    company_url = models.URLField(blank=True, null=True)
    company_logo = models.ImageField(upload_to="images/logos", blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(max_length=2000, blank=True, null=True)
    is_current = models.BooleanField(default=False)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name="experience")

    def start_year(self):
        return self.start_date.year

    def end_year(self):
        return self.end_date.year

    def __str__(self):
        return self.title


class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        "SkillCategory",
        on_delete=models.CASCADE,
        related_name="skills",
        blank=True,
        null=True
    )
    percentage = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    is_percentage = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Certificate(models.Model):
    title = models.CharField(max_length=100)
    issuer = models.CharField(max_length=100)
    issue_date = models.DateField()
    expiration_date = models.DateField(blank=True, null=True)
    credential_id = models.CharField(max_length=100, blank=True, null=True)
    credential_url = models.URLField(blank=True, null=True)
    credential_image = models.ImageField(upload_to="images/certificates", blank=True, null=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name="certificates")

    def __str__(self):
        return self.title


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=500)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
