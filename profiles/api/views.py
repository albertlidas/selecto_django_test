from django.views.generic.base import TemplateView
from rest_framework import generics, filters
from .serializers import ProfileSerializer
from profiles.models import Profile, Comment


class RootView(TemplateView):
    template_name = "profiles.html"


class ProfilesListAPIView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('first_name', 'last_name', 'phone', 'address')
    ordering_fields = ('date_created', 'comments_count')
    pagination_class = None

