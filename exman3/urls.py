from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout_then_login

urlpatterns = [
    url(r"", include("expenses.urls")),
    url(r"^login/$", login, kwargs={
        'template_name': 'form.html',
    }, name="login"),
    url(r"^logout/$", logout_then_login, name="logout"),
    url(r'^admin/', admin.site.urls),
]
