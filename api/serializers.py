from rest_framework import serializers
from .models import User, Reading

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username',)

class ReadingSerializer(serializers.ModelSerializer):
    systolic = serializers.IntegerField()
    diastolic= serializers.IntegerField()
    reading_time = serializers.DateTimeField()

    class Meta:
        model = Reading
        fields= ('systolic', 'diastolic', 'reading_time', 'id',)