# import requests
# from api import config
#
#
# class ApiManager(object):
# 	GET = 'GET'
# 	POST = 'POST'
# 	PUT = 'PUT'
# 	DELETE = 'DELETE'
# 	def __init__(self):
# 		self.base_url = config.BASE_URL['base_url']
#
# 	def get_url(self,url):
# 		"""
# 		:param url:[string] partial resource path
# 		:return: [string] complete url including full domain
# 		"""
# 		return self.base_url+url
#
#
# 	def make_request(self, url, action='GET', **kwargs):
# 		"""
# 		:param url:  [string] representing api resource
# 		:param action: [string] http method in the request
# 		:param kwargs: [dict] params to be pass with either 'post, put, delete' methods
# 		:return: None
# 		"""
# 		action.upper()
# 		params = kwargs
# 		if action == self.GET:
# 			return requests.get(self.get_url(url),params)
# 		elif action == self.POST:
# 			return requests.post(self.get_url(url),json=params)
# 		elif action == self.PUT:
# 			return requests.put(self.get_url(url),json=params)
# 		else:
# 			return "There is and error with your request"
#
#
# class DashBoardManager(ApiManager):
# 	def __init__(self):
# 		super(DashBoardManager,self).__init__()
# 		self.autonomy_url = 'generate/autonomy_left/'
#
# 	def get_autonomy(self,url):
# 		res=self.make_request(url)
# 		if res.status_code == 200:
# 			return res.text
#
#
# # Power Plant related management models
# class PowerPlant(object):
#
#     THERM = "Thermal"
#     HYDRO = "Hydro"
#     OTHER = "Other"
#     TYPES = ((1, HYDRO), (2, THERM), (3, OTHER))
#
#     plant_name =
#
#     location =
#
#     production_capacity =
#
#     power_category =
#
#     placement_priority =
#
#     grouping =
#
# class AutonomyLeft(object):
#
#     power_plant =
#
#     power_autonomy =
#
#     unit_measurement =
#
#     date_recorded =
#
#     time_recorded =
#
#
# class HourlyTotalPowerAvailable(object):
#
#     power_plant =
#     power_units_available =
#     production_capacity =
#     unit_measurement =
#     date_recorded =
#     time_recorded =
#
# class Generators(object):
#
#     gen_number =
#     power_units =
#     unit_measurement =
#     power_plant =
#     date_recorded
#     time_recorded
#
# class Demand(object):
#
#     power_consumer =
#
#     power_units =
#
#     unit_measurement =
#
#     date_recorded =
#
#     time_recorded =
#
# class HourlyProductionForecast(object):
#
#     power_plant =
#
#     power_units =
#
#     unit_measurement = models.CharField(
#             verbose_name=_("Unit of measurement"),
#             help_text=_("The unit of measurement in which power is quantified"), max_length=256, default="MW(Mega Watts)")
#
#     date_recorded = models.DateField(verbose_name=_("Date"), default=datetime.today, blank=False)
#
#     time_recorded = models.TimeField(verbose_name=_("Time"), default=datetime.today, blank=False)
#
#     def __str__(self):
#         return "Hourly Power forecast for {} on {}".format(self.power_plant, self.date_recorded.isoformat(),
#                                                     self.time_recorded.isoformat())
#
#     class Meta:
#         verbose_name = _("Hourly Forecast")
#         verbose_name_plural = _("Hourly Forecast")
