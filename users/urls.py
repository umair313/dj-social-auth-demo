from django.urls import path
from .views import FacebookLogin, GoogleLogin
urlpatterns = [
    path('facebook-login/', FacebookLogin.as_view(), name="fb_auth"),
    path('google-login/', GoogleLogin.as_view(), name="google_auth")
]
