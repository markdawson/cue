from django.shortcuts import render


def home_view(request):

    data = request.GET

    name = data['username']


    content = {
        'username': name
    }
    return render(request, "dashboard/index.html", content)