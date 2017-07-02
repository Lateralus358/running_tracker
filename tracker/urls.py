from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.track_list, name='track_list'),
    url(r'^tracker/dashboard/$', views.tracker_dashboard, name='tracker_dashboard'),
]