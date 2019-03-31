"""FMMSysApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
# from datetime import datetime
# from django.views.generic import TemplateView
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from apiauth.views import HomeView
# from rest_framework_jwt.views import refresh_jwt_token



schema_view = get_schema_view(title='FMMS API')


version = settings.APP_VERSION
root_url = settings.APIBASE_URL
urlpatterns = [
    path(r'', HomeView.as_view(),name="home"),
    path('admin/', admin.site.urls),
    path('schema/', schema_view),
    path(root_url+'auth/', include('apiauth.urls')),
    path(root_url+'generate/', include('generation.urls')),
    path(root_url+'fuel/', include('fuel.urls')),
    path(root_url+'docs/', include_docs_urls(title='Fuel Monitoring and Management System APIv0.{} Document'.format(version), public=False))
]
