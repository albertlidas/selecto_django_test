from django.conf.urls import url
from .views import ProfileList

urlpatterns = [
    url(r'^profiles$', ProfileList.as_view(), name='profile-list'),
]
