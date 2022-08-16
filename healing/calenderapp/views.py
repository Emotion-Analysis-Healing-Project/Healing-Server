from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import *
from .models import *
from datetime import datetime

class MonthListView(APIView):
    # data 생성
    def post(self, request):
        serializer=CalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # monthpk달의 data 조회
    def get(self, request, monthpk):
        this_year=datetime.now().year
        month_date=Calender.objects.filter(date__year=this_year, date__month=monthpk)
        serializer=CalSerializer(month_date, many=True)
        return Response(serializer.data)