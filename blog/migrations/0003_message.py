# Generated by Django 4.1.6 on 2023-02-24 10:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("blog", "0002_category_post_category")]

    operations = [
        migrations.CreateModel(
            name="Message",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("subject", models.CharField(max_length=100)),
                ("message", models.CharField(max_length=500)),
            ],
        )
    ]
