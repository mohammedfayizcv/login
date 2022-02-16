
from unicodedata import name
from django.urls import include, path
from . import views
urlpatterns = [
    path('index',views.funIndex,name='index'),
    path('',views.funLogin,name='login'),
    path('register/',views.funRegist,name='register'),
    path('viewspage/',views.funViews,name='viewspage'),
    path('forgetpass/',views.funForgetPass,name='forgetpass'),
    path('changepass/<token>/',views.funChangePass,name='changepass'),
    path('logout/',views.funLogout,name='logout'),

]
