from django.urls import path,include
from user_detail_app import views

app_name='user_detail_app'
urlpatterns = [
    
    path('',views.index,name='index'),
    # path('subscribe',views.subscribe,name='subscribe'),
    path('subscribe/<int:id>',views.subscribe,name='subscribe'),
    path('register_email',views.register_email,name='register_email'),
    path('save_players',views.save_players,name='save_players'),
]
