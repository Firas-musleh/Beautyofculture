"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from bock import views

from django.utils.translation import gettext_lazy as _
from django.views.i18n import JavaScriptCatalog

urlpatterns = [
    path('selectlanguage', views.selectlanguage, name='selectlanguage'),
    path('selectcurrency', views.selectcurrency, name='selectcurrency'),
    path('i18n/', include('django.conf.urls.i18n')),
]


urlpatterns += i18n_patterns(
    path('currencies/', include('currencies.urls')),
    path('admin/', admin.site.urls),
    path("cart/", include("cart.urls", namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('', include('bock.urls', namespace='ost')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    prefix_default_language=False,
)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


def get_filename(filename, request):
    return filename.upper()
