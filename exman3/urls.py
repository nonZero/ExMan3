"""exman3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.http.response import HttpResponse, HttpResponseBadRequest


def f(request):
    # assert False, request.META['HTTP_USER_AGENT']
    return HttpResponse("shalom shalom!")
    # return HttpResponse("shalom shalom!", content_type="text/plain")
    # return HttpResponse("shalom shalom!", status=404)


def kuku_view(request, n):
    return HttpResponse("KUKU! " + "*" * int(n))


def calc(request, x, y):
    return HttpResponse("{x} + {y} = {plus}<br/>{x} * {y} = {mul}".format(
        x=x,
        y=y,
        mul=int(x) * int(y),
        plus=int(x) + int(y),
    ))


def hello(request, age, name):
    try:
        repeat = int(request.GET.get('repeat', 1))
    except ValueError:
        repeat = 1
        # return HttpResponseBadRequest("go fish")

    return HttpResponse("hello {}, you are {} years old.".format(
        name.title(), age,
    ) * repeat)


urlpatterns = [
    url(r"^$", f),

    url(r"^hi/(?P<name>\w+)/(?P<age>[0-9]+)/$", hello),
    url(r"^hi/(?P<age>[0-9]+)/(?P<name>\w+)/$", hello),
    url(r"^hi/(?P<age>[0-9]+)/$", hello, kwargs={'name': 'Foo'}),

    url(r"^calc/([0-9]+)/([0-9]+)/$", calc),
    url(r"^stars/([0-9]+)/$", kuku_view),
    url(r'^admin/', admin.site.urls),
]
