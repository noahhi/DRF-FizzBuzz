from rest_framework import serializers
from FizzBuzz_App.models import FizzBuzz

class FizzBuzzSerializer(serializers.ModelSerializer):
    class Meta:
        model = FizzBuzz
        fields = ['fizzbuzz_id', 'useragent', 'creation_date', 'message']


    def create(self, validated_data):
        """
        Create and return a new fizzBuzz instance, given the validated data
        """
        return FizzBuzz.objects.create(**validated_data)