from rest_framework import serializers
from rest_framework.reverse import reverse
from rest_framework.validators import UniqueValidator
from api.models import Post, Comment
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(error_messages={'required': 'The email field is required.', 
                                                    'blank': 'The email field is required.'})
    password = serializers.CharField(error_messages={'required': 'The password field is required.',
                                                    'blank': 'The password field is required'})

    def validate(self, data):
        email = data['email']
        password = data['password']
        try:
            account = User.objects.get(email=email)
            if not account.check_password(password):
                raise serializers.ValidationError({'password': 'Password incorrect.'})
        except ObjectDoesNotExist:
            raise serializers.ValidationError({'email': 'The credentials do not match our records.'})
        return data

    class Meta:
        model = User
        fields = ['email', 'password']

class RegistrationSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField()
    name = serializers.CharField(required=True, error_messages={'required': 'The name field is required', 'blank': 'The name field is required'})

    class Meta:
        model = User
        fields = ['email', 'password', 'name', 'password_confirmation']
    
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('The email has already been taken.')
        return value
    
    def validate_name(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError('An account with the same name has already exists.')
        return value

    def validate(self, data):
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError({'password': ['The password confirmation does not match.', ]})
        return data

    def save(self):
        account = User(
                        email=self.validated_data['email'],
                        username = self.validated_data['name']
                )
        password = self.validated_data['password']
        account.set_password(password)
        account.save()