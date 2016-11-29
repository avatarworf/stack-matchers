import pytest
import json
from json import JSONDecoder

from datetime import datetime

class DateTimeDecoder(json.JSONDecoder):

    def __init__(self, *args, **kargs):
        JSONDecoder.__init__(self, object_hook=self.dict_to_object,
                             *args, **kargs)
    
    def dict_to_object(self, d): 
        if '__type__' not in d:
            return d

        type = d.pop('__type__')
        try:
            dateobj = datetime(**d)
            return dateobj
        except:
            d['__type__'] = type
            return d

@pytest.fixture
def stack():
    with open('stack_fixture.json') as data_file:    
        data = data_file.read()
        return json.loads(data, cls=DateTimeDecoder)

@pytest.fixture
def stack_resources():
    with open('stack_resources_fixture.json') as data_file:
        data = data_file.read()
        return json.loads(data, cls=DateTimeDecoder)
