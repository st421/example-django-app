from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^signup$', views.signup, name="signup"),
    url(r'^user/new$', views.signup),
    url(r'^profile$', views.profile, name="profile"),
    url(r'^login$', views.user_login, name="login"),
    url(r'^logout$', views.user_logout, name="logout"),
    url(r'^user/get$', views.user_login),
    url(r'^task/new$', views.new_task),
]
