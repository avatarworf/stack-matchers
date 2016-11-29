import pytest
import json

from hamcrest import *
from datetime import datetime
from test_context import *
from stack_fixtures import stack, stack_resources

def test_stack_has_status(stack):
    assert_that(stack, has_stack_status_in('UPDATE_COMPLETE', 'CREATE_COMPLETE'))

def test_stack_has_output_with_key(stack):
    assert_that(stack, has_output_with_key('TestOutputKey1'))

def test_stack_has_output(stack):
    assert_that(stack, has_output('TestOutputKey1', 'TestOutputValue1'))
    assert_that(stack, has_output(with_key('TestOutputKey2'), with_value(ends_with('Value2'))))

def test_stack_has_parameter_with_key(stack):
    assert_that(stack, has_parameter_with_key('TestParamKey1'))

def test_stack_has_parameter(stack):
    assert_that(stack, has_parameter('TestParamKey1', 'TestParamValue1'))
    assert_that(stack, has_parameter(with_key('TestParamKey2'), with_value(starts_with('TestParamValue'))))

def test_stack_has_resource(stack_resources):
    assert_that(stack_resources, has_resource(with_type("AWS::CloudFormation::Stack"), with_logical_id("TestResource122")))
