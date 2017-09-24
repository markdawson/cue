from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

import logging
import json
import requests
import os
from time import sleep

logger = logging.getLogger('cue.custom')


@csrf_exempt
def messages_response(request):

    if request.method == 'POST':
        data = json.loads(request.body)
        logger.info(data)



        sender = data['entry'][0]['messaging'][0]['sender']['id']
        text = data['entry'][0]['messaging'][0]['message']['text']

        # payload = {
        #     "recipient": {
        #         "id": sender
        #     },
        #     "message": {
        #         "text": text
        #     }
        # }
        #
        # token = os.environ.get('PAGE_ACCESS_TOKEN')
        # url = "https://graph.facebook.com/v2.6/me/messages?access_token={}".format(token)
        #
        # r = requests.post(url, json=payload)
        # logger.info(token)
        # logger.info(url)
        # logger.info(r.content)

        token = 'EAAEZBsQCC0fwBACo4UPYZCVd74pQcm2VkorSaDoQJ143SxMUPM8zx6D102UijrhGYTCpZAYRvZBhKdNCen4SO8unytSlAkjM3GygIPwtO1ZBokEcPMsK2ZCubLi0drQbZBDuqyvgfvol5MriB66bPxHaI1dzK7AjqZAkmc5nkZBbrVQZDZD'
        url = "https://graph.facebook.com/v2.6/me/messages?access_token={}".format(token)

        payload = {
            "recipient": {
                "id": sender
            },
            "message": {
                "text": text
            }
        }

        payload2 = {
            "recipient": {
                "id": sender
            },
            "message": {
                "text": 'tehe'
            }
        }



        r = requests.post(url, json=payload)
        sleep(1)
        requests.post(url, json=payload2)
        logger.info(text)
        logger.info(sender)
        logger.info(token)
        logger.info(url)
        logger.info(r.content)


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







