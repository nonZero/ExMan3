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
from django.http.response import HttpResponse


def f(request):
    # assert False, request.META['HTTP_USER_AGENT']
    return HttpResponse("shalom shalom!")
    # return HttpResponse("shalom shalom!", content_type="text/plain")
    # return HttpResponse("shalom shalom!", status=404)


def kuku_view(request, n):
    return HttpResponse("KUKU! " + "*" * int(n))


urlpatterns = [
    url(r"^$", f),
    url(r"^stars/([0-9]+)/$", kuku_view),
    url(r'^admin/', admin.site.urls),
]
