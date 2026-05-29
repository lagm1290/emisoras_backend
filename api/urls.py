from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'emisoras', views.EmisoraViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('cadenas/', views.cadenas_list, name='cadenas-list'),
    path('ciudades/', views.ciudades_list, name='ciudades-list'),
]
