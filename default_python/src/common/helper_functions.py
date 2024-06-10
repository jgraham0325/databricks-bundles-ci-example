import os

class HelperFunctions:

    @staticmethod
    def get_schema_json_path(table_name: str, layer: str) -> str:
        
        # Get the parent directory of this helper_functions.py file. Works locally and in Databricks.
        parent_directory = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        
        # Construct the path to the schema json file
        return os.path.normpath(os.path.join(parent_directory, f"./resources/schemas/patents/{layer}/{table_name}.json"))