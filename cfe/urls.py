from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

def handler400(request, exception):
    from django.shortcuts import render
    return render(request, "error/404.html")



def handler500(request, *args, **kwargs):
    from django.shortcuts import render
    return render(request, "error/500.html")


hander404 = handler400
hander500 = handler500