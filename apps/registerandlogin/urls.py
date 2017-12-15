from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^reg$', views.reg),
    url(r'^successfulReg$', views.successfulReg),
    url(r'^login$', views.login),
    url(r'^successfulLog$', views.successfulLog),
]
