# Generated by Django 4.1.6 on 2023-02-18 14:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("core", "0003_interests")]

    operations = [
        migrations.AddField(model_name="education", name="is_current", field=models.BooleanField(default=False))
    ]
