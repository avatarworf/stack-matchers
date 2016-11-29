import boto3
import pytest
import json

from hamcrest import *

from datetime import datetime

from context import *

def get_stack(stack_name):
    client = boto3.client('cloudformation')

    response = client.describe_stacks(
        StackName=stack_name
    )

    for stack in response['Stacks']:
        return stack

    # TODO: Handle stack not found boto exception

    return None

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, datetime):
        serial = obj.isoformat()
        return serial
    raise TypeError ("Type not serializable")

def stack():
    return get_stack('FT-Tech-Infra-Dev-Account')

print json.dumps(stack(), default=json_serial, indent=2, separators=(',', ': '))
