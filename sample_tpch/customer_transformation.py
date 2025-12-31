# Databricks notebook source
from pyspark.sql.functions import current_date, lit

def transform_customer(run_id):
    df_customer = spark.table("workspace.default.customer_csv")
    df_customer_trans = (
        df_customer
        .withColumn("load_date", current_date())
        .withColumn("run_id", lit(run_id))
    )
    df_customer_trans.write.mode("overwrite").saveAsTable("workspace.default.customer_transformation")
    return df_customer_trans
