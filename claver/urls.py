"""claver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
# from home.sitemaps import PortfolioSitemap, ProjectSitemap, SkillSitemap, ServiceSitemap, CategorySitemap
# from django.contrib.sitemaps.views import sitemap


# sitemaps = {
#     'portfolio': PortfolioSitemap,
#     'skills': SkillSitemap,
#     'category': CategorySitemap,
#     'projects': ProjectSitemap,
#     'services': ServiceSitemap,
# }


urlpatterns = [
    path('admin-site/', admin.site.urls),
    # path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('', include("home.urls", namespace='home')),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
