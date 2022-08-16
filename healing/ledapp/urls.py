from . import views
from django.urls import path

urlpatterns = [
    path('<str:colorpk>/',views.LEDColorView.as_view()),
]
