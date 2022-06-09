from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('', include('content.urls'), name='home'),
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls'), name='shop'),
    path('cart/', include('cart.urls'), name='cart'),

]
handler404 = "main.views.page_not_found_view"

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
