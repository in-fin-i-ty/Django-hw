from django.urls import path
from .views import contacts, index

urlpatterns = [
    path('main.contacts/', contacts),
    path('', index)
]
