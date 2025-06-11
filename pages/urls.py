from django.urls import path
from .views import MainAPIView

urlpatterns = [
    path('main/', MainAPIView.as_view(), name='main'),
]
