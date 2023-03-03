# Generated by Django 4.1.6 on 2023-03-03 20:10

from django.db import migrations


class Migration(migrations.Migration):

    def create_contact(apps, schema_editor):
        contact = apps.get_model('core', 'Contact')
        contact.objects.create(forename='Default', lastname='Contact')

    dependencies = [("core", "0014_alter_contact_address_alter_contact_birthdate_and_more")]

    operations = [
        migrations.RunPython(create_contact)
    ]
