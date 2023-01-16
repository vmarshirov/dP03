from django.http import HttpResponse


def index(request):
    return HttpResponse("Привет")

def abc(request):
    return HttpResponse('abc')