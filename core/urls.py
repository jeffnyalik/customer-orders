
from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls'), name='api'),
    path('snippets/v1', include('snipptes.urls'), name='snipptes'),
    # re_path(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]