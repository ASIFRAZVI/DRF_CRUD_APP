from django.urls import path
from .views import *

urlpatterns=[
    path('create/', Crud_Application.as_view(), name="crud_application"),
     path('edit/<int:pk>', Crud_Application.as_view(), name='crud_application_detail'),

]