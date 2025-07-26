from django.urls import path
from .views import WheelSpecificationList, WheelSpecificationCreate

urlpatterns = [
    path('forms/wheel-specifications/', WheelSpecificationList.as_view(), name='wheel-specifications-list'),
    path('forms/wheel-specifications/create/', WheelSpecificationCreate.as_view(), name='wheel-specifications-create'),
]
