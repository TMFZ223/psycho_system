import json
from pathlib import Path


class BaseValidator:

    BASE_DIR = Path(__file__).resolve().parent.parent
    SCHEMAS_DIR = BASE_DIR / "json_schemas"

    def load_schema(self, schema_name: str):
        schema_path = self.SCHEMAS_DIR / schema_name

        with open(schema_path) as file:
            return json.load(file)