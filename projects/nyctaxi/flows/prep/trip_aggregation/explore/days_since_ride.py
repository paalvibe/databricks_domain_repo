# Databricks notebook source
import datetime

from pyspark.sql import functions as F

# COMMAND ----------

taxi_data_df = table("paal_taxidata.taxi_2019_12")

# COMMAND ----------

taxi_data_df.display()

# COMMAND ----------

w_pu_dt_df = taxi_data_df.withColumn('pickup_date', F.to_date('Pickup_DateTime'))
w_pu_dt_df.select('Pickup_DateTime', 'pickup_date').display()

# COMMAND ----------

# COMMAND ----------

# Enable importing libs in an orderly manner
from projects.nyctaxi.libs.projpath import add_project_dir_to_syspath
add_project_dir_to_syspath()


# COMMAND ----------

from srclibs.age import gen_age
from datetime import date

# COMMAND ----------

w_trip_age = gen_age(df=w_pu_dt_df, today=date(2022, 12, 10), datecol="pickup_date")
w_trip_age.select('Pickup_DateTime', 'pickup_date', 'age').display()

# COMMAND ----------


