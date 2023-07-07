
from django.urls import path
from .views import  PostViev

urlpatterns = [
    path('', PostViev.as_view())
]
