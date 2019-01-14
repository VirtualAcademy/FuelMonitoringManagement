from django.shortcuts import render
from rest_framework import generics
from .serializers import ConsumptionSerializer, DailyProductionOnFuelSerializer, DeliveryOrderSerializer, FuelSerializer, \
	InventorySerializer, SpecificConsumptionSerializer, StockVariationSerializer, StorageUnitSerializer, SupplierSerializer, SupplySerializer, SupplyScheduleTransactionSerializer

from .models import Consumption, DailyProductionOnFuel, DeliveryOrder, Fuel, Inventory, SpecificConsumption, StockVariation, StorageUnit, Supplier, Supply, SupplyScheduleTransaction


class CreateConsumptionView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    name = 'Create Consumption'
    queryset = Consumption.objects.all()
    serializer_class = ConsumptionSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Consumption."""
        serializer.save()


class ConsumptionDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    name = 'Modify Consumption Details'

    queryset = Consumption.objects.all()
    serializer_class = ConsumptionSerializer


class CreateDailyProductionOnFuelView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    name = 'Create Daily Production on Fuel'
    queryset = DailyProductionOnFuel.objects.all()
    serializer_class = DailyProductionOnFuelSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Daily Production from Fuel."""
        serializer.save()


class DailyProductionOnFuelDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    name = 'Modify Daily Production on Fuel Details'

    queryset = DailyProductionOnFuel.objects.all()
    serializer_class = DailyProductionOnFuelSerializer


class CreateDeliveryOrderView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""

    name = 'Create Delivery Order'
    queryset = DeliveryOrder.objects.all()
    serializer_class = DeliveryOrderSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Delivery Order."""
        serializer.save()


class DeliveryOrderDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    name = 'Modify Delivery Order Details'

    queryset = DeliveryOrder.objects.all()
    serializer_class = DeliveryOrderSerializer


class CreateFuelView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    name = 'Create Fuel'
    queryset = Fuel.objects.all()
    serializer_class = FuelSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Fuel."""
        serializer.save()


class FuelDetailstView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    name = 'Modify Fuel Details'

    queryset = Fuel.objects.all()
    serializer_class = FuelSerializer


class CreateInventoryView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    name = 'Create Inventory'
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Inventory."""
        serializer.save()


class InventoryDetailstView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    name = 'Modify Inventory Details'

    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class CreateSpecificConsumptionView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    name = 'Create Specific Consumption'
    queryset = SpecificConsumption.objects.all()
    serializer_class = SpecificConsumptionSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Specific Consumption."""
        serializer.save()

class SpecificConsumptionDetailstView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    name = 'Modify Specific Consumption'

    queryset = SpecificConsumption.objects.all()
    serializer_class = SpecificConsumptionSerializer


class CreateStockVariationView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    name = 'Create Stock Variation'
    queryset = StockVariation.objects.all()
    serializer_class = StockVariationSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Stock Variation."""
        serializer.save()


class StockVariationDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    name = 'Modify Stock Variation Details'

    queryset = StockVariation.objects.all()
    serializer_class = StockVariationSerializer


class CreateStorageUnitView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""

    name = 'Create Storage Unit'
    queryset = StorageUnit.objects.all()
    serializer_class = StorageUnitSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Storage Unit."""
        serializer.save()


class StorageUnitDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    name = 'Modify Storage Unit Details'

    queryset = StorageUnit.objects.all()
    serializer_class = StorageUnitSerializer


class CreateSupplierView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    name = 'Create Supplier'
    queryset = Fuel.objects.all()
    serializer_class = SupplierSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Supplier."""
        serializer.save()


class SupplierDetailstView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    name = 'Modify Supplier Details'

    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class CreateSupplyView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    name = 'Create Supply'
    queryset = Supply.objects.all()
    serializer_class = SupplySerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Supply."""
        serializer.save()


class SupplyDetailstView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    name = 'Modify Supply Details'

    queryset = Supply.objects.all()
    serializer_class = SupplySerializer


class CreateSupplyScheduleTransactionView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    name = 'Create Supply Schedule Transaction'
    queryset = SupplyScheduleTransaction.objects.all()
    serializer_class = SupplyScheduleTransactionSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Supply Schedule Transaction."""
        serializer.save()

class SupplyScheduleTransactionDetailstView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    name = 'Modify Supply Schedule Transaction'

    queryset = SupplyScheduleTransaction.objects.all()
    serializer_class = SupplyScheduleTransactionSerializer