# Generated by Django 4.1.6 on 2023-02-26 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [("github", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="GitHubUser",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("username", models.CharField(max_length=50)),
                ("access_token", models.CharField(max_length=200)),
                ("excluded_repos", models.CharField(blank=True, max_length=200, null=True)),
                ("excluded_langs", models.CharField(blank=True, max_length=200, null=True)),
                ("exclude_forked_repos", models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name="stats",
            name="user",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to="github.githubuser"
            ),
        ),
    ]
