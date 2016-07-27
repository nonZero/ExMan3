from django.conf.urls import url

from . import views

app_name = "expenses"
urlpatterns = [
    url(r'^$', views.expense_list, name="list"),
    url(r'^(?P<id>[0-9]+)/$', views.expense_detail, name="detail"),
    url(r'create/', views.expense_create_view, name='create'),

    url(r'contact/', views.contact_us_view, name='contact'),
]
