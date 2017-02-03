from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^signup$', views.signup, name="signup"),
    url(r'^profile$', views.profile, name="profile"),
    url(r'^login$', views.user_login, name="login"),
    url(r'^logout$', views.user_logout, name="logout"),
    url(r'^new/task$', views.new_task, name="new_task"),
    url(r'^finish/task$', views.finish_task, name="finish_task"),
]
