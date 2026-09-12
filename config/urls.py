from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token  #[cite: 1, 2]
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from biblioteca.views import AutorViewSet, LibroViewSet, PrestamoViewSet

router = DefaultRouter()
router.register(r'autores', AutorViewSet)
router.register(r'libros', LibroViewSet)
router.register(r'prestamos', PrestamoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Endpoints CRUD
    path('api/', include(router.urls)),
    
    # Endpoint de Login (Obtener Token)
    path('api/login/', obtain_auth_token, name='api_token_auth'),  #[cite: 1, 2]
    
    # Documentación OpenAPI / Swagger
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]