from __future__ import unicode_literals

import logging
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

from django.utils.translation import ugettext_lazy as _
from generation.models import AppModel

# Create your models here.

log = logging.getLogger('models')


# Fuel related management model
class Fuel(models.Model):

    HFO = "Heavy Fuel Oil (HFO)"
    LFO = "Light Fuel Oil (LFO)"
    GAS = "Gas(G)"
    OTHER = "Other(O)"

    TYPES = ((1, HFO), (2, LFO), (3, GAS), (4, OTHER))

    fuel_name = models.CharField(
            verbose_name=_("Fuel Name"),
            help_text=_("The name of the type of fuel."), max_length=1000)

    fuel_discription = models.TextField(
            verbose_name=_("Description"),
            help_text=_("Brief description."), max_length=1000, null=True, blank=True)

    fuel_category = models.PositiveIntegerField(
            verbose_name=_("Category"),
            help_text=_("The fuel category or type: HFO or LFO"), choices=TYPES)

    def __str__(self):
        return """{} > {}""".format(
                self.fuel_name,
                dict(self.TYPES).get(self.fuel_category))

    class Meta:
        verbose_name = _("Fuel")
        verbose_name_plural = _("Fuel")


class StorageUnit(models.Model):

	unit_name = models.CharField(
			verbose_name=_("Storage Unit"), max_length=256,
			help_text=_("Name of storage facility"))

	storage_capacity = models.FloatField(
			verbose_name=_("Storage Capacity"),
			help_text=_("The fuel tank storage capacity."))

	measurement = models.CharField(
			verbose_name=_("Measurement"), max_length=256,
			help_text=_("Units of measurement"), default="Litre(L))")

	facility_location = models.CharField(
			verbose_name=_("Facility location"), max_length=256,
			help_text=_("The fuel reservoir location or power plant."))

	fuel = models.ForeignKey(
			Fuel,
			verbose_name=_("Fuel"),
			help_text=_("The fuel product in the reservoir or storage unit."),
			on_delete=models.CASCADE, related_name='storage_units')

	def __str__(self):
		return "{} Storage Unit of {}{} capacity".format(
				self.unit_name,
				self.storage_capacity,
				self.measurement)

	class Meta:
		verbose_name = _("Storage Unit")
		verbose_name_plural = _("Storage Units")


class DailyProductionOnFuel(AppModel):

	storage_area = models.ForeignKey(
            StorageUnit,
            verbose_name=_("Storage Unit"),
            help_text=_("The Production realise with fuel from this storage unit"), on_delete=models.CASCADE)

	power_units = models.FloatField(
            verbose_name=_("Power Available"),
            help_text=_("Amount of power that can be generated"), max_length=1000, default=0)

	unit_measurement = models.CharField(
            verbose_name=_("Unit of measurement"),
            help_text=_("The unit of measurement in which power is quantified"), max_length=256, default="MW(Mega Watts)")

	date_recorded = models.DateField(verbose_name=_("Date"), default=datetime.today, blank=False)

	def __str__(self):
		return "Daily Power production from {} on {}".format(self.storage_area, self.date_recorded.isoformat())

	class Meta:
		verbose_name = _("Production Realisation")
		verbose_name_plural = _("Production Realisations")


class SpecificConsumption(models.Model):

    storage_area = models.ForeignKey(
            StorageUnit,
            verbose_name=_("Storage Unit"),
            help_text=_("The consumption rate with fuel from this storage unit"), on_delete=models.CASCADE)


    specific_consumptions = models.FloatField(
            verbose_name=_("Specific Consumption"),
            help_text=_("The rate of fuel consumption per m3 to generated 1MWH of energy"), max_length=1000, default=0)

    date_recorded = models.DateField(verbose_name=_("Date"), default=datetime.today, blank=False)

    def __str__(self):
        return "Specific consumption of {} on {}".format(self.specific_consumptions, self.date_recorded.isoformat())

    class Meta:
        verbose_name = _("Specific Consumption")
        verbose_name_plural = _("Specific Consumptions")


class Consumption(AppModel):

	storage_area = models.ForeignKey(
			StorageUnit,
			verbose_name=_("Storage Unit"),
			help_text=_("The Consumption realise with fuel from this storage unit"),
			on_delete=models.CASCADE, related_name='production_realisations')

	quantity_consumed = models.FloatField(
			verbose_name=_("Quantity"),
			help_text=_("The quantity that has been consumed."), default=0)

	measurement = models.CharField(
			verbose_name=_("Measurement"), max_length=256,
			help_text=_("Units of measurement"), default="Litre(L))")

	date_recorded = models.DateField(verbose_name=_("Date"), default=datetime.today, blank=False)

	def __str__(self):
		return """ {} {} consumed on {}""".format(self.quantity_consumed, self.measurement, self.date_recorded.isoformat())


class Inventory(AppModel):

	record_date = models.DateTimeField(verbose_name=_("Date"), default=datetime.today, blank=False)

	storage_unit = models.ForeignKey(
			StorageUnit,
			verbose_name=_("Storage Facility"),
			help_text=_("The record the inventory or physical stock."), on_delete=models.CASCADE)

	quantity = models.FloatField(
			verbose_name=_("Initial Quantity"),
			help_text=_("The quantity left of the inventory on previous day."), default=0)

	measurement = models.CharField(
			verbose_name=_("Measurement"), max_length=256,
			help_text=_("Units of measurement"), default="Litre(L)")

	def __str__(self):
		return self.storage_unit.name+' inventories of '+self.record_date

	class Meta:
		verbose_name = _("Inventory")
		verbose_name_plural = _("Inventories")

class Supplier(AppModel):

	supplier_name = models.CharField(
			verbose_name=_("Fuel Supplier's Name"),
			help_text=_("The name of the fuel supplier.e.g. TOTAL"), max_length=256)

	def __str__(self):
		return self.supplier_name

	class Meta:
		verbose_name = _("Supplier")
		verbose_name_plural = _("Suppliers")


class Supply(AppModel):

	supplier = models.ForeignKey(
			Supplier,
			verbose_name=_("Fuel Supplier"),
			help_text=_("The company that supplies fuel."), on_delete=models.CASCADE, related_name='supplies')

	destined_to = models.ForeignKey(
			StorageUnit,
			verbose_name=_("Fuel Receptacle"),
			help_text=_("The fuel storage unit."), on_delete=models.CASCADE, related_name='supplies')

	quantity_supplied = models.FloatField(
			verbose_name=_("Quantity Supplied"),
			help_text=_("The Supplied quantity."), default=0)

	measurement = models.CharField(
			verbose_name=_("Measurement"), max_length=256,
			help_text=_("Units of measurement"), default="Litre(L)")

	date_recorded = models.DateField(verbose_name=_("Date"), default=datetime.today, blank=False)

	def __str__(self):
		return """{} {} Supplied on {}""".format(self.quantity_supplied, self.measurement, self.date_recorded.isoformat())

	class Meta:
		verbose_name = _("Supply")
		verbose_name_plural = _("Supplies")


class StockVariation(AppModel):

	record_date = models.DateTimeField(verbose_name=_("Date"), default=datetime.today, blank=False)

	storage_unit = models.ForeignKey(
			StorageUnit,
			verbose_name=_("Storage Facility"),
			help_text=_("The record changes in inventory."), on_delete=models.CASCADE)

	initial_qty = models.FloatField(
			verbose_name=_("Initial Quantity"),
			help_text=_("The quantity left of the inventory on previous day."), default=0)

	qty_added = models.ForeignKey(
			Supply,
			verbose_name=_("Quantity Supplied"),
			help_text=_("The quantity added from supply."), on_delete=models.CASCADE, default=0)

	qty_removed = models.ForeignKey(
			Consumption,
			verbose_name=_("Quantity Consumed"),
			help_text=_("The quantity to be consumed."), on_delete=models.CASCADE, default=0)

	qty_left = models.FloatField(
			verbose_name=_("Quantity on Hand"),
			help_text=_("The usable quantity left before consumption."), default=0)

	minimum_qty = models.FloatField(
			verbose_name=_("Threshold"),
			help_text=_("The threshold quantity that can't be consumed."), default=0)

	measurement = models.CharField(
			verbose_name=_("Measurement"), max_length=256,
			help_text=_("Units of measurement"), default="Litre(L)")

	def __str__(self):
		return "Recorded on {}".format(self.record_date)

	class Meta:
		verbose_name = _("Inventory Variation")
		verbose_name_plural = _("Inventory Varations")

	def add_stock(self):
		return

class DeliveryOrder(AppModel):

	STATUS=((1,'Created'),(2,'Pending'),(3,'Received'))

	do_number = models.AutoField(
			primary_key=True,
			verbose_name=_("Order number"),
			help_text=_("The ordered number or bond de command of the purchase that has been made to be delivered."),
			unique=True)

	po_date = models.DateField(
			verbose_name=_("Purchase Order Date"),
			help_text=_("The date the purchase was ordered."), default=datetime.today, blank=False)

	po_description = models.TextField(
			verbose_name=_("Order Description"), max_length=256,
			help_text=_("Brief description of the order made including the purchase order number.")
	)

	delivery_status = models.PositiveIntegerField(
			verbose_name=_("Delivery Status"),
			help_text=_("The delivery status.i.e. 'created', 'pending' or 'received'."), choices=STATUS, default=1)

	eta = models.DateField(
			verbose_name=_("Estimated Arrival Date"),
			help_text=_("The Estimated Time of Arrival of the order that is being made."),  default=datetime.today, blank=False)

	order_qty = models.FloatField(
			verbose_name=_("Quantity Ordered"),
			help_text=_("The quantity of fuel ordered."), default=0)

	# created_on = models.DateField(auto_now_add=True)

	created_by = models.ForeignKey(
			User,
			verbose_name=_("Created by"),
			help_text=_("The person who created this order."), on_delete=models.CASCADE, related_name='created_by'
	)

	# modified_on = models.DateField(auto_now=True)

	modified_by = models.ForeignKey(
			User,
			verbose_name=_("Modified by"),
			help_text=_("The person who modified this order."), on_delete=models.CASCADE, related_name='modified_by'
	)

	delievery_item = models.ForeignKey(
			'Fuel',
			verbose_name=_("Item"),
			help_text=_("The item to be delievered."), on_delete=models.CASCADE

	)

	def __str__(self):
		return "Delivery order No.{} for {} on {}".format(str(self.delievery_order),self.delievery_item.fuel_name,self.po_date)

	class Meta:
		verbose_name = _("Delivery Order")
		verbose_name_plural = _("Delivery Orders")


class SupplyScheduleTransaction(AppModel):
	"""Confirm receipt of product"""

	transaction_no = models.AutoField(
			primary_key=True,
			verbose_name=_("Transaction number"),
			help_text=_("The id number for the supply transaction"), default=0)
	transaction_date = models.DateField(
			verbose_name=_("Purchase Order Date"),
			help_text=_("The date the purchase was ordered."), default=datetime.today, blank=False)

	memo = models.TextField(
			verbose_name=_("Memo"), max_length=1000,
			help_text=_("Brief description of the supply schedule including and constraints attached.")
	)

	eta = models.DateField(
			verbose_name=_("Estimated Arrival Date"),
			help_text=_("The Estimated Time of Arrival of the order that is being made."))

	delivery_order = models.ForeignKey(
			DeliveryOrder,
			verbose_name=_("Delivery Order No."),
			help_text=_("The delivery order linked to this receipt confirmation."), on_delete=models.CASCADE,
	)

	# created_on = models.DateField(auto_now_add=True, editable=False)
	#
	# # created_by = models.ForeignKey(
	# # 		User,
	# # 		verbose_name=_("Created by"),
	# # 		help_text=_("The person who created this schedule."), on_delete=models.CASCADE, related_name='delivery_schedule'
	# # )
	#
	# modified_on = models.DateField(auto_now=True, editable=False)

	# modified_by = models.ForeignKey(
	# 		User,
	# 		verbose_name=_("Modified by"),
	# 		help_text=_("The person who modified this schedule."), on_delete=models.CASCADE, related_name='delivery_orders'
	# )

	def __str__(self):
		return "Delivery Schedule No.{} for D.O no.{} on {}".format(str(self.transaction_no),self.delivery_order,self.transaction_date)

	class Meta:
		verbose_name = _("Delivery Schedule")
		verbose_name_plural = _("Delivery Schedules")

