from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

import logging
import json
import requests
import os

logger = logging.getLogger('cue.custom')


@csrf_exempt
def messages_response(request):

    if request.method == 'POST':
        data = json.loads(request.body)
        logger.info(data)

        token = os.environ.get('PAGE_ACCESS_TOKEN')

        sender = data['messaging'][0]['sender']['id']
        text = data.get('text')

        payload = {
            "recipient": {
                "id": sender
            },
            "message": {
                "text": text
            }
        }

        url = "https://graph.facebook.com/v2.6/me/messages?access_token={}".format(token)

        requests.post(url, data=payload)
        return JsonResponse({'thanks': True})

    else:
        data = request.GET
        token = data.get('hub.verify_token')

        if token == 'cueparty':
            challenge = data.get('hub.challenge')
            return HttpResponse(challenge)

        #logger.info(data)


    return JsonResponse({'status': 'success'})


def messages_response_verify(request):
    pass







