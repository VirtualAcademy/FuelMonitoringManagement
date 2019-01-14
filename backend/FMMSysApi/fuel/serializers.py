
from rest_framework import serializers
from .models import Consumption, DailyProductionOnFuel, DeliveryOrder, Fuel, Inventory, SpecificConsumption, StockVariation, StorageUnit, Supplier, Supply, SupplyScheduleTransaction


class ConsumptionSerializer(serializers.ModelSerializer):
	"""Serializer to map the Model instance into JSON format."""

	class Meta:
		"""Meta class to map serializer's fields with the model fields."""
		model = Consumption
		fields = '__all__'


class DailyProductionOnFuelSerializer(serializers.ModelSerializer):
	"""Serializer to map the Model instance into JSON format."""

	class Meta:
		"""Meta class to map serializer's fields with the model fields."""
		model = DailyProductionOnFuel
		fields = '__all__'
		read_only_fields = ('date_created', 'date_modified')


class DeliveryOrderSerializer(serializers.ModelSerializer):
	"""Serializer to map the Model instance into JSON format."""

	class Meta:
		"""Meta class to map serializer's fields with the model fields."""
		model = DeliveryOrder
		fields = '__all__'
		read_only_fields = ('date_created', 'date_modified')

class FuelSerializer(serializers.ModelSerializer):
	"""Serializer to map the Model instance into JSON format."""

	class Meta:
		"""Meta class to map serializer's fields with the model fields."""
		model = Fuel
		fields = '__all__'

class InventorySerializer(serializers.ModelSerializer):
	"""Serializer to map the Model instance into JSON format."""

	class Meta:
		"""Meta class to map serializer's fields with the model fields."""
		model = Inventory
		fields = '__all__'
		read_only_fields = ('date_created', 'date_modified')

class SpecificConsumptionSerializer(serializers.ModelSerializer):
	"""Serializer to map the Model instance into JSON format."""

	class Meta:
		"""Meta class to map serializer's fields with the model fields."""
		model = SpecificConsumption
		fields = '__all__'
		read_only_fields = ('date_created', 'date_modified')

class StockVariationSerializer(serializers.ModelSerializer):
	"""Serializer to map the Model instance into JSON format."""

	class Meta:
		"""Meta class to map serializer's fields with the model fields."""
		model = StockVariation
		fields = '__all__'
		read_only_fields = ('date_created', 'date_modified')

class SupplyScheduleTransactionSerializer(serializers.ModelSerializer):
	"""Serializer to map the Model instance into JSON format."""

	class Meta:
		"""Meta class to map serializer's fields with the model fields."""
		model = SupplyScheduleTransaction
		fields = '__all__'
		read_only_fields = ('date_created', 'date_modified')

class SupplySerializer(serializers.ModelSerializer):
	"""Serializer to map the Model instance into JSON format."""

	class Meta:
		"""Meta class to map serializer's fields with the model fields."""
		model = Supply
		fields = '__all__'
		read_only_fields = ('date_created', 'date_modified')

class StorageUnitSerializer(serializers.ModelSerializer):
	"""Serializer to map the Model instance into JSON format."""

	class Meta:
		"""Meta class to map serializer's fields with the model fields."""
		model = StorageUnit
		fields = '__all__'

class SupplierSerializer(serializers.ModelSerializer):
	"""Serializer to map the Model instance into JSON format."""

	class Meta:
		"""Meta class to map serializer's fields with the model fields."""
		model = Supplier
		fields = '__all__'