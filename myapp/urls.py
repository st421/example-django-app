from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^user/new/$', views.add_user, name="add_user"),
    url(r'^user/get/$', views.get_user, name="get_user")
]
