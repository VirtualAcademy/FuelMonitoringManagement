from __future__ import unicode_literals

import logging
from django.db import models
from datetime import datetime
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class AppModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# Power Plant related management models
class PowerPlant(models.Model):

    THERM = "Thermal"
    HYDRO = "Hydro"
    OTHER = "Other"
    TYPES = ((1, HYDRO), (2, THERM), (3, OTHER))

    plant_name = models.CharField(
            verbose_name=_("Power Plant Name"), max_length=1000,
            help_text=_("The name power plant concerned .e.g. Limbe Power Plant(LPP)."))

    location = models.CharField(
            verbose_name=_("Location"), max_length=1000,
            help_text=_("The location of the Power Plant."))

    production_capacity = models.FloatField(
            verbose_name=_("Production Capacity"), max_length=1000,
            help_text=_("The production capacity of the Power Plant in MW(Mega Watt)."), default=0)

    power_category = models.PositiveIntegerField(
            verbose_name=_("Category"),
            help_text=_("The category of the Power Plant .i.e. hydro or thermal"), choices=TYPES, null=False)

    placement_priority = models.PositiveIntegerField(
            verbose_name=_("Placement Priority"),
            help_text=_("The order of the Power Plant placement for generation."), default=1, null=False)
    grouping = models.CharField(
            verbose_name=_("Grouping"), max_length=1000,
            help_text=_("The group to which Power Plant belongs."), null=True, blank=True, editable=False)

    def __str__(self):
        return self.plant_name

    def getcat(self):
        return self.power_category

    class Meta:
        verbose_name = _("Power Plant")
        verbose_name_plural = _("Power Plants")


class AutonomyLeft(AppModel):

    power_plant = models.ForeignKey(
            PowerPlant,
            verbose_name=_("Power Plant"),
            help_text=_("The related Power Plant's Total Autonomy at this time"), on_delete=models.CASCADE, related_name='power_autonomy')

    power_autonomy = models.FloatField(
            verbose_name=_("Duration"),
            help_text=_("How long it can take to generated at full capacity"),default=0)

    unit_measurement = models.CharField(
            verbose_name=_("Unit of measurement"),
            help_text=_("The unit of measurement in which power is quantified"), max_length=256, default="Hours")

    date_recorded = models.DateField(default=datetime.today, blank=False)

    time_recorded = models.TimeField(default=datetime.today, blank=False)

    def __str__(self):
        return "Power Autonomy at {} on {}".format(
                self.power_plant,
                self.date_recorded.isoformat(),
                self.time_recorded.isoformat()
        )

    class Meta:
        verbose_name = _("Autonomy")
        verbose_name_plural = _("Autonomy")


class HourlyTotalPowerAvailable(AppModel):

    power_plant = models.ForeignKey(
            PowerPlant,
            verbose_name=_("Power Plant"),
            help_text=_("The related Power Plant's Total Availability at this time"), on_delete=models.CASCADE, related_name='total_hourly_availabilities')

    power_units_available = models.FloatField(
            verbose_name=_("Total Power Available"),
            help_text=_("Amount of power that can be generated at this time"),default=0)

    production_capacity = models.FloatField(
            verbose_name=_("Production Capacity"),
            help_text=_("The production capacity of the given thermal plant"), default=0)

    unit_measurement = models.CharField(
            verbose_name=_("Unit of measurement"),
            help_text=_("The unit of measurement in which power is quantified"), max_length=256, default="MW(Mega Watts)")

    date_recorded = models.DateField(default=datetime.today, blank=False)

    time_recorded = models.TimeField(default=datetime.today, blank=False)

    def __str__(self):
        return "Power available at {} on {}-{}".format(
                self.power_plant,
                self.date_recorded.isoformat(),
                self.time_recorded.isoformat())

    class Meta:
        verbose_name = _("Total Hourly Available")
        verbose_name_plural = _("Total Hourly Availabilities")


class Generators(AppModel):

    gen_number = models.PositiveIntegerField(
            verbose_name=_("Generator Number"),
            help_text=_("Number given to identify the generator"), default=1)

    power_units = models.FloatField(
            verbose_name=_("Available Power"),
            help_text=_("Amount of power that can be generated"), default=0)

    unit_measurement = models.CharField(
            verbose_name=_("Unit of measurement"),
            help_text=_("The unit of measurement in which power is quantified"), max_length=256, default="MW(Mega Watts)")

    power_plant = models.ForeignKey(
            PowerPlant,
            verbose_name=_("Power Plant"),
            help_text=_("The related Power Plant's given generator's Availability at this time"), on_delete=models.CASCADE, related_name='generators')

    date_recorded = models.DateField(default=datetime.today, blank=False)

    time_recorded = models.TimeField(default=datetime.today, blank=False)

    def __str__(self):
        return "{} Generator {}".format(
                self.power_plant,
                self.gen_number)

    class Meta:
        verbose_name = _("Power Plant Generator")
        verbose_name_plural = _("Power Plant Generators")


class Demand(AppModel):

    power_consumer = models.CharField(
            verbose_name=_("Client"),
            help_text=_("The name of power consumer.e.g. Public Sector"), max_length=256)

    power_units = models.FloatField(
            verbose_name=_("Amount in Demanded"),
            help_text=_("Amount of power required to satisfy client demand at this time."), default=0)

    unit_measurement = models.CharField(
            verbose_name=_("Unit of measurement"),
            help_text=_("The unit of measurement in which power is quantified"), max_length=256, default="MWH(Mega Watts Hours)")

    date_recorded = models.DateField(verbose_name=_("Date"), default=datetime.today, blank=False)

    time_recorded = models.TimeField(verbose_name=_("Time"), default=datetime.today, blank=False)

    def __str__(self):
        return "{} Deamand at {} - {}".format(
                self.power_consumer,
                self.date_recorded,
                self.time_recorded)

    class Meta:
        verbose_name = _("Consumer")
        verbose_name_plural = _("Consumers")


class HourlyProductionForecast(AppModel):

    power_plant = models.ForeignKey(
            PowerPlant,
            verbose_name=_("Power Plant"),
            help_text=_("The Power Production Plant"), on_delete=models.CASCADE, related_name='hourly_forecasts')

    power_units = models.FloatField(
            verbose_name=_("Power Available"),
            help_text=_("Amount of power that can be generated"), max_length=1000, default=0)

    unit_measurement = models.CharField(
            verbose_name=_("Unit of measurement"),
            help_text=_("The unit of measurement in which power is quantified"), max_length=256, default="MW(Mega Watts)")

    date_recorded = models.DateField(verbose_name=_("Date"), default=datetime.today, blank=False)

    time_recorded = models.TimeField(verbose_name=_("Time"), default=datetime.today, blank=False)

    def __str__(self):
        return "Hourly Power forecast for {} on {}".format(self.power_plant, self.date_recorded.isoformat(),
                                                    self.time_recorded.isoformat())

    class Meta:
        verbose_name = _("Hourly Forecast")
        verbose_name_plural = _("Hourly Forecast")
