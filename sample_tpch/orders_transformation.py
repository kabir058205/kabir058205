# Databricks notebook source
from pyspark.sql.functions import current_date, lit

def transform_orders(run_id):
    df_orders = spark.table("workspace.default.orders_csv")
    df_orders_trans = (
        df_orders
        .withColumn("load_date", current_date())
        .withColumn("run_id", lit(run_id))
    )
    df_orders_trans.write.mode("overwrite").saveAsTable("workspace.default.orders_transformation")
