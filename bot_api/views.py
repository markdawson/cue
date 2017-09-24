from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

import logging
import json

logger = logging.getLogger('cue.custom')


@csrf_exempt
def messages_response(request):

    if request.method == 'POST':
        data = json.loads(request.body)
        logger.info(data)
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







