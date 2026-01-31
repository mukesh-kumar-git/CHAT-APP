from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='user_list'), 
    path('signup/', views.signup, name='signup'),
    path('chat/<int:user_id>/', views.chat_view, name='chat'),
    path('send/', views.send_message, name='send_message'),
    path('messages/<int:user_id>/', views.get_messages, name='get_messages'),
]
