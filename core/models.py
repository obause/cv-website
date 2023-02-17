import datetime
from django.db import models

GENDER_TYPES = (
    ("F", "Female"),
    ("M", "Male"),
)


# Create your models here.
class Contact(models.Model):
    forename = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    gender = models.CharField(choices=GENDER_TYPES, max_length=10)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    birthdate = models.DateField()
    address = models.TextField(max_length=1000)
    nationality = models.CharField(max_length=100)
    social_media = models.ManyToManyField("SocialMedia", blank=True)
    website = models.CharField(max_length=100, blank=True)
    profile_image = models.ImageField(upload_to="images", blank=True)
    description = models.TextField(max_length=2000, blank=True)
    slogan = models.CharField(max_length=100, blank=True)

    def full_name(self):
        return f"{self.forename} {self.lastname}"

    def age(self):
        return int((datetime.date.today() - self.birthdate).days / 365.25)

    def __str__(self):
        return self.full_name()


class Education(models.Model):
    title = models.CharField(max_length=100)
    institute = models.CharField(max_length=100)
    institute_url = models.URLField()
    course_of_study = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
    final_grade = models.CharField(max_length=10)
    start_date = models.DateField()
    end_date = models.DateField()
    major_field = models.CharField(max_length=100)
    description = models.TextField(max_length=2000, blank=True)
    contact = models.ForeignKey(
        Contact, on_delete=models.CASCADE, related_name="education"
    )

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

    def __str__(self):
        return self.name


class FunFact(models.Model):
    title = models.CharField(max_length=100)
    value = models.IntegerField()
    icon = models.CharField(max_length=100)