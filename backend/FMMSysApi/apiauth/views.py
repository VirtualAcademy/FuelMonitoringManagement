from django.shortcuts import render
import math as m
from datetime import datetime
from django.views.generic import TemplateView
from django.conf import settings
from django.contrib.auth.models import User
from generation.urls import urlpatterns as gurls


# Create your views here.

# class UserViewSet(viewsets.ReadOnlyModelViewSet):
#     """
#     This viewset automatically provides `list` and `detail` actions.
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


class HomeView(TemplateView):
    template_name = 'rest_framework/home.html'
    name = "home"

    def get_context_data(self, **kwargs):

        # gen = settings.ROOT_URLCONF #set([i.name for i in gurls.__iter__() if  'details' not in i.name.split('_')])
        # fu = set([i.name for i in furls.__iter__() if  'details' not in i.name.split('_')])
        # print(gen)
        dt = datetime.now()
        context = super(HomeView, self).get_context_data(**kwargs)
        ctxt = {'d':dt.strftime('%Y-%m-%d'),'t':dt.strftime('%H:%M:%S')}
        context['data'] = ctxt
        # context['half'] = m.ceil(len(endpoints)/2)
        # context['endpoints'] = endpoints
        context['version'] = settings.APP_VERSION
        context['update'] = settings.UPDATED
        context['app_root'] = settings.APIBASE_URL
        return context