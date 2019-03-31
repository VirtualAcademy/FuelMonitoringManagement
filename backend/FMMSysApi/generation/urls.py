from django.conf.urls import url, include
from django.urls import reverse
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PowerPlantViewSet, AutonomyLeftViewSet, HourlyTPAViewSet, GeneratorsViewSet, DemandViewSet, HourlyPFViewSet

router = routers.SimpleRouter()
router.register(r'power_plant', PowerPlantViewSet)
router.register(r'autonomy_left', AutonomyLeftViewSet)
router.register(r'hourly_total_power_available', HourlyTPAViewSet)
router.register(r'generators', GeneratorsViewSet)
router.register(r'demand', DemandViewSet)
router.register(r'hourly_production_forecast', HourlyPFViewSet)
urlpatterns = {
	url(r'^', include(router.urls)),
}

urlpatterns = format_suffix_patterns(urlpatterns)