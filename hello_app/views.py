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
    return render(request, template_name="hello.html", context={"name":name})