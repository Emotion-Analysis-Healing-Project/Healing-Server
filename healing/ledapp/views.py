from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *

class LEDColorView(APIView):
    def put(self, request, colorpk):
        led=LED.objects.get(color=colorpk)
        print(colorpk)
        f=0
        for i in LED.get_color(led):
            if colorpk==i[0]:
                print(i[0])
                f=1
        if f==0:
            return Response({'error':'no such color'}, status=status.HTTP_400_BAD_REQUEST)

        if led.state=='1':
            led.state=0
        else:
            led.state=1
        led.save()
        return Response(led.state)
