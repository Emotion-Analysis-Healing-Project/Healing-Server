from .models import LED
from rest_framework import serializers

class LEDSerializer(serializers.ModelSerializer):
    class Meta:
        model=LED
        fields=['id','color','state']

    def get_state(self):
        return self.state