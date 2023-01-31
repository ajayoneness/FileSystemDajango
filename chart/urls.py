from django.urls import path
from .views import codeAj,get_bot_response

urlpatterns = [
    path('',codeAj,name="codeaj"),
    path('get/',get_bot_response,name='botresponse')



    ]