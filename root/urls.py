from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    # swagger
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # admin
    path('admin/', admin.site.urls),

    # my urls
    path('user/', include('user.urls')),
    path('product/', include('product.urls')),
]
