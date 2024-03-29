"""makewiki URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


"""
CHALLENGES:
    1. Uncomment the path() for the wiki app below. Use it to direct any request (except `/admin` URLs)
        to the the `wiki` app's URL configuration. Use the above docstring to guide you if you feel stuck.
    2. Make sure Django doesn't give you any warnings or errors when you execute `python manage.py runserver`.
"""
urlpatterns = [
    path('maps/', include('maps.urls')),
    # Admin Site
    path('admin/', admin.site.urls),
    path('', include('wiki.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/', include('api.urls')),


    # Wiki App

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
