from background_task import background
# from projects.models import News
# import requests, datetime
from logging import getLogger


# Asynchronous tasks
@background(schedule=5)
def demo_task(message):
    print('demo_task. message={0}'.format(message))
