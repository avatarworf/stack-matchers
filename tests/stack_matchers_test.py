import pytest
import json

from hamcrest import *
from datetime import datetime
from test_context import *
from stack_fixture import stack

def test_stack_has_status(stack):
    assert_that(stack, has_stack_status_in('UPDATE_COMPLETE', 'CREATE_COMPLETE'))

def test_stack_has_output_with_key(stack):
    assert_that(stack, has_output_with_key('TestOutputKey1'))

def test_stack_has_output(stack):
    assert_that(stack, has_output(with_key('TestOutputKey1'), with_value('TestOutputValue1')))
    assert_that(stack, has_output(with_key('TestOutputKey2'), with_value(ends_with('Value2'))))


