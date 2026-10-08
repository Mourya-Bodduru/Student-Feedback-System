from django.urls import path
from .views import *

urlpatterns = [
    path('send_email/',send_email,name='send_email'),
    path('send_otp/',send_otp,name='send_otp'),
    path('validate_otp/',validate_otp,name='validate_otp'),

]