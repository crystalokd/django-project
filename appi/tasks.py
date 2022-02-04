from __future__ import absolute_import, unicode_literals

import requests

from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

import io
from rest_framework.parsers import JSONParser
logger = get_task_logger(__name__)



@periodic_task(
    run_every=(crontab(minute='*/15')),
    name="task_save_latest_flickr_image",
    ignore_result=True
)
def save_response():

	url = "https://hacker-news.firebaseio.com/v0/showstories.json?print=pretty"

	payload = "{}"
	response = requests.request("GET", url, data=payload)
	
	stream = io.BytesIO(json)
    data = JSONParser().parse(stream)


	serializer = NewsSerializer(comment)
	serializer = NewsSerializer(comment, data=data)
	serializer.is_valid()
	news = response.save()
	