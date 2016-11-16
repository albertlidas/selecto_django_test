from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ProfilesListView.as_view(), name='profiles_view'),
]