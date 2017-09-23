from django.http import JsonResponse, HttpResponse


def messages_response(request):

    data = request.GET


    return JsonResponse({'status': 'success'})


def messages_response_verify(request):

    data = request.GET

    token = data.get('hub.verify_token')

    if token == 'cueparty':
        challenge = data.get('hub.challenge')
    else:
        challenge = 'Failure'

    return HttpResponse(challenge)
