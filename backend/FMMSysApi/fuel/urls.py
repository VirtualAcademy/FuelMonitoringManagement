from django.conf.urls import url, include
from django.urls import reverse
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from .views import ConsumptionViewSet, DailyProductionOnFuelViewSet, DeliveryOrderViewSet, FuelViewSet, InventoryViewSet, SpecificConsumptionViewSet, StockVariationViewSet, StorageUnitViewSet, SupplierViewSet, SupplyViewSet, SupplyScheduleTransactionViewSet


router = routers.SimpleRouter()

router.register(r'consumption', ConsumptionViewSet)
router.register(r'daily_production_on_fuel', DailyProductionOnFuelViewSet)
router.register(r'delivery_order', DeliveryOrderViewSet)
router.register(r'fuel', FuelViewSet)
router.register(r'inventory', InventoryViewSet)
router.register(r'specific_consumption', SpecificConsumptionViewSet)
router.register(r'stock_variation', StockVariationViewSet)
router.register(r'supplies', SupplyViewSet)
router.register(r'storage_unit', StorageUnitViewSet)
router.register(r'supplier', SupplierViewSet)
router.register(r'schedule_transaction', SupplyScheduleTransactionViewSet)



urlpatterns = {
	url(r'^', include(router.urls)),
}

# print(include(router.urls)[0][0].url)
urlpatterns = format_suffix_patterns(urlpatterns)