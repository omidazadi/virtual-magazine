from django.http import HttpResponse


def index(request):
    print("Hi, I'm here!")
    return HttpResponse("Hello, world. You're at the polls index.")
