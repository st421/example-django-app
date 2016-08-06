from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^profile$', views.profile, name="profile"),
    url(r'^user/new/$', views.signup, name="signup"),
    url(r'^user/get/$', views.user_login, name="login"),
    url(r'^task/new/$', views.new_task, name="new_task"),
]
