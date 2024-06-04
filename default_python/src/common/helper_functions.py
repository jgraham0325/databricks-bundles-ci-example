import os

class HelperFunctions:

    @staticmethod
    def get_schema_json_path(table_name: str, layer: str) -> str:

        if not table_name:
            raise ValueError("The 'table_name' argument is required but was not provided.")
        if not layer:
            raise ValueError("The 'layer' argument is required but was not provided.")
        
        # Get the parent directory of this helper_functions.py file. Works locally and in Databricks.
        parent_directory = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        
        # Construct the path to the schema json file
        return os.path.normpath(os.path.join(parent_directory, f"./resources/schemas/patents/{layer}/{table_name}.json"))