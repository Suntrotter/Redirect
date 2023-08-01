from django.contrib import admin
from django.urls import path, include
from month.urls import urlpatterns
from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urlpatterns)),
    ]