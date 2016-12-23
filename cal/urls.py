from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.workoutsession_list, name='workoutsession_list'),
]
