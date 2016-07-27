from django.conf.urls import url

from . import views

app_name = "expenses"
urlpatterns = [
    url(r'^$', views.ExpenseListView.as_view(), name="list"),
    url(r'^(?P<pk>[0-9]+)/$', views.ExpenseDetailView.as_view(),
        name="detail"),
    url(r'^create/', views.ExpenseCreateView.as_view(), name='create'),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.ExpenseUpdateView.as_view(),
        name="update"),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.ExpenseDeleteView.as_view(),
        name="delete"),

    url(r'^contact/', views.contact_us_view, name='contact'),

    url(r'^my/(\d+)/', views.MyView.as_view(), name='my'),

    # url(r'^login/', views.login_view, name='login'),
    # url(r'^logout/', views.logout_view, name='logout'),

]
