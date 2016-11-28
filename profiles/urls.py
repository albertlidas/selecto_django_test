from django.conf.urls import url
from profiles.api.views import ProfilesListAPIView, RootView

urlpatterns = [
    url(r'^$', RootView.as_view()),
    url(r'^profiles/$', ProfilesListAPIView.as_view(), name='profiles-list'),
]
