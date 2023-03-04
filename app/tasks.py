from background_task import background
from background_task.models import Task
from django.conf import settings

from core.models import Contact
from github.models import GitHubUser
# import requests, datetime
from logging import getLogger


# Asynchronous tasks
@background(schedule=Task.HOURLY)
def github_task(message):
    print('task. message={0}'.format(message))
    contact = Contact.objects.get(pk=settings.CONTACT_PK)
    gh_user = contact.github_user.get()
    gh_user.update_userstats()
