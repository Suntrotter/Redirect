from django.http import request

from month import views
from django.urls import path

from month.views import *

urlpatterns = [
    path("", views.year_plans),
    path("<str:title>", views.month_plan, name="http://127.0.0.1:8000/{item['month']}"),
        ]

