from django.conf.urls import url

from . import views

app_name = "expenses"
urlpatterns = [
    url(r'^$', views.expense_list, name="list"),
    url(r'^(?P<id>[0-9]+)/$', views.expense_detail, name="detail"),
]
