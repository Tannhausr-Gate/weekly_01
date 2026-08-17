from pathlib import Path
from weekly_01.loader import load_manifest

def main() -> None:
    manifest_path = Path(__file__).parent.parent / "data/restock_manifest.json"
    valid_items, errors = load_manifest(manifest_path)


    print(f"Valid Items: {len(valid_items)}")
    print(f"Errors: {len(errors)}")

if __name__ == "__main__":
    main()