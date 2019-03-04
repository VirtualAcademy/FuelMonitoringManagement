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
from datetime import datetime
from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import refresh_jwt_token

class HomeView(TemplateView):
    template_name = 'rest_framework/home.html'

    def get_context_data(self, **kwargs):
        from generation.urls import urlpatterns as gurls
        from fuel.urls import urlpatterns as furls

        gen = set([i.name for i in gurls.__iter__() if  'details' not in i.name.split('_')])
        fu = set([i.name for i in furls.__iter__() if  'details' not in i.name.split('_')])
        dt = datetime.now()
        context = super(HomeView, self).get_context_data(**kwargs)
        ctxt = {'d':dt.strftime('%Y-%m-%d'),'t':dt.strftime('%H:%M:%S')}
        context['data'] = ctxt
        context['gen'] = sorted(gen)
        context['fu'] = sorted(fu)
        return context


urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('refresh-token/', refresh_jwt_token),
    path('', HomeView.as_view()),
    path('admin/', admin.site.urls),
    path('generate/', include('generation.urls')),
    path('fuel/', include('fuel.urls')),
    path('docs/', include_docs_urls(title='Fuel Monitoring and Management System APIv0.1 Document', public=False))
]
