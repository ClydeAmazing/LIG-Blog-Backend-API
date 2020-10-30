from rest_framework import serializers
from rest_framework.reverse import reverse
from api.models import Post, Comment
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField()

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password_confirmation']

    def save(self):
        account = User(
                        email=self.validated_data['email'],
                        username = self.validated_data['username']
                )

        password = self.validated_data['password']
        password2 = self.validated_data['password_confirmation']

        if password != password2:
            raise serializers.ValidationError({'password': 'Password must match'})
            
        account.set_password(password)
        account.save()