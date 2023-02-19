# Generated by Django 4.1.6 on 2023-02-19 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [("core", "0008_skillcategory_skill_percentage_alter_skill_category")]

    operations = [
        migrations.CreateModel(
            name="Certificate",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=100)),
                ("issuer", models.CharField(max_length=100)),
                ("issue_date", models.DateField()),
                ("expiration_date", models.DateField(blank=True, null=True)),
                ("credential_id", models.CharField(blank=True, max_length=100, null=True)),
                ("credential_url", models.URLField(blank=True, null=True)),
                ("credential_image", models.ImageField(blank=True, null=True, upload_to="images")),
                (
                    "contact",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="certificates", to="core.contact"
                    ),
                ),
            ],
        )
    ]
