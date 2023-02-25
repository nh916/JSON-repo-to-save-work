import json
from jsonschema import validate, exceptions

db_schema = open("./node_test/db_schema.json")
db_schema = json.load(db_schema)

node_json = open("./node_test/protein_plastic.json")
node_json = json.load(node_json)

validate(instance=node_json, schema=db_schema)
