from django.conf.urls import url, include
from django.urls import reverse
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreatePowerPlantView, CreateAutonomyLeftView, CreateHourlyTPAView, CreateGeneratorsView, CreateDemandView, CreateHourlyPFView, \
	PowerPlantDetailsView, AutonomyLeftDetailsView, HourlyTPADetailstView, GeneratorsDetailstView, DemandDetailstView, HourlyPFDetailstView

urlpatterns = {
	url(r'^power_plant/$', CreatePowerPlantView.as_view(), name="power_plant"),
	url(r'^power_plant/(?P<pk>[0-9]+)/modify/$', PowerPlantDetailsView.as_view(), name="power_plant_details"),
	url(r'^autonomy_left/$', CreateAutonomyLeftView.as_view(), name="autonomy_left"),
	url(r'^autonomy_left/(?P<pk>[0-9]+)/modify/$', AutonomyLeftDetailsView.as_view(), name="autonomy_left_details"),
	url(r'^hourly_total_power_available/$', CreateHourlyTPAView.as_view(), name="hourly_total_power_available"),
	url(r'^hourly_total_power_available/(?P<pk>[0-9]+)/modify/$', HourlyTPADetailstView.as_view(), name="hourly_total_power_available_details"),
	url(r'^generators/$', CreateGeneratorsView.as_view(), name="generators"),
	url(r'^generators/(?P<pk>[0-9]+)/modify/$', GeneratorsDetailstView.as_view(), name="generators_details"),
	url(r'^demand/$', CreateDemandView.as_view(), name="demand"),
	url(r'^demand/(?P<pk>[0-9]+)/modify/$', DemandDetailstView.as_view(), name="demand_details"),
	url(r'^hourly_production_forecast/$', CreateHourlyPFView.as_view(), name="hourly_production_forecast"),
	url(r'^hourly_production_forecast/(?P<pk>[0-9]+)/modify/$', HourlyPFDetailstView.as_view(), name="hourly_production_forecast_details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)