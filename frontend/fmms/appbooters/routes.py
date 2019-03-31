from ..management import production, supplies, consumption
from ..monitoring import overview, dashboard, connectednetworks
from .. import home

routes = {
	'/':  home.home,
	'/Dashboard': dashboard.dashboard,
	'/Monitoring': overview.overview,
	'/manage/production': production.production,
	'/manage/production': production.production,
	'/manage/consumption': consumption.consumption,
	'/manage/production': production.production,
	'/manage/supplies': supplies.supply}