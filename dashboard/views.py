from django.shortcuts import render


def home_view(request):

    data = request.GET

    name = data['username']


    context = {
        'user_name': name[::-2]

    }

    return render(request, "dashboard/index.html", context)