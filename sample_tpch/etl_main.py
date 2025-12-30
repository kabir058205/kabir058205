# Databricks notebook source
from pyspark.sql.functions import current_date, lit
import uuid
from datetime import date

def log_error(run_id, error_message):
    log_df = spark.createDataFrame(
        [(run_id, "ERROR", error_message, date.today())],
        ["run_id", "status", "message", "log_date"]
    )
    log_df.write.mode("append").saveAsTable("workspace.default.etl_run_log")

run_id = str(uuid.uuid4())

try:
    # Read tables
    df_customer = spark.table("workspace.default.customer_csv")
    df_orders = spark.table("workspace.default.orders_csv")

    # Add load_date and run_id columns
    df_customer_trans = (
        df_customer
        .withColumn("load_date", current_date())
        .withColumn("run_id", lit(run_id))
    )
    df_orders_trans = (
        df_orders
        .withColumn("load_date", current_date())
        .withColumn("run_id", lit(run_id))
    )

    # Write transformation tables
    df_customer_trans.write.mode("overwrite").saveAsTable("workspace.default.customer_transformation")
    df_orders_trans.write.mode("overwrite").saveAsTable("workspace.default.orders_transformation")

    # Log success to etl_run_log table
    log_df = spark.createDataFrame(
        [(run_id, "SUCCESS", "ETL run completed successfully.", date.today())],
        ["run_id", "status", "message", "log_date"]
    )
    log_df.write.mode("append").saveAsTable("workspace.default.etl_run_log")

except Exception as e:
    log_error(run_id, str(e))
