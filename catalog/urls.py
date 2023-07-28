from django.urls import path
from .views import contacts, index, product
from .apps import MainConfig

app_name = MainConfig.name

urlpatterns = [
    path('main.contacts/', contacts, name='contacts'),
    path('', index, name='index'),
    # path('<int:pk>main.product/', product, name='product'),
    path('product/<int:pk>/', product, name='product'),
]
