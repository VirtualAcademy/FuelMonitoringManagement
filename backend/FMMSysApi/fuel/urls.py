from django.conf.urls import url, include
from django.urls import reverse
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateConsumptionView, CreateDailyProductionOnFuelView, CreateDeliveryOrderView, CreateFuelView, CreateInventoryView, CreateSpecificConsumptionView, CreateStockVariationView, CreateStorageUnitView,CreateSupplierView,CreateSupplyView,CreateSupplyScheduleTransactionView,\
	ConsumptionDetailsView, DailyProductionOnFuelDetailsView, DeliveryOrderDetailsView, FuelDetailstView, InventoryDetailstView, SpecificConsumptionDetailstView, StockVariationDetailsView, StorageUnitDetailsView, SupplierDetailstView, SupplyDetailstView, SupplyScheduleTransactionDetailstView

urlpatterns = {
	url(r'^consumption/$', CreateConsumptionView.as_view(), name="consumption"),
	url(r'^consumption/(?P<pk>[0-9]+)/modify/$', ConsumptionDetailsView.as_view(), name="consumption_details"),

	url(r'^daily_production_on_fuel/$', CreateDailyProductionOnFuelView.as_view(), name="daily_production_on_fuel"),
	url(r'^daily_production_on_fuel/(?P<pk>[0-9]+)/modify/$', DailyProductionOnFuelDetailsView.as_view(), name="daily_production_on_fuel_details"),

	url(r'^delivery_order/$', CreateDeliveryOrderView.as_view(), name="delivery_order"),
	url(r'^delivery_order/(?P<pk>[0-9]+)/modify/$', DeliveryOrderDetailsView.as_view(), name="delivery_order_details"),

	url(r'^fuel/$', CreateFuelView.as_view(), name="fuel"),
	url(r'^fuel/(?P<pk>[0-9]+)/modify/$', FuelDetailstView.as_view(), name="fuel_details"),

	url(r'^inventory/$', CreateInventoryView.as_view(), name="inventory"),
	url(r'^inventory/(?P<pk>[0-9]+)/modify/$', InventoryDetailstView.as_view(), name="inventory_details"),

	url(r'^specific_consumption/$', CreateSpecificConsumptionView.as_view(), name="specific_consumption"),
	url(r'^specific_consumption/(?P<pk>[0-9]+)/modify/$', SpecificConsumptionDetailstView.as_view(), name="specific_consumption_details"),

	url(r'^stock_variation/$', CreateStockVariationView.as_view(), name="stock_variation"),
	url(r'^stock_variation/(?P<pk>[0-9]+)/modify/$', StockVariationDetailsView.as_view(), name="stock_variation_details"),

	url(r'^storage_unit/$', CreateStorageUnitView.as_view(), name="storage_unit"),
	url(r'^storage_unit/(?P<pk>[0-9]+)/modify/$', StorageUnitDetailsView.as_view(), name="storage_unit_details"),

	url(r'^supplier/$', CreateSupplierView.as_view(), name="supplier"),
	url(r'^supplier/(?P<pk>[0-9]+)/modify/$', SupplierDetailstView.as_view(), name="supplier_details"),

	url(r'^supplies/$', CreateSupplyView.as_view(), name="supplies"),
	url(r'^supplies/(?P<pk>[0-9]+)/modify/$', SupplyDetailstView.as_view(), name="supply_details"),

	url(r'^schedule_transaction/$', CreateSupplyScheduleTransactionView.as_view(), name="schedule_transaction"),
	url(r'^schedule_transaction/(?P<pk>[0-9]+)/modify/$', SupplyScheduleTransactionDetailstView.as_view(), name="schedule_transaction_details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)