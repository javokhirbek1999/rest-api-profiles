from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=15)


class PopulationSerializer(serializers.Serializer):
    country = serializers.CharField(max_length=20)
    population = serializers.IntegerField()
    year = serializers.IntegerField()
