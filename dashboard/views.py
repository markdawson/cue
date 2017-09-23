from django.shortcuts import render


def home_view(request):


    data = request.GET

    name = data.get('username', '')

    context = {
        'user_name': name[::-1]
    }

    return render(request, "dashboard/index.html", context)


def user_view(request, name):

    print(name)

    context = {
        'user_name': name
    }

    return render(request, "dashboard/index.html", context)
