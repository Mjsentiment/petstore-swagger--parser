# get_version.py
import json

with open("swagger.yaml") as f:
    content = f.read()

# Example: extract version from Swagger spec
import re
match = re.search(r'version:\s*([0-9]+\.[0-9]+\.[0-9]+)', content)
version = match.group(1) if match else "0.0.1"

print(f"v{version}")
