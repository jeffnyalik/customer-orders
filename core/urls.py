
from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls'), name='api'),
    re_path(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('authentication/', include('authentication.urls'), name='authentication')
]