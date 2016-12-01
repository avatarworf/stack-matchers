import boto3
import pytest
import json

from hamcrest import *

from datetime import datetime

from test_context import *
from stack_matchers.boto_helper import *

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

print json.dumps(stack(), default=json_serial, indent=2, separators=(',', ': '))
print json.dumps(stack_resources(), default=json_serial, indent=2, separators=(',', ': '))
