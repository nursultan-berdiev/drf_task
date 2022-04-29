from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        print(validated_data)
        user = User(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user
