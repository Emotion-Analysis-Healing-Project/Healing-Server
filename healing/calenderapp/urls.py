from django.urls import path
from . import views


urlpatterns = [
    path('<int:monthpk>/',views.MonthListView.as_view()),
    path('write/',views.MonthListView.as_view()),

]