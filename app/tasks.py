from background_task import background
from background_task.models import Task
# from projects.models import News
# import requests, datetime
from logging import getLogger


# Asynchronous tasks
@background(schedule=Task.HOURLY)
def demo_task(message):
    print('demo_task. message={0}'.format(message))
