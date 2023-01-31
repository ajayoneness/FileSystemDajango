from django.urls import path
from . import views
urlpatterns = [
    path('',views.fileHome,name="codeaj"),
    path("disp/",views.display,name="disp"),
    ]