from django.shortcuts import HttpResponse


def hello(request):
    # print(dir(request))
    return HttpResponse("hello world")
