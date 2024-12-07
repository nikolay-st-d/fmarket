from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web.urls')),
    path('accounts/', include('accounts.urls')),
    path('sellers/', include('sellers.urls')),
    path('products/', include('products.urls')),
    path('reviews/', include('reviews.urls')),
    path('topics/', include('topics.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
