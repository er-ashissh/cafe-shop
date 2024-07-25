from django.contrib import admin
from django.urls import path
from users.api_views.user_api_view import UserApiView
from users.web_views import user_web_view


urlpatterns = [
    # -> APIs View
    path('register-api/', UserApiView.register),
    path('activation-api/', UserApiView.activation),
    path('login-api/', UserApiView.login),

    # -> Webs Views
    path('register/', user_web_view.register, name='user-register'),
    path('activation/', user_web_view.activation, name='user-activation'),
    path('login/', user_web_view.login, name='user-login'),
    path('about/', user_web_view.about, name='user-about'),
]