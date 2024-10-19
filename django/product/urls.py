from django.urls import path
from .views import ProductViewSets, UserApiView

urlpatterns = [
    path('products', ProductViewSets.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('products/<int:pk>', ProductViewSets.as_view({
        'get': 'retrieve',
        'patch': 'update',
        'delete': 'destroy'
    })),
    path('user', UserApiView.as_view())
]
