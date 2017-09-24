from django.shortcuts import render
import os


def home_view(request):


    data = request.GET

    name = data.get('username', '')

    token = os.environ.get('PAGE_ACCESS_TOKEN')

    context = {
        'user_name': name[::-1],
        'token': token
    }

    return render(request, "dashboard/index.html", context)


def user_view(request, name):

    print(name)

    context = {
        'user_name': name
    }

    return render(request, "dashboard/index.html", context)
