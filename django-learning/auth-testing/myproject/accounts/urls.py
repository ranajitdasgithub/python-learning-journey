from django.urls import path
from dj_rest_auth.registration.views import RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='rest_register'),
]
