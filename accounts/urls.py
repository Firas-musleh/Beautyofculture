from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('signup', views.signup, name='signup'),

   
    path('om_oss/', views.om_oss, name='om_oss'),
   
    path('profile', views.view_profile, name='view_profile'),
]
