from django.http import JsonResponse, HttpResponse
import logging

logger = logging.getLogger('cue.custom')



def messages_response(request):

    if request.method == 'POST':
        logger.info(request.POST)
        return JsonResponse({'thanks': True})

    data = request.GET
    token = data.get('hub.verify_token')

    if token == 'cueparty':
        challenge = data.get('hub.challenge')
        return HttpResponse(challenge)

    logger.info(data)


    return JsonResponse({'status': 'success'})


def messages_response_verify(request):
    pass







