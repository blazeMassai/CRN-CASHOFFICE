from django.urls import re_path
from cr_note import views

from django.urls import path

urlpatterns = [
    re_path(r'^crn/(?P<pk>\d+)$', views.CrnDetailView.as_view(),name='crn_detail'),
    re_path(r'^crn/new/$', views.CreateCrnView.as_view(),name='crn_new'),
    re_path(r'^crn/(?P<pk>\d+)/edit/$', views.CrnUpdateView.as_view(),name='crn_edit'),
    re_path(r'^crn/(?P<pk>\d+)/remove/$', views.CrnDeleteView.as_view(),name='crn_remove'),
    re_path(r'^crn/$' ,views.CrnListView.as_view(),name='crn_list'),
    path('all_crn' ,views.allcrn, name='allcrn'),
]
