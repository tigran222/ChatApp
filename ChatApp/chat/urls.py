from django.urls import include, path
from chat import views as chat_views
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns=[
    path('', chat_views.chatPage, name='chat-page'),
    path('auth/login/', LoginView.as_view(template_name='chat/LoginPage.html'), name='login-user'),
    path('auth/logout/', LogoutView.as_view(), name='logout-user'),
    path('register', views.register, name='register'),
]