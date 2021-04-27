from rest_framework import serializers


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


