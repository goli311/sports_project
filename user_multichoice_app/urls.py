from django.urls import path,include
from user_multichoice_app import views

app_name='user_multichoice_app'
urlpatterns = [
    
    path('',views.index,name='index'),
    path('user_subscribe',views.user_subscribe,name='user_subscribe'),
    path('send_mail',views.send_mail1,name='send_mail1'),
]
