from rest_framework import serializers,fields
from django.contrib.auth import get_user_model

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=get_user_model()
        # fields="username,"
        fields = ('id', 'username', 'email', 'password')