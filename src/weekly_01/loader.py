import json
from pathlib import Path
from weekly_01.exceptions import ManifestFileNotFoundError
from weekly_01.models import RestockItem
from pydantic import ValidationError


def load_manifest(path: Path) -> tuple[list[RestockItem], list[dict]]:
    
    try:
        file = path.read_text(encoding="utf-8")
        
    except FileNotFoundError as e:
        raise ManifestFileNotFoundError(f"No manifest file at {path}") from e

    rows = json.loads(file)

    valid_manifest: list[RestockItem] = []
    error_manifest: list[dict] = []

    for row in rows:
        try:
            item = RestockItem.model_validate(row)
            valid_manifest.append(item)
        except ValidationError as e:
            error_manifest.append(row)

    return valid_manifest, error_manifest