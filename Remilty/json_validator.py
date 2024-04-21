import json
import sys
import re


def JsonValidator(jsonFile):
    # File validation
    with open(jsonFile, 'r') as file:
        try:
            data = json.load(file)
        except json.decoder.JSONDecodeError:
            raise Exception("Invalid JSON file")
    # PolicyName validation
    if not isinstance(data['PolicyName'], str) or not re.match('[\w+=,.@-]+', data['PolicyName']) or not 1 <= len(
            data['PolicyName']) <= 128:
        raise Exception("Invalid policy name")
    # PolicyDocument validation
    if not data['PolicyDocument'] or not isinstance(data['PolicyDocument'], dict):
        raise Exception("Invalid policy document")
    # Version validation
    if not data['PolicyDocument']['Version']:
        raise Exception("Version not specified")
    # "Statement" validation
    if not isinstance(data['PolicyDocument']['Statement'], list) and len(data['PolicyDocument']['Statement']) > 0:
        raise Exception("Statement is invalid")
    # check if an input JSON Resource field contains a single asterisk
    if data['PolicyDocument']['Statement'][0]['Resource'] == '*':
        return False
    return True


