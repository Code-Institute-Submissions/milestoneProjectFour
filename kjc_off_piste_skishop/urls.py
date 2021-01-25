"""kjc_off_piste_skishop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('profile/', include('profiles.urls')),
    path('about/', include('about.urls')),
    path('contact/', include('contact.urls')),
    path('categories/', include('categories.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(
#     settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# if settings.SERVE_MEDIA_FILES:
#     urlpatterns += patterns('',
#         url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL.lstrip('/'),
#             'django.views.static.serve',
#             {'document_root': settings.MEDIA_ROOT}),)