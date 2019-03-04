BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "fuel_supplyscheduletransaction" (
	"date_created"	datetime NOT NULL,
	"date_modified"	datetime NOT NULL,
	"transaction_date"	date NOT NULL,
	"memo"	text NOT NULL,
	"eta"	date NOT NULL,
	"delivery_order_id"	integer NOT NULL,
	"transaction_no"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	FOREIGN KEY("delivery_order_id") REFERENCES "fuel_deliveryorder"("delievery_order") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "fuel_consumption" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"date_created"	datetime NOT NULL,
	"date_modified"	datetime NOT NULL,
	"quantity_consumed"	real NOT NULL,
	"measurement"	varchar(256) NOT NULL,
	"date_recorded"	date NOT NULL,
	"storage_area_id"	integer NOT NULL,
	FOREIGN KEY("storage_area_id") REFERENCES "fuel_storageunit"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "fuel_dailyproductiononfuel" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"date_created"	datetime NOT NULL,
	"date_modified"	datetime NOT NULL,
	"power_units"	real NOT NULL,
	"unit_measurement"	varchar(256) NOT NULL,
	"date_recorded"	date NOT NULL,
	"storage_area_id"	integer NOT NULL,
	FOREIGN KEY("storage_area_id") REFERENCES "fuel_storageunit"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "fuel_deliveryorder" (
	"date_created"	datetime NOT NULL,
	"date_modified"	datetime NOT NULL,
	"delievery_order"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"po_date"	date NOT NULL,
	"po_description"	text NOT NULL,
	"delivery_status"	integer unsigned NOT NULL,
	"eta"	date NOT NULL,
	"order_qty"	real NOT NULL,
	"created_by_id"	integer NOT NULL,
	"delievery_item_id"	integer NOT NULL,
	"modified_by_id"	integer NOT NULL,
	FOREIGN KEY("created_by_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("modified_by_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("delievery_item_id") REFERENCES "fuel_fuel"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "fuel_inventory" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"date_created"	datetime NOT NULL,
	"date_modified"	datetime NOT NULL,
	"record_date"	datetime NOT NULL,
	"quantity"	real NOT NULL,
	"measurement"	varchar(256) NOT NULL,
	"storage_unit_id"	integer NOT NULL,
	FOREIGN KEY("storage_unit_id") REFERENCES "fuel_storageunit"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "fuel_specificconsumption" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"specific_consumptions"	real NOT NULL,
	"date_recorded"	date NOT NULL,
	"storage_area_id"	integer NOT NULL,
	FOREIGN KEY("storage_area_id") REFERENCES "fuel_storageunit"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "fuel_stockvariation" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"date_created"	datetime NOT NULL,
	"date_modified"	datetime NOT NULL,
	"record_date"	datetime NOT NULL,
	"initial_qty"	real NOT NULL,
	"qty_left"	real NOT NULL,
	"minimum_qty"	real NOT NULL,
	"measurement"	varchar(256) NOT NULL,
	"qty_added_id"	integer NOT NULL,
	"qty_removed_id"	integer NOT NULL,
	"storage_unit_id"	integer NOT NULL,
	FOREIGN KEY("qty_removed_id") REFERENCES "fuel_consumption"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("qty_added_id") REFERENCES "fuel_supply"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("storage_unit_id") REFERENCES "fuel_storageunit"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "fuel_supply" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"date_created"	datetime NOT NULL,
	"date_modified"	datetime NOT NULL,
	"quantity_supplied"	real NOT NULL,
	"measurement"	varchar(256) NOT NULL,
	"date_recorded"	date NOT NULL,
	"destined_to_id"	integer NOT NULL,
	"supplier_id"	integer NOT NULL,
	FOREIGN KEY("supplier_id") REFERENCES "fuel_supplier"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("destined_to_id") REFERENCES "fuel_storageunit"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "fuel_supplier" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"date_created"	datetime NOT NULL,
	"date_modified"	datetime NOT NULL,
	"supplier_name"	varchar(256) NOT NULL
);
CREATE TABLE IF NOT EXISTS "fuel_storageunit" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"unit_name"	varchar(256) NOT NULL,
	"storage_capacity"	real NOT NULL,
	"measurement"	varchar(256) NOT NULL,
	"facility_location"	varchar(256) NOT NULL,
	"fuel_id"	integer NOT NULL,
	FOREIGN KEY("fuel_id") REFERENCES "fuel_fuel"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "fuel_fuel" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"fuel_name"	varchar(1000) NOT NULL,
	"fuel_discription"	text,
	"fuel_category"	integer unsigned NOT NULL
);
CREATE TABLE IF NOT EXISTS "generation_hourlytotalpoweravailable" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"date_created"	datetime NOT NULL,
	"date_modified"	datetime NOT NULL,
	"power_units_available"	real NOT NULL,
	"production_capacity"	real NOT NULL,
	"unit_measurement"	varchar(256) NOT NULL,
	"date_recorded"	date NOT NULL,
	"time_recorded"	time NOT NULL,
	"power_plant_id"	integer NOT NULL,
	FOREIGN KEY("power_plant_id") REFERENCES "generation_powerplant"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "generation_hourlyproductionforecast" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"date_created"	datetime NOT NULL,
	"date_modified"	datetime NOT NULL,
	"power_units"	real NOT NULL,
	"unit_measurement"	varchar(256) NOT NULL,
	"date_recorded"	date NOT NULL,
	"time_recorded"	time NOT NULL,
	"power_plant_id"	integer NOT NULL,
	FOREIGN KEY("power_plant_id") REFERENCES "generation_powerplant"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "generation_generators" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"date_created"	datetime NOT NULL,
	"date_modified"	datetime NOT NULL,
	"gen_number"	integer unsigned NOT NULL,
	"power_units"	real NOT NULL,
	"unit_measurement"	varchar(256) NOT NULL,
	"date_recorded"	date NOT NULL,
	"time_recorded"	time NOT NULL,
	"power_plant_id"	integer NOT NULL,
	FOREIGN KEY("power_plant_id") REFERENCES "generation_powerplant"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "generation_demand" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"date_created"	datetime NOT NULL,
	"date_modified"	datetime NOT NULL,
	"power_consumer"	varchar(256) NOT NULL,
	"power_units"	real NOT NULL,
	"unit_measurement"	varchar(256) NOT NULL,
	"date_recorded"	date NOT NULL,
	"time_recorded"	time NOT NULL
);
CREATE TABLE IF NOT EXISTS "generation_autonomyleft" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"date_created"	datetime NOT NULL,
	"date_modified"	datetime NOT NULL,
	"power_autonomy"	real NOT NULL,
	"unit_measurement"	varchar(256) NOT NULL,
	"date_recorded"	date NOT NULL,
	"time_recorded"	time NOT NULL,
	"power_plant_id"	integer NOT NULL,
	FOREIGN KEY("power_plant_id") REFERENCES "generation_powerplant"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "generation_powerplant" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"plant_name"	varchar(1000) NOT NULL,
	"location"	varchar(1000) NOT NULL,
	"production_capacity"	real NOT NULL,
	"power_category"	integer unsigned NOT NULL,
	"placement_priority"	integer unsigned NOT NULL,
	"grouping"	varchar(1000)
);
INSERT INTO "generation_powerplant" VALUES (5,'Edea','Songloulou',254.0,1,1,NULL);
INSERT INTO "generation_powerplant" VALUES (6,'Edea','Edea',552.0,1,3,NULL);
CREATE INDEX IF NOT EXISTS "fuel_supplyscheduletransaction_delivery_order_id_74e1a2b3" ON "fuel_supplyscheduletransaction" (
	"delivery_order_id"
);
CREATE INDEX IF NOT EXISTS "fuel_consumption_storage_area_id_dc5cb0ad" ON "fuel_consumption" (
	"storage_area_id"
);
CREATE INDEX IF NOT EXISTS "fuel_dailyproductiononfuel_storage_area_id_ca4d6001" ON "fuel_dailyproductiononfuel" (
	"storage_area_id"
);
CREATE INDEX IF NOT EXISTS "fuel_deliveryorder_modified_by_id_1271b9d0" ON "fuel_deliveryorder" (
	"modified_by_id"
);
CREATE INDEX IF NOT EXISTS "fuel_deliveryorder_delievery_item_id_01e02619" ON "fuel_deliveryorder" (
	"delievery_item_id"
);
CREATE INDEX IF NOT EXISTS "fuel_deliveryorder_created_by_id_83cdcbbe" ON "fuel_deliveryorder" (
	"created_by_id"
);
CREATE INDEX IF NOT EXISTS "fuel_inventory_storage_unit_id_cafcb38d" ON "fuel_inventory" (
	"storage_unit_id"
);
CREATE INDEX IF NOT EXISTS "fuel_specificconsumption_storage_area_id_3665c4a7" ON "fuel_specificconsumption" (
	"storage_area_id"
);
CREATE INDEX IF NOT EXISTS "fuel_stockvariation_storage_unit_id_b53fc9d5" ON "fuel_stockvariation" (
	"storage_unit_id"
);
CREATE INDEX IF NOT EXISTS "fuel_stockvariation_qty_removed_id_47d36b4e" ON "fuel_stockvariation" (
	"qty_removed_id"
);
CREATE INDEX IF NOT EXISTS "fuel_stockvariation_qty_added_id_75281c4a" ON "fuel_stockvariation" (
	"qty_added_id"
);
CREATE INDEX IF NOT EXISTS "fuel_supply_supplier_id_6d28ba24" ON "fuel_supply" (
	"supplier_id"
);
CREATE INDEX IF NOT EXISTS "fuel_supply_destined_to_id_b6f15b7c" ON "fuel_supply" (
	"destined_to_id"
);
CREATE INDEX IF NOT EXISTS "fuel_storageunit_fuel_id_f2028919" ON "fuel_storageunit" (
	"fuel_id"
);
CREATE INDEX IF NOT EXISTS "generation_hourlytotalpoweravailable_power_plant_id_7bc80f80" ON "generation_hourlytotalpoweravailable" (
	"power_plant_id"
);
CREATE INDEX IF NOT EXISTS "generation_hourlyproductionforecast_power_plant_id_84897d6f" ON "generation_hourlyproductionforecast" (
	"power_plant_id"
);
CREATE INDEX IF NOT EXISTS "generation_generators_power_plant_id_a4e07337" ON "generation_generators" (
	"power_plant_id"
);
CREATE INDEX IF NOT EXISTS "generation_autonomyleft_power_plant_id_154a7d33" ON "generation_autonomyleft" (
	"power_plant_id"
);
COMMIT;
