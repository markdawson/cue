from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User

import logging
import json
import requests
import os
from time import sleep
import random

logger = logging.getLogger('cue.custom')


@csrf_exempt
def messages_response(request):

    if request.method == 'POST':
        data = json.loads(request.body)
        logger.info(data)

        sender = data['entry'][0]['messaging'][0]['sender']['id']
        text = data['entry'][0]['messaging'][0]['message'].get('text')

        if text:
            logger.info(post_message_to_fb(sender, text))
            if random.random() < 0.30:
                sleep(1)
                requests.post(sender, 'teehee')

        return JsonResponse({'thanks': True})

    else: # This logic is for verifying the inital api
        data = request.GET
        token = data.get('hub.verify_token')

        if token == 'cueparty':
            challenge = data.get('hub.challenge')
            return HttpResponse(challenge)

    return JsonResponse({'status': 'success'})


def post_message_to_fb(to, text):

    token = os.environ.get('PAGE_ACCESS_TOKEN')
    url = "https://graph.facebook.com/v2.6/me/messages?access_token={}".format(token)

    payload = {
        "recipient": {
            "id": to
        },
        "message": {
            "text": text
        }
    }

    r = requests.post(url, json=payload)
    return r


def get_user_info_from_fb(id):

    token = os.environ.get('PAGE_ACCESS_TOKEN')
    url = "https://graph.facebook.com/v2.6/{}?fields=first_name,last_name,profile_pic&access_token={}".format(id, token)
    r = requests.get(url)

    return json.loads(r.content.decode("utf-8"))


def save_user_info_to_db(json_obj):
    pass

