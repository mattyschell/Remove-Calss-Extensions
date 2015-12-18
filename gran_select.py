# Import arcpy module
import arcpy

CSCLCONNECTION = "Database Connections\\_dev_10.2_cscl@csclcdev.doitt.nycnet.sde"
arcpy.env.workspace = CSCLCONNECTION


# Tables
tables = arcpy.ListTables()
for table in tables:
	# Process: Change Privileges
	arcpy.ChangePrivileges_management(table, "CSCL_READ_ONLY", "GRANT", "AS_IS")

# Feature Classes
featureclasses = arcpy.ListFeatureClasses()
for fc in featureclasses:
	# Process: Change Privileges
	arcpy.ChangePrivileges_management(fc, "CSCL_READ_ONLY", "GRANT", "AS_IS")
	
# for fc in featureclasses:
	# print (fc)


# Feature Datasets
datasets = arcpy.ListDatasets("CSCL.*", "Feature")
for dataset in datasets:
    # Process: Change Privileges
	arcpy.ChangePrivileges_management(dataset, "CSCL_READ_ONLY", "GRANT", "AS_IS")
	
# for dataset in datasets:
    # print(dataset)
