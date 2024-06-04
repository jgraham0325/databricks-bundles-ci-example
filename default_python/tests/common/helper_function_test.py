import os
import pytest
from common.helper_functions import HelperFunctions


def test_get_schema_json_path():
    # Test with valid inputs
    table_name = "patent_docdb_raw"
    layer = "bronze"
    actual_path = HelperFunctions.get_schema_json_path(table_name, layer)
    print(f"actual_path: {actual_path}")
    assert actual_path.endswith("resources/schemas/patents/bronze/patent_docdb_raw.json")

    # Test with missing table_name
    with pytest.raises(ValueError):
        HelperFunctions.get_schema_json_path(None, layer)

    # Test with missing layer
    with pytest.raises(ValueError):
        HelperFunctions.get_schema_json_path(table_name, None)