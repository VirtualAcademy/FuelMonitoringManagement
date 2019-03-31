BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "django_site" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"name"	varchar(50) NOT NULL,
	"domain"	varchar(100) NOT NULL UNIQUE
);
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
CREATE TABLE IF NOT EXISTS "account_emailaddress" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"verified"	bool NOT NULL,
	"primary"	bool NOT NULL,
	"user_id"	integer NOT NULL,
	"email"	varchar(254) NOT NULL UNIQUE,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "account_emailconfirmation" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"created"	datetime NOT NULL,
	"sent"	datetime,
	"key"	varchar(64) NOT NULL UNIQUE,
	"email_address_id"	integer NOT NULL,
	FOREIGN KEY("email_address_id") REFERENCES "account_emailaddress"("id") DEFERRABLE INITIALLY DEFERRED
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
CREATE TABLE IF NOT EXISTS "django_session" (
	"session_key"	varchar(40) NOT NULL,
	"session_data"	text NOT NULL,
	"expire_date"	datetime NOT NULL,
	PRIMARY KEY("session_key")
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
CREATE TABLE IF NOT EXISTS "auth_user" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"password"	varchar(128) NOT NULL,
	"last_login"	datetime,
	"is_superuser"	bool NOT NULL,
	"username"	varchar(150) NOT NULL UNIQUE,
	"first_name"	varchar(30) NOT NULL,
	"email"	varchar(254) NOT NULL,
	"is_staff"	bool NOT NULL,
	"is_active"	bool NOT NULL,
	"date_joined"	datetime NOT NULL,
	"last_name"	varchar(150) NOT NULL
);
CREATE TABLE IF NOT EXISTS "auth_permission" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"content_type_id"	integer NOT NULL,
	"codename"	varchar(100) NOT NULL,
	"name"	varchar(255) NOT NULL,
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "django_content_type" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"app_label"	varchar(100) NOT NULL,
	"model"	varchar(100) NOT NULL
);
CREATE TABLE IF NOT EXISTS "django_admin_log" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"action_time"	datetime NOT NULL,
	"object_id"	text,
	"object_repr"	varchar(200) NOT NULL,
	"change_message"	text NOT NULL,
	"content_type_id"	integer,
	"user_id"	integer NOT NULL,
	"action_flag"	smallint unsigned NOT NULL,
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "auth_user_user_permissions" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"user_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "auth_user_groups" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"user_id"	integer NOT NULL,
	"group_id"	integer NOT NULL,
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "auth_group_permissions" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"group_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "auth_group" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"name"	varchar(80) NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS "django_migrations" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"app"	varchar(255) NOT NULL,
	"name"	varchar(255) NOT NULL,
	"applied"	datetime NOT NULL
);
INSERT INTO "django_site" VALUES (1,'example.com','example.com');
INSERT INTO "generation_powerplant" VALUES (5,'Edea','Songloulou',254.0,1,1,NULL);
INSERT INTO "generation_powerplant" VALUES (6,'Edea','Edea',552.0,1,3,NULL);
INSERT INTO "auth_user" VALUES (1,'pbkdf2_sha256$120000$Inwx6CtuO0Gw$8vHiGF0L+oQtPtq9S9LLzX5De95G85FZCbEKvi2cDqo=','2019-01-08 22:28:11.468525',1,'admin','','admin@site.check',1,1,'2019-01-08 21:49:55.265376','');
INSERT INTO "auth_permission" VALUES (1,1,'add_logentry','Can add log entry');
INSERT INTO "auth_permission" VALUES (2,1,'change_logentry','Can change log entry');
INSERT INTO "auth_permission" VALUES (3,1,'delete_logentry','Can delete log entry');
INSERT INTO "auth_permission" VALUES (4,1,'view_logentry','Can view log entry');
INSERT INTO "auth_permission" VALUES (5,2,'add_group','Can add group');
INSERT INTO "auth_permission" VALUES (6,2,'change_group','Can change group');
INSERT INTO "auth_permission" VALUES (7,2,'delete_group','Can delete group');
INSERT INTO "auth_permission" VALUES (8,2,'view_group','Can view group');
INSERT INTO "auth_permission" VALUES (9,3,'add_user','Can add user');
INSERT INTO "auth_permission" VALUES (10,3,'change_user','Can change user');
INSERT INTO "auth_permission" VALUES (11,3,'delete_user','Can delete user');
INSERT INTO "auth_permission" VALUES (12,3,'view_user','Can view user');
INSERT INTO "auth_permission" VALUES (13,4,'add_permission','Can add permission');
INSERT INTO "auth_permission" VALUES (14,4,'change_permission','Can change permission');
INSERT INTO "auth_permission" VALUES (15,4,'delete_permission','Can delete permission');
INSERT INTO "auth_permission" VALUES (16,4,'view_permission','Can view permission');
INSERT INTO "auth_permission" VALUES (17,5,'add_contenttype','Can add content type');
INSERT INTO "auth_permission" VALUES (18,5,'change_contenttype','Can change content type');
INSERT INTO "auth_permission" VALUES (19,5,'delete_contenttype','Can delete content type');
INSERT INTO "auth_permission" VALUES (20,5,'view_contenttype','Can view content type');
INSERT INTO "auth_permission" VALUES (21,6,'add_session','Can add session');
INSERT INTO "auth_permission" VALUES (22,6,'change_session','Can change session');
INSERT INTO "auth_permission" VALUES (23,6,'delete_session','Can delete session');
INSERT INTO "auth_permission" VALUES (24,6,'view_session','Can view session');
INSERT INTO "auth_permission" VALUES (25,7,'add_powerplant','Can add Power Plant');
INSERT INTO "auth_permission" VALUES (26,7,'change_powerplant','Can change Power Plant');
INSERT INTO "auth_permission" VALUES (27,7,'delete_powerplant','Can delete Power Plant');
INSERT INTO "auth_permission" VALUES (28,7,'view_powerplant','Can view Power Plant');
INSERT INTO "auth_permission" VALUES (29,8,'add_demand','Can add Consumer');
INSERT INTO "auth_permission" VALUES (30,8,'change_demand','Can change Consumer');
INSERT INTO "auth_permission" VALUES (31,8,'delete_demand','Can delete Consumer');
INSERT INTO "auth_permission" VALUES (32,8,'view_demand','Can view Consumer');
INSERT INTO "auth_permission" VALUES (33,9,'add_hourlytotalpoweravailable','Can add Total Hourly Available');
INSERT INTO "auth_permission" VALUES (34,9,'change_hourlytotalpoweravailable','Can change Total Hourly Available');
INSERT INTO "auth_permission" VALUES (35,9,'delete_hourlytotalpoweravailable','Can delete Total Hourly Available');
INSERT INTO "auth_permission" VALUES (36,9,'view_hourlytotalpoweravailable','Can view Total Hourly Available');
INSERT INTO "auth_permission" VALUES (37,10,'add_autonomyleft','Can add Autonomy');
INSERT INTO "auth_permission" VALUES (38,10,'change_autonomyleft','Can change Autonomy');
INSERT INTO "auth_permission" VALUES (39,10,'delete_autonomyleft','Can delete Autonomy');
INSERT INTO "auth_permission" VALUES (40,10,'view_autonomyleft','Can view Autonomy');
INSERT INTO "auth_permission" VALUES (41,11,'add_generators','Can add Power Plant Generator');
INSERT INTO "auth_permission" VALUES (42,11,'change_generators','Can change Power Plant Generator');
INSERT INTO "auth_permission" VALUES (43,11,'delete_generators','Can delete Power Plant Generator');
INSERT INTO "auth_permission" VALUES (44,11,'view_generators','Can view Power Plant Generator');
INSERT INTO "auth_permission" VALUES (45,12,'add_hourlyproductionforecast','Can add Hourly Forecast');
INSERT INTO "auth_permission" VALUES (46,12,'change_hourlyproductionforecast','Can change Hourly Forecast');
INSERT INTO "auth_permission" VALUES (47,12,'delete_hourlyproductionforecast','Can delete Hourly Forecast');
INSERT INTO "auth_permission" VALUES (48,12,'view_hourlyproductionforecast','Can view Hourly Forecast');
INSERT INTO "auth_permission" VALUES (49,13,'add_specificconsumption','Can add Specific Consumption');
INSERT INTO "auth_permission" VALUES (50,13,'change_specificconsumption','Can change Specific Consumption');
INSERT INTO "auth_permission" VALUES (51,13,'delete_specificconsumption','Can delete Specific Consumption');
INSERT INTO "auth_permission" VALUES (52,13,'view_specificconsumption','Can view Specific Consumption');
INSERT INTO "auth_permission" VALUES (53,14,'add_supplier','Can add Supplier');
INSERT INTO "auth_permission" VALUES (54,14,'change_supplier','Can change Supplier');
INSERT INTO "auth_permission" VALUES (55,14,'delete_supplier','Can delete Supplier');
INSERT INTO "auth_permission" VALUES (56,14,'view_supplier','Can view Supplier');
INSERT INTO "auth_permission" VALUES (57,15,'add_consumption','Can add consumption');
INSERT INTO "auth_permission" VALUES (58,15,'change_consumption','Can change consumption');
INSERT INTO "auth_permission" VALUES (59,15,'delete_consumption','Can delete consumption');
INSERT INTO "auth_permission" VALUES (60,15,'view_consumption','Can view consumption');
INSERT INTO "auth_permission" VALUES (61,16,'add_supplyscheduletransaction','Can add Delivery Schedule');
INSERT INTO "auth_permission" VALUES (62,16,'change_supplyscheduletransaction','Can change Delivery Schedule');
INSERT INTO "auth_permission" VALUES (63,16,'delete_supplyscheduletransaction','Can delete Delivery Schedule');
INSERT INTO "auth_permission" VALUES (64,16,'view_supplyscheduletransaction','Can view Delivery Schedule');
INSERT INTO "auth_permission" VALUES (65,17,'add_inventory','Can add Inventory');
INSERT INTO "auth_permission" VALUES (66,17,'change_inventory','Can change Inventory');
INSERT INTO "auth_permission" VALUES (67,17,'delete_inventory','Can delete Inventory');
INSERT INTO "auth_permission" VALUES (68,17,'view_inventory','Can view Inventory');
INSERT INTO "auth_permission" VALUES (69,18,'add_dailyproductiononfuel','Can add Production Realisation');
INSERT INTO "auth_permission" VALUES (70,18,'change_dailyproductiononfuel','Can change Production Realisation');
INSERT INTO "auth_permission" VALUES (71,18,'delete_dailyproductiononfuel','Can delete Production Realisation');
INSERT INTO "auth_permission" VALUES (72,18,'view_dailyproductiononfuel','Can view Production Realisation');
INSERT INTO "auth_permission" VALUES (73,19,'add_storageunit','Can add Storage Unit');
INSERT INTO "auth_permission" VALUES (74,19,'change_storageunit','Can change Storage Unit');
INSERT INTO "auth_permission" VALUES (75,19,'delete_storageunit','Can delete Storage Unit');
INSERT INTO "auth_permission" VALUES (76,19,'view_storageunit','Can view Storage Unit');
INSERT INTO "auth_permission" VALUES (77,20,'add_deliveryorder','Can add Delivery Order');
INSERT INTO "auth_permission" VALUES (78,20,'change_deliveryorder','Can change Delivery Order');
INSERT INTO "auth_permission" VALUES (79,20,'delete_deliveryorder','Can delete Delivery Order');
INSERT INTO "auth_permission" VALUES (80,20,'view_deliveryorder','Can view Delivery Order');
INSERT INTO "auth_permission" VALUES (81,21,'add_fuel','Can add Fuel');
INSERT INTO "auth_permission" VALUES (82,21,'change_fuel','Can change Fuel');
INSERT INTO "auth_permission" VALUES (83,21,'delete_fuel','Can delete Fuel');
INSERT INTO "auth_permission" VALUES (84,21,'view_fuel','Can view Fuel');
INSERT INTO "auth_permission" VALUES (85,22,'add_supply','Can add Supply');
INSERT INTO "auth_permission" VALUES (86,22,'change_supply','Can change Supply');
INSERT INTO "auth_permission" VALUES (87,22,'delete_supply','Can delete Supply');
INSERT INTO "auth_permission" VALUES (88,22,'view_supply','Can view Supply');
INSERT INTO "auth_permission" VALUES (89,23,'add_stockvariation','Can add Inventory Variation');
INSERT INTO "auth_permission" VALUES (90,23,'change_stockvariation','Can change Inventory Variation');
INSERT INTO "auth_permission" VALUES (91,23,'delete_stockvariation','Can delete Inventory Variation');
INSERT INTO "auth_permission" VALUES (92,23,'view_stockvariation','Can view Inventory Variation');
INSERT INTO "auth_permission" VALUES (93,24,'add_site','Can add site');
INSERT INTO "auth_permission" VALUES (94,24,'change_site','Can change site');
INSERT INTO "auth_permission" VALUES (95,24,'delete_site','Can delete site');
INSERT INTO "auth_permission" VALUES (96,24,'view_site','Can view site');
INSERT INTO "auth_permission" VALUES (97,25,'add_socialapp','Can add social application');
INSERT INTO "auth_permission" VALUES (98,25,'change_socialapp','Can change social application');
INSERT INTO "auth_permission" VALUES (99,25,'delete_socialapp','Can delete social application');
INSERT INTO "auth_permission" VALUES (100,25,'view_socialapp','Can view social application');
INSERT INTO "auth_permission" VALUES (101,26,'add_socialaccount','Can add social account');
INSERT INTO "auth_permission" VALUES (102,26,'change_socialaccount','Can change social account');
INSERT INTO "auth_permission" VALUES (103,26,'delete_socialaccount','Can delete social account');
INSERT INTO "auth_permission" VALUES (104,26,'view_socialaccount','Can view social account');
INSERT INTO "auth_permission" VALUES (105,27,'add_socialtoken','Can add social application token');
INSERT INTO "auth_permission" VALUES (106,27,'change_socialtoken','Can change social application token');
INSERT INTO "auth_permission" VALUES (107,27,'delete_socialtoken','Can delete social application token');
INSERT INTO "auth_permission" VALUES (108,27,'view_socialtoken','Can view social application token');
INSERT INTO "auth_permission" VALUES (109,28,'add_emailconfirmation','Can add email confirmation');
INSERT INTO "auth_permission" VALUES (110,28,'change_emailconfirmation','Can change email confirmation');
INSERT INTO "auth_permission" VALUES (111,28,'delete_emailconfirmation','Can delete email confirmation');
INSERT INTO "auth_permission" VALUES (112,28,'view_emailconfirmation','Can view email confirmation');
INSERT INTO "auth_permission" VALUES (113,29,'add_emailaddress','Can add email address');
INSERT INTO "auth_permission" VALUES (114,29,'change_emailaddress','Can change email address');
INSERT INTO "auth_permission" VALUES (115,29,'delete_emailaddress','Can delete email address');
INSERT INTO "auth_permission" VALUES (116,29,'view_emailaddress','Can view email address');
INSERT INTO "django_content_type" VALUES (1,'admin','logentry');
INSERT INTO "django_content_type" VALUES (2,'auth','group');
INSERT INTO "django_content_type" VALUES (3,'auth','user');
INSERT INTO "django_content_type" VALUES (4,'auth','permission');
INSERT INTO "django_content_type" VALUES (5,'contenttypes','contenttype');
INSERT INTO "django_content_type" VALUES (6,'sessions','session');
INSERT INTO "django_content_type" VALUES (7,'generation','powerplant');
INSERT INTO "django_content_type" VALUES (8,'generation','demand');
INSERT INTO "django_content_type" VALUES (9,'generation','hourlytotalpoweravailable');
INSERT INTO "django_content_type" VALUES (10,'generation','autonomyleft');
INSERT INTO "django_content_type" VALUES (11,'generation','generators');
INSERT INTO "django_content_type" VALUES (12,'generation','hourlyproductionforecast');
INSERT INTO "django_content_type" VALUES (13,'fuel','specificconsumption');
INSERT INTO "django_content_type" VALUES (14,'fuel','supplier');
INSERT INTO "django_content_type" VALUES (15,'fuel','consumption');
INSERT INTO "django_content_type" VALUES (16,'fuel','supplyscheduletransaction');
INSERT INTO "django_content_type" VALUES (17,'fuel','inventory');
INSERT INTO "django_content_type" VALUES (18,'fuel','dailyproductiononfuel');
INSERT INTO "django_content_type" VALUES (19,'fuel','storageunit');
INSERT INTO "django_content_type" VALUES (20,'fuel','deliveryorder');
INSERT INTO "django_content_type" VALUES (21,'fuel','fuel');
INSERT INTO "django_content_type" VALUES (22,'fuel','supply');
INSERT INTO "django_content_type" VALUES (23,'fuel','stockvariation');
INSERT INTO "django_content_type" VALUES (24,'sites','site');
INSERT INTO "django_content_type" VALUES (25,'allauth','socialapp');
INSERT INTO "django_content_type" VALUES (26,'allauth','socialaccount');
INSERT INTO "django_content_type" VALUES (27,'allauth','socialtoken');
INSERT INTO "django_content_type" VALUES (28,'account','emailconfirmation');
INSERT INTO "django_content_type" VALUES (29,'account','emailaddress');
INSERT INTO "django_migrations" VALUES (1,'contenttypes','0001_initial','2019-01-06 20:57:11.559411');
INSERT INTO "django_migrations" VALUES (2,'auth','0001_initial','2019-01-06 20:57:11.600302');
INSERT INTO "django_migrations" VALUES (3,'admin','0001_initial','2019-01-06 20:57:11.627231');
INSERT INTO "django_migrations" VALUES (4,'admin','0002_logentry_remove_auto_add','2019-01-06 20:57:11.651167');
INSERT INTO "django_migrations" VALUES (5,'admin','0003_logentry_add_action_flag_choices','2019-01-06 20:57:11.672170');
INSERT INTO "django_migrations" VALUES (6,'contenttypes','0002_remove_content_type_name','2019-01-06 20:57:11.713061');
INSERT INTO "django_migrations" VALUES (7,'auth','0002_alter_permission_name_max_length','2019-01-06 20:57:11.731014');
INSERT INTO "django_migrations" VALUES (8,'auth','0003_alter_user_email_max_length','2019-01-06 20:57:11.751958');
INSERT INTO "django_migrations" VALUES (9,'auth','0004_alter_user_username_opts','2019-01-06 20:57:11.777963');
INSERT INTO "django_migrations" VALUES (10,'auth','0005_alter_user_last_login_null','2019-01-06 20:57:11.799905');
INSERT INTO "django_migrations" VALUES (11,'auth','0006_require_contenttypes_0002','2019-01-06 20:57:11.804889');
INSERT INTO "django_migrations" VALUES (12,'auth','0007_alter_validators_add_error_messages','2019-01-06 20:57:11.827831');
INSERT INTO "django_migrations" VALUES (13,'auth','0008_alter_user_username_max_length','2019-01-06 20:57:11.849772');
INSERT INTO "django_migrations" VALUES (14,'auth','0009_alter_user_last_name_max_length','2019-01-06 20:57:11.869717');
INSERT INTO "django_migrations" VALUES (15,'generation','0001_initial','2019-01-06 20:57:11.882719');
INSERT INTO "django_migrations" VALUES (16,'sessions','0001_initial','2019-01-06 20:57:11.895726');
INSERT INTO "django_migrations" VALUES (17,'generation','0002_autonomyleft_demand_generators_hourlyproductionforecast_hourlytotalpoweravailable','2019-01-07 20:57:29.266109');
INSERT INTO "django_migrations" VALUES (18,'fuel','0001_initial','2019-01-09 10:54:36.029310');
INSERT INTO "django_migrations" VALUES (19,'account','0001_initial','2019-02-05 17:08:11.558700');
INSERT INTO "django_migrations" VALUES (20,'account','0002_email_max_length','2019-02-05 17:08:11.593607');
INSERT INTO "django_migrations" VALUES (21,'fuel','0002_auto_20190120_0913','2019-02-05 17:08:11.661425');
INSERT INTO "django_migrations" VALUES (22,'sites','0001_initial','2019-02-05 17:08:11.677383');
INSERT INTO "django_migrations" VALUES (23,'sites','0002_alter_domain_unique','2019-02-05 17:08:11.697330');
CREATE INDEX IF NOT EXISTS "fuel_supplyscheduletransaction_delivery_order_id_74e1a2b3" ON "fuel_supplyscheduletransaction" (
	"delivery_order_id"
);
CREATE INDEX IF NOT EXISTS "account_emailaddress_user_id_2c513194" ON "account_emailaddress" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "account_emailconfirmation_email_address_id_5b7f8c58" ON "account_emailconfirmation" (
	"email_address_id"
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
CREATE INDEX IF NOT EXISTS "django_session_expire_date_a5c62663" ON "django_session" (
	"expire_date"
);
CREATE INDEX IF NOT EXISTS "auth_permission_content_type_id_2f476e4b" ON "auth_permission" (
	"content_type_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" (
	"content_type_id",
	"codename"
);
CREATE UNIQUE INDEX IF NOT EXISTS "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" (
	"app_label",
	"model"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_user_id_c564eba6" ON "django_admin_log" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" (
	"content_type_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_user_permissions_permission_id_1fbb5f2c" ON "auth_user_user_permissions" (
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_user_permissions_user_id_a95ead1b" ON "auth_user_user_permissions" (
	"user_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" ON "auth_user_user_permissions" (
	"user_id",
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_groups_group_id_97559544" ON "auth_user_groups" (
	"group_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_groups_user_id_6a12ed8b" ON "auth_user_groups" (
	"user_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_user_groups_user_id_group_id_94350c0c_uniq" ON "auth_user_groups" (
	"user_id",
	"group_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" (
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" (
	"group_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" (
	"group_id",
	"permission_id"
);
COMMIT;
