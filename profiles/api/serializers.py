from rest_framework import serializers

from profiles.models import Profile, Comment


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'first_name', 'last_name', 'phone', 'address', 'date_created', 'last_comment',
                  'comments_count')

    last_comment = serializers.CharField()




