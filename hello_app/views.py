import datetime

from django.core.mail.message import sanitize_address
from django.shortcuts import HttpResponse
from django.utils.html import escape
from django.shortcuts import render


def hello(request):
    # print(dir(request))
    return HttpResponse("hello world")


def hello_name(request, name):
    sanitize_name = escape(name)
    return HttpResponse(f"Hello, {sanitize_name}")


def hello_template(request, name):
    # return HttpResponse("hello world")
    return render(request, template_name="hello_app/hello.html", context={"name":name})


def is_it_monday(request):
    now = datetime.datetime.now()

    is_monday = now.weekday() == 0

    return render(
        request,
        template_name="hello_app/isitmonday.html",
        context={"is_monday":is_monday})


def dtl(request):
    fruits = [
        "jabłko",
        "banan",
        "winogron",
    ]
    user = {
        "name": "Jan",
        "username": "Kowalski",
        "age": 20
    }

    class Cow:
        def __init__(self, name):
            self.name = name

    cowl = Cow("Mućka")


    return render(
        request,
        template_name="hello_app/dtl.html",
        context={
            "fruits": fruits,
            "user": user,
            "cowl": cowl
        }
    )


def first_view(request):
    return render(
        request, "hello_app/first.html"
    )


def second_view(request):
    return render(
        request, "hello_app/second.html"
    )


def third_view(request, param):
    return render(
        request, "hello_app/third.html", {"param": param}
    )


def child1_view(request):
    return render(request, "hello_app/child1.html")


def child2_view(request):
    return render(request, "hello_app/child2.html")


