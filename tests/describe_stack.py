import boto3
import pytest
import json

from hamcrest import *

from datetime import datetime

from test_context import *

def get_stack(stack_name):
    client = boto3.client('cloudformation')

    response = client.describe_stacks(
        StackName=stack_name
    )

    return response

    for stack in response['Stacks']:
        return stack

    return None

def get_stack_resources(stack_name):
    client = boto3.client('cloudformation')

    response = client.list_stack_resources(
        StackName=stack_name
    )

    return response['StackResourceSummaries']

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, datetime):
        serial = obj.isoformat()
        return serial
    raise TypeError ("Type not serializable")

def stack():
    return get_stack('FT-Tech-Infra-Dev-Account')

def stack_resources():
    return get_stack_resources('FT-Tech-Infra-Dev-Account')

#print json.dumps(stack(), default=json_serial, indent=2, separators=(',', ': '))
print json.dumps(stack_resources(), default=json_serial, indent=2, separators=(',', ': '))
