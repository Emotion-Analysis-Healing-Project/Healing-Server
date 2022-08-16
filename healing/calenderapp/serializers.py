from .models import Calender
from rest_framework import serializers

class CalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Calender
        fields='__all__'
