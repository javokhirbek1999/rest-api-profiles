from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=15)


class PopulationSerializer(serializers.Serializer):
    country = serializers.CharField(max_length=20)
    population = serializers.IntegerField()
    year = serializers.IntegerField()

class Jobs(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    position = serializers.CharField(max_length=150)
    company = serializers.CharField(max_length=100)
    location = serializers.CharField(max_length=100)
    salary = serializers.DecimalField(max_digits=None,decimal_places=2)

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user model object"""

    class Meta:
        model = models.UserProfile
        fields = ('id','email','name','password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type':'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user

class CreateUserProfiles(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ('id','email','name','password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type':'password'}
            }
        }
    
    def create(self,validated_data):
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user


