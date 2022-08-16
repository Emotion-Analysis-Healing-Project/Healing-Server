from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calender/',include('calenderapp.urls')),
    path('emotion/led/',include('ledapp.urls')),
]
