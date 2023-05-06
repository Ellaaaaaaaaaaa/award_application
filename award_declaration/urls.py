from django.conf.urls import url

from . import views

urlpatterns = (
    url(r'^$', views.home),
    url(r'^organization/$', views.organization),
    url(r'^award/$', views.award),
    url(r'^batch_copy/$', views.batch_copy),
)
