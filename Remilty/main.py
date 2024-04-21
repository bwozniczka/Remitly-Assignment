import json
import sys
from json_validator import JsonValidator

if len(sys.argv) >= 2:
    print(JsonValidator(sys.argv[1]))
else:
    raise Exception("No json file name provided")
