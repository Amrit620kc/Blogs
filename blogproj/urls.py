"""
URL configuration for blogproj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'SUDURTECH'                    # default: "Django Administration"
admin.site.index_title = 'SUDURTECH'                 # default: "Site administration"
admin.site.site_title = 'SUDURTECH' # default: "Django site admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("blogapp.urls")),
    path('tinymce/', include('tinymce.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
