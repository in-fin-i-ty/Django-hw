from django.urls import path
from .views import contacts, IndexListView, ProductDetailView, BlogCreateView, BlogListView, BlogDetailView,\
    BlogUpdateView, BlogDeleteView
from .apps import MainConfig

app_name = MainConfig.name

urlpatterns = [
    path('catalog.contacts/', contacts, name='contacts'),
    path('', IndexListView.as_view(), name='index'),
    # path('<int:pk>catalog.product/', product, name='product'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='detail_product'),
    path('create/', BlogCreateView.as_view(), name='create_blog'),
    path('view/', BlogListView.as_view(), name='view_blog'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='detail_blog'),
    path('edit/<int:pk>/', BlogUpdateView.as_view(), name='update_blog'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete_blog'),
]
