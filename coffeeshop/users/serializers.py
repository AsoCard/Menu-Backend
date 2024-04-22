from rest_framework import serializers
from coffeeshop.users.models import BaseUser


class SmallUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        fields = ('full_name', 'email')
