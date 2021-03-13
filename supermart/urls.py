from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from bazzar.views import redirect_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include("account.urls", namespace ="account")),
    path('bazzar/', include("bazzar.urls", namespace ="bazzar")),
    path('adminapp/', include("adminapp.urls", namespace ="adminapp")),
    path("", redirect_view),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)
                            
    urlpatterns += static(settings.STATIC_URL,
                            document_root=settings.STATIC_ROOT)