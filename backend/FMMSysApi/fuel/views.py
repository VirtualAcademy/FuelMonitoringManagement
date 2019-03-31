from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ConsumptionSerializer, DailyProductionOnFuelSerializer, DeliveryOrderSerializer, FuelSerializer, \
	InventorySerializer, SpecificConsumptionSerializer, StockVariationSerializer, StorageUnitSerializer, SupplierSerializer, SupplySerializer, SupplyScheduleTransactionSerializer

from .models import Consumption, DailyProductionOnFuel, DeliveryOrder, Fuel, Inventory, SpecificConsumption, StockVariation, StorageUnit, Supplier, Supply, SupplyScheduleTransaction


class ConsumptionViewSet(viewsets.ModelViewSet):
    """This class handles the http GET, PUT and DELETE requests."""
    name = 'Modify Consumption Details'

    queryset = Consumption.objects.all()
    serializer_class = ConsumptionSerializer
    

class DailyProductionOnFuelViewSet(viewsets.ModelViewSet):
    """This class handles the http GET, PUT and DELETE requests."""
    name = 'Modify Daily Production on Fuel Details'

    queryset = DailyProductionOnFuel.objects.all()
    serializer_class = DailyProductionOnFuelSerializer


class DeliveryOrderViewSet(viewsets.ModelViewSet):
    """This class handles the http GET, PUT and DELETE requests."""
    name = 'Modify Delivery Order Details'

    queryset = DeliveryOrder.objects.all()
    serializer_class = DeliveryOrderSerializer



class FuelViewSet(viewsets.ModelViewSet):
    """This class handles the http GET, PUT and DELETE requests."""
    name = 'Modify Fuel Details'

    queryset = Fuel.objects.all()
    serializer_class = FuelSerializer



class InventoryViewSet(viewsets.ModelViewSet):
    """This class handles the http GET, PUT and DELETE requests."""
    name = 'Modify Inventory Details'

    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer



class SpecificConsumptionViewSet(viewsets.ModelViewSet):
    """This class handles the http GET, PUT and DELETE requests."""

    name = 'Modify Specific Consumption'

    queryset = SpecificConsumption.objects.all()
    serializer_class = SpecificConsumptionSerializer


class StockVariationViewSet(viewsets.ModelViewSet):
    """This class handles the http GET, PUT and DELETE requests."""
    name = 'Modify Stock Variation Details'

    queryset = StockVariation.objects.all()
    serializer_class = StockVariationSerializer


class StorageUnitViewSet(viewsets.ModelViewSet):
    """This class handles the http GET, PUT and DELETE requests."""
    name = 'Modify Storage Unit Details'

    queryset = StorageUnit.objects.all()
    serializer_class = StorageUnitSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    """This class handles the http GET, PUT and DELETE requests."""
    name = 'Modify Supplier Details'

    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class SupplyViewSet(viewsets.ModelViewSet):
    """This class handles the http GET, PUT and DELETE requests."""
    name = 'Modify Supply Details'

    queryset = Supply.objects.all()
    serializer_class = SupplySerializer


class SupplyScheduleTransactionViewSet(viewsets.ModelViewSet):
    """This class handles the http GET, PUT and DELETE requests."""

    name = 'Modify Supply Schedule Transaction'

    queryset = SupplyScheduleTransaction.objects.all()
    serializer_class = SupplyScheduleTransactionSerializer