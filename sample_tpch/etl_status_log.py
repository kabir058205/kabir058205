# Databricks notebook source
from datetime import date

def log_status(run_id, status, message):
    log_df = spark.createDataFrame(
        [(run_id, status, message, date.today())],
        ["run_id", "status", "message", "log_date"]
    )
    log_df.write.mode("append").saveAsTable("workspace.default.etl_run_log")
