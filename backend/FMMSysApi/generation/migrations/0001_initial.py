# Generated by Django 2.1.5 on 2019-03-17 15:50

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AutonomyLeft',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('power_autonomy', models.FloatField(default=0, help_text='How long it can take to generated at full capacity', verbose_name='Duration')),
                ('unit_measurement', models.CharField(default='Hours', help_text='The unit of measurement in which power is quantified', max_length=256, verbose_name='Unit of measurement')),
                ('date_recorded', models.DateField(default=datetime.datetime.today)),
                ('time_recorded', models.TimeField(default=datetime.datetime.today)),
            ],
            options={
                'verbose_name_plural': 'Autonomy',
                'verbose_name': 'Autonomy',
            },
        ),
        migrations.CreateModel(
            name='Demand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('power_consumer', models.CharField(help_text='The name of power consumer.e.g. Public Sector', max_length=256, verbose_name='Client')),
                ('power_units', models.FloatField(default=0, help_text='Amount of power required to satisfy client demand at this time.', verbose_name='Amount in Demanded')),
                ('unit_measurement', models.CharField(default='MWH(Mega Watts Hours)', help_text='The unit of measurement in which power is quantified', max_length=256, verbose_name='Unit of measurement')),
                ('date_recorded', models.DateField(default=datetime.datetime.today, verbose_name='Date')),
                ('time_recorded', models.TimeField(default=datetime.datetime.today, verbose_name='Time')),
            ],
            options={
                'verbose_name_plural': 'Consumers',
                'verbose_name': 'Consumer',
            },
        ),
        migrations.CreateModel(
            name='Generators',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('gen_number', models.PositiveIntegerField(default=1, help_text='Number given to identify the generator', verbose_name='Generator Number')),
                ('power_units', models.FloatField(default=0, help_text='Amount of power that can be generated', verbose_name='Available Power')),
                ('unit_measurement', models.CharField(default='MW(Mega Watts)', help_text='The unit of measurement in which power is quantified', max_length=256, verbose_name='Unit of measurement')),
                ('date_recorded', models.DateField(default=datetime.datetime.today)),
                ('time_recorded', models.TimeField(default=datetime.datetime.today)),
            ],
            options={
                'verbose_name_plural': 'Power Plant Generators',
                'verbose_name': 'Power Plant Generator',
            },
        ),
        migrations.CreateModel(
            name='HourlyProductionForecast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('power_units', models.FloatField(default=0, help_text='Amount of power that can be generated', max_length=1000, verbose_name='Power Available')),
                ('unit_measurement', models.CharField(default='MW(Mega Watts)', help_text='The unit of measurement in which power is quantified', max_length=256, verbose_name='Unit of measurement')),
                ('date_recorded', models.DateField(default=datetime.datetime.today, verbose_name='Date')),
                ('time_recorded', models.TimeField(default=datetime.datetime.today, verbose_name='Time')),
            ],
            options={
                'verbose_name_plural': 'Hourly Forecast',
                'verbose_name': 'Hourly Forecast',
            },
        ),
        migrations.CreateModel(
            name='HourlyTotalPowerAvailable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('power_units_available', models.FloatField(default=0, help_text='Amount of power that can be generated at this time', verbose_name='Total Power Available')),
                ('production_capacity', models.FloatField(default=0, help_text='The production capacity of the given thermal plant', verbose_name='Production Capacity')),
                ('unit_measurement', models.CharField(default='MW(Mega Watts)', help_text='The unit of measurement in which power is quantified', max_length=256, verbose_name='Unit of measurement')),
                ('date_recorded', models.DateField(default=datetime.datetime.today)),
                ('time_recorded', models.TimeField(default=datetime.datetime.today)),
            ],
            options={
                'verbose_name_plural': 'Total Hourly Availabilities',
                'verbose_name': 'Total Hourly Available',
            },
        ),
        migrations.CreateModel(
            name='PowerPlant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plant_name', models.CharField(help_text='The name power plant concerned .e.g. Limbe Power Plant(LPP).', max_length=1000, verbose_name='Power Plant Name')),
                ('location', models.CharField(help_text='The location of the Power Plant.', max_length=1000, verbose_name='Location')),
                ('production_capacity', models.FloatField(default=0, help_text='The production capacity of the Power Plant in MW(Mega Watt).', max_length=1000, verbose_name='Production Capacity')),
                ('power_category', models.PositiveIntegerField(choices=[(1, 'Hydro'), (2, 'Thermal'), (3, 'Other')], help_text='The category of the Power Plant .i.e. hydro or thermal', verbose_name='Category')),
                ('placement_priority', models.PositiveIntegerField(default=1, help_text='The order of the Power Plant placement for generation.', verbose_name='Placement Priority')),
                ('grouping', models.CharField(blank=True, editable=False, help_text='The group to which Power Plant belongs.', max_length=1000, null=True, verbose_name='Grouping')),
            ],
            options={
                'verbose_name_plural': 'Power Plants',
                'verbose_name': 'Power Plant',
            },
        ),
        migrations.AddField(
            model_name='hourlytotalpoweravailable',
            name='power_plant',
            field=models.ForeignKey(help_text="The related Power Plant's Total Availability at this time", on_delete=django.db.models.deletion.CASCADE, related_name='total_hourly_availabilities', to='generation.PowerPlant', verbose_name='Power Plant'),
        ),
        migrations.AddField(
            model_name='hourlyproductionforecast',
            name='power_plant',
            field=models.ForeignKey(help_text='The Power Production Plant', on_delete=django.db.models.deletion.CASCADE, related_name='hourly_forecasts', to='generation.PowerPlant', verbose_name='Power Plant'),
        ),
        migrations.AddField(
            model_name='generators',
            name='power_plant',
            field=models.ForeignKey(help_text="The related Power Plant's given generator's Availability at this time", on_delete=django.db.models.deletion.CASCADE, related_name='generators', to='generation.PowerPlant', verbose_name='Power Plant'),
        ),
        migrations.AddField(
            model_name='autonomyleft',
            name='power_plant',
            field=models.ForeignKey(help_text="The related Power Plant's Total Autonomy at this time", on_delete=django.db.models.deletion.CASCADE, related_name='power_autonomy', to='generation.PowerPlant', verbose_name='Power Plant'),
        ),
    ]
