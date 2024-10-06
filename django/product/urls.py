from django.urls import path
from .views import ProductViewSets

urlpatterns = [
    path('products', ProductViewSets.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('products/<int:pk>', ProductViewSets.as_view({
        'get': 'retrieve',
        # 'put': 'update',
        'patch': 'update',
        'delete': 'destroy'
    }))
]
