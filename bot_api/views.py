from django.http import JsonResponse


def messages_response(request):
    return JsonResponse({'status': 'success'})