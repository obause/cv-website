# Generated by Django 4.1.6 on 2023-02-18 22:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("core", "0006_workexperience")]

    operations = [
        migrations.CreateModel(
            name="Skill",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                (
                    "category",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Technical", "Technical"),
                            ("Soft", "Soft"),
                            ("Other", "Other"),
                            ("Languages", "Languages"),
                            ("Tools", "Tools"),
                            ("Frameworks", "Frameworks"),
                        ],
                        max_length=100,
                        null=True,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="contact", name="skills", field=models.ManyToManyField(blank=True, to="core.skill")
        ),
    ]
