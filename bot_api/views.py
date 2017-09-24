from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import CueUser

import logging
import json
import requests
import os
from time import sleep
import random
import urllib
import re

logger = logging.getLogger('cue.custom')

GOOGLE_API_KEY = "AIzaSyAT5yDn3sJ5Fqvm5MTijloIqYm1QeEIREA"



@csrf_exempt
def messages_response(request):

    if request.method == 'POST':
        data = json.loads(request.body)
        logger.info(data)

        sender_id = data['entry'][0]['messaging'][0]['sender']['id']
        text = data['entry'][0]['messaging'][0]['message'].get('text')
        attachments = data['entry'][0]['messaging'][0]['message'].get('attachments')

        try:
            sender = CueUser.objects.get(user_id=sender_id)

        except CueUser.DoesNotExist:
            json_obj = get_user_info_from_fb(sender_id)
            save_user_info_to_db(json_obj)


        if text=='hey':
            post_message_to_fb(sender_id, 'teehee')
            sleep(1)
            post_share_location_prompt_to_fb(sender_id)
            return JsonResponse({'thanks': True})

        if attachments:
            coords = attachments[0]['payload'].get('coordinates')
            if coords:
                lat = coords['lat']
                long = coords['long']
                u = CueUser.objects.get(user_id=sender_id)
                u.home_lat = lat
                u.home_long = long
                u.save()
                post_message_to_fb(sender_id, "Thank ya! I can help you find events near you now.")
            return JsonResponse({'thanks': True})


        ## * START TEXT INTERPOLATION * ##
        pattern = "cue\s(.+)\sat\s(.+)\sat\s(.+)$"
        m = re.match(pattern, text)
        title, time, place = m.groups()

        response = "I'll schedule an event called {} at at {}".format()
        post_message_to_fb(sender_id, response)
        quick_replies = [
            {
                "content_type":"text",
                "title": "Yes",
                "payload": True,
            },
            {
                "content_type": "text",
                "title": "No",
                "payload": False,
            },

        ]
        post_message_to_fb(sender_id, "Does that sound okay?", quick_replies)



        if text:
            logger.info(post_message_to_fb(sender_id, text))
            dice_roll = random.random()
            logger.info("teehee dice roll: {}".format(dice_roll))
            if dice_roll < 0.30:
                post_message_to_fb(sender_id, 'teehee')

        return JsonResponse({'thanks': True})


    ####################################################################################

    else: # This logic is for verifying the inital api
        data = request.GET
        token = data.get('hub.verify_token')

        if token == 'cueparty':
            challenge = data.get('hub.challenge')
            return HttpResponse(challenge)

    return JsonResponse({'status': 'success'})


def post_share_location_prompt_to_fb(to):

    token = os.environ.get('PAGE_ACCESS_TOKEN')
    url = "https://graph.facebook.com/v2.6/me/messages?access_token={}".format(token)

    payload = {
        "recipient": {
            "id": to
        },
        "message": {
            "text": "To help you with event planning, could you tell me where you are?",
            "quick_replies": [
                {
                    "content_type": "location"
                }
            ]
        },


    }

    r = requests.post(url, json=payload)
    return r


def post_message_to_fb(to, text, quick_replies=None):


    sleep(0.5)
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

    if quick_replies:
        payload['message']['quick_replies'] = quick_replies

    r = requests.post(url, json=payload)
    return r


def get_user_info_from_fb(id):

    token = os.environ.get('PAGE_ACCESS_TOKEN')
    url = "https://graph.facebook.com/v2.6/{}?fields=first_name,last_name,timezone&access_token={}".format(id, token)
    r = requests.get(url)

    return json.loads(r.content.decode("utf-8"))


def save_user_info_to_db(json_obj):

    CueUser.objects.create(
        user_id=json_obj['id'],
        iso_timezone=json_obj['timezone'],
        first_name=json_obj['first_name'],
        last_name=json_obj['last_name']
    )

    return True


def getNearbyLocations(keyword, latitude, longitude):
    """
    Given a latitude and longitude, queries the Google Places API to find the 5 locations nearest those coordinates
    matching the given keyword.
    """

    query = ("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + str(latitude) + "," + str(longitude)
            + "&keyword=" + str(keyword) + "&rankby=distance" + "&key=" + str(GOOGLE_API_KEY))

    response = urllib.urlopen(query)
    jsonRaw = response.read()
    jsonData = json.loads(jsonRaw)

    return [item for item in jsonData["results"] if jsonData["results"].index(item) < 5]



