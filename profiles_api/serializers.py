from django.db.models import fields
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

class Counties(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    capital = serializers.CharField(max_length=200)
    population = serializers.IntegerField()
    gdp = serializers.DecimalField(max_digits=None,decimal_places=2)

class Companies(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    locations_states = ['Default','California','New York','Washington']
    choices_states = [(locations_states[0],'Please select location'),(locations_states[1],'California'),(locations_states[2],'New York'),(locations_states[3],'Washington')]
    hq_location = serializers.ChoiceField(choices=choices_states)
    founded = serializers.CharField(max_length=200)
    revenue = serializers.DecimalField(decimal_places=2,max_digits=None)

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


class UserProfSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserProfile
        fields = ('id','email','name','password')
        extra_kwargs = {
            'password':{
                'write_only':True,
                'style':{'input_style':'password'}
            }
        }

    def create(self, validated_data):
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
        )
        return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serilaizers profile feed items"""
    class Meta:
        model = models.ProfileFeedItem
        fields = ('id','user_profile','status_text','created_on')
        extra_kwargs = {
            'user_profile':{
                'read_only':True
            }
        }

class ProfileFeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProfileFeedItem
        fields = ('id','user_profile','status_text','created_on')
        extra_kwargs = {
            'user_profile':{
                'read_only':True
            }
        }