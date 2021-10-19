
from .models import Property, Activity, Survey
from rest_framework import serializers

class SerializedProperty(serializers.ModelSerializer):

    class Meta:
        model = Property
        fields = ('id', 'title','address')


class SerializedCreateProperty(serializers.ModelSerializer):

    class Meta:
        model = Property
        fields = '__all__'

    def create(self, validated_data):
        """
        Create and return a new `Activity` instance, given the validated data.
        """
        return Property.objects.create(**validated_data)


class SerializedActivity(serializers.ModelSerializer):

    class Meta:
        model = Activity
        fields = ('id', 'schedule', 'title','created_at','status','property')


class SerializedCreateActivity(serializers.ModelSerializer):
    schedule = serializers.DateTimeField()


    class Meta:
        model = Activity
        fields = '__all__'


    def create(self, validated_data):
        """
        Create and return a new `Activity` instance, given the validated data.
        """
        return Activity.objects.create(**validated_data)


class SerializedSurvey(serializers.ModelSerializer):

    class Meta:
        model = Survey
        fields = ('answers')