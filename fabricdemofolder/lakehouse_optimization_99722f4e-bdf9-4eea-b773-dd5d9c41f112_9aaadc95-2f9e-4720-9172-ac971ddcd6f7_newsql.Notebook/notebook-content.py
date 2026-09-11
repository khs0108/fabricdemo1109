# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "9aaadc95-2f9e-4720-9172-ac971ddcd6f7",
# META       "default_lakehouse_name": "workspacelakeh1",
# META       "default_lakehouse_workspace_id": "99722f4e-bdf9-4eea-b773-dd5d9c41f112",
# META       "known_lakehouses": [
# META         {
# META           "id": "9aaadc95-2f9e-4720-9172-ac971ddcd6f7",
# META           "name": "workspacelakeh1"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Run the below script or schedule it to run regularly to optimize your Lakehouse table 'newsql'

from delta.tables import *
deltaTable = DeltaTable.forName(spark, "newsql")
deltaTable.optimize().executeCompaction()

# If you only want to optimize a subset of your data, you can specify an optional partition predicate. For example:
#
#     from datetime import datetime, timedelta
#     startDate = (datetime.now() - timedelta(days=3)).strftime('%Y-%m-%d')
#     deltaTable.optimize().where("date > '{}'".format(startDate)).executeCompaction()


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
