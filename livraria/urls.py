from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import routers

from core import views

router = routers.DefaultRouter()
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'editora', views.EditoraViewSet)
router.register(r'autor', views.AutorViewSet)
router.register(r'livro', views.LivroViewSet)
router.register(r'compras', views.CompraViewSet)


urlpatterns = [
    # YOUR PATTERNS
]


urlpatterns = [
    path('admin/', admin.site.urls),
    #OpenAPI3
    path('api/schema', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    #Autenticação
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #Endpoints
    path('teste/', views.teste),
    path('pag/', views.teste2),
    path('categorias-class/', views.CategoriaView.as_view()),
    path('categorias-class/<int:id>/', views.CategoriaView.as_view()),
    path('categorias-apiview/', views.CategoriasList.as_view()),
    path('categorias-apiview/<int:id>', views.CategoriaDetail.as_view()),
    path('categorias-generic', views.CategoriasListGeneric.as_view()),
    path('categorias-generic/<int:id>', views.CategoriaDetailGeneric.as_view()),
    path('api/', include(router.urls))
]
