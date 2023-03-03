# Generated by Django 4.1.6 on 2023-03-03 19:56

from django.db import migrations, models
import django.db.models.deletion
import github.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0013_socialmedia_add_to_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('stars', models.IntegerField(blank=True, null=True)),
                ('forks', models.IntegerField(blank=True, null=True)),
                ('contributions', models.IntegerField(blank=True, null=True)),
                ('repositories', models.IntegerField(blank=True, null=True)),
                ('loc_added', models.IntegerField(blank=True, null=True)),
                ('loc_deleted', models.IntegerField(blank=True, null=True)),
                ('page_views', models.IntegerField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('size', models.IntegerField(blank=True, null=True)),
                ('occurences', models.IntegerField(blank=True, null=True)),
                ('color', models.CharField(blank=True, max_length=100, null=True)),
                ('prop', models.FloatField(blank=True, null=True)),
                ('stat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='language', to='github.userstats')),
            ],
        ),
        migrations.CreateModel(
            name='GitHubUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('access_token', models.CharField(max_length=200)),
                ('excluded_repos', models.CharField(blank=True, max_length=200, null=True)),
                ('excluded_langs', models.CharField(blank=True, max_length=200, null=True)),
                ('exclude_forked_repos', models.BooleanField(default=False)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='github_user', to='core.contact')),
                ('stats', models.OneToOneField(default=github.models.default_stats, on_delete=django.db.models.deletion.CASCADE, to='github.userstats')),
            ],
        ),
    ]
