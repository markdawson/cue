from django.shortcuts import render
import os
import requests


def home_view(request):


    data = request.GET

    name = data.get('username', '')

    token = os.environ.get('PAGE_ACCESS_TOKEN')

    context = {
        'user_name': name[::-1],
        'token': token
    }

    to_send = data.get('send')
    if to_send:
        context['sent'] = to_send

        text = to_send
        sender = 1518048118282187

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

        r = requests.post(url, json=payload)
        context['response'] = r.content

    return render(request, "dashboard/index.html", context)


def user_view(request, name):

    print(name)

    context = {
        'user_name': name
    }

    return render(request, "dashboard/index.html", context)
