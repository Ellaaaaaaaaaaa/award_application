from django.conf.urls import url

from . import views

urlpatterns = (
    url(r'^$', views.home),
    url(r'^organization/$', views.organization),
    url(r'^award/$', views.award),
    url(r'^batch_copy/$', views.batch_copy),
    url(r'^save_org_info/$', views.save_org_info),
    url(r'^get_org_list/$', views.get_org_list),
    url(r'^get_org_select_data/$', views.get_org_select_data),
    url(r'^get_org_info/(?P<org_id>\d+)/', views.get_org_info_by_id),
    url(r'^delete_org_info/(?P<org_id>\d+)/', views.delete_org_info),
    url(r'^get_award_list/$', views.get_award_list),
    url(r'^get_award_copy_list/$', views.get_award_copy_list),
    url(r'^save_award_info/$', views.save_award_info),
    url(r'^get_award_info/(?P<award_id>\d+)/', views.get_award_info_by_id),
    url(r'^get_award_display_info/(?P<award_id>\d+)/', views.get_award_display_info_by_id),
    url(r'^delete_award_info/(?P<award_id>\d+)/', views.delete_award_info),
    url(r'^batch_copy_award_data/$', views.batch_copy_award_data),
    url(r'^get_org_list/$', views.get_org_list),
)