import sys
import os

from pyspark.sql import SparkSession, DataFrame
from common.helper_functions import HelperFunctions

def get_taxis(spark: SparkSession) -> DataFrame:
  return spark.read.table("samples.nyctaxi.trips")


# Create a new Databricks Connect session. If this fails,
# check that you have configured Databricks Connect correctly.
# See https://docs.databricks.com/dev-tools/databricks-connect.html.
def get_spark() -> SparkSession:
  try:
    from databricks.connect import DatabricksSession
    return DatabricksSession.builder.getOrCreate()
  except ImportError:
    return SparkSession.builder.getOrCreate()

def main():
  # Simple demo of how to read a schema file
  print_json_schema_to_console("patent_docdb_raw", "bronze")
  
  
def print_json_schema_to_console(table_name: str, layer: str) -> None:
  helper = HelperFunctions()
  path = helper.get_schema_json_path(table_name, layer)
    
  with open(path, 'r') as file:
    content = file.read()
  print(f"file content for {path}: {content}")

if __name__ == '__main__':
  main()
