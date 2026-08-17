from pathlib import Path
from weekly_01.loader import load_manifest
from weekly_01.models import RestockItem
import pytest
from pydantic import ValidationError
from weekly_01.exceptions import ManifestFileNotFoundError

@pytest.fixture
def manifest_path():
    return Path(__file__).parent.parent / "data/restock_manifest.json"

def test_valid_row():
    row = { "sku": "SKU-1001", "warehouse": "west-1", "quantity": 25, "unit_cost": 12.50, "category": "electronics"  }
    
    item = RestockItem.model_validate(row)

    assert item.sku == "SKU-1001"
    assert item.quantity == 25

test_data = [
    ("category", "furniture"),
    ("quantity", -5),
    ("unit_cost", 0),
]

@pytest.mark.parametrize("field, bad_value", test_data)
def test_invalid_fields(field, bad_value):
    row = {
        "sku": "SKU-11225",
        "warehouse": "west-1",
        "quantity": 42,
        "unit_cost": 3.14,
        "category": "electronics",
    }
    row[field] = bad_value

    with pytest.raises(ValidationError):
        RestockItem.model_validate(row)

def test_for_missing_manifest():
    path = Path(__file__).parent / "notfound.json"
    with pytest.raises(ManifestFileNotFoundError):
        load_manifest(path)

def test_manifest(manifest_path):
    valid_items, error_rows = load_manifest(manifest_path)
    assert len(valid_items) == 8
    assert len(error_rows) == 4