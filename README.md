## Synopsis

This project provides a number of hamcrest matchers that allow testing of cloudformation stacks in Python. 

Please take a look at [PyHamcrest](https://github.com/hamcrest/PyHamcrest) for documentation of how matchers work.

## Installing stack-matchers

To install manually:
```
pip install git+ssh://git@github.com/Financial-Times/stack-matchers
```
or add the following line to requirements.txt
```
git+ssh://git@github.com/Financial-Times/stack-matchers
```

## Usage Examples

The module stack_matchers.matchers provides a number of methods to create matchers that can verify stack properties. 

### Imports
```
import pytest
from hamcrest import *
from stack_matchers.matchers import *
```

### Retrieve a stack using boto

The utility module stack_matchers.boto_helper provides a function get_stack(stack_name) that can be used to create a pytest fixture e.g.
```
from stack_matchers.boto_helper import get_stack

@pytest.fixture
def stack():
    return get_stack("FT-Tech-Infra_dev-Account")
```

### Retrieve stack resources using boto

The utility module stack_matchers.boto_helper provides a function get_stack_resources(stack_name) that can be used to create a pytest fixture e.g.
```
from stack_matchers.boto_helper import get_stack_resources

@pytest.fixture
def stack_resources():
    return get_stack_resources("FT-Tech-Infra_dev-Account")
```

Note the stack and stack_resources fixtures are used in the stack matcher reference below.

## Stack Matchers Reference

### has status

assert the stack status of a cloudformation stack

```
def test_stack_has_status(stack):
    assert_that(stack, has_status('UPDATE_COMPLETE'))
    assert_that(stack, has_status(equal_to('UPDATE_COMPLETE')
    assert_that(stack, has_status(ends_with('_COMPLETE')
    assert_that(stack, has_status(any_of('UPDATE_COMPLETE', 'CREATE_COMPLETE')))
```

### has_status_in

assert that the stack status of a cloudformation stack is one of a number of values

```
def test_stack_has_status(stack):
    assert_that(stack, has_status_in('UPDATE_COMPLETE', 'CREATE_COMPLETE'))
```

### has_resource

assert that the stack has created a resource with a cloudformation type and logical id

```
def test_stack_has_resource(stack_resources):
    assert_that(stack_resources, has_resource("AWS::CloudFormation::Stack", "TestResource1"))
    assert_that(stack_resources, has_resource(with_type("AWS::CloudFormation::Stack"), with_logical_id("TestResource1")))
```

Note the asserts require the stack_resources fixture rather than the stack fixture

### has_parameter

assert the value of a stack parameter that was used during stack execution 

```
def test_stack_has_parameter(stack):
    assert_that(stack, has_parameter('TestParamKey1', 'TestParamValue1'))
    assert_that(stack, has_parameter(with_key('TestParamKey1'), with_value('TestParamValue1')))
    assert_that(stack, has_parameter(with_key('TestParamKey1'), ends_with('Value1')))
```

### has_parameter_with_key

assert that a parameter with a key was supplied

```
def test_stack_has_parameter_with_key(stack):
    assert_that(stack, has_parameter_with_key('TestParamKey1'))
```

### has_output

assert the value of a stack output

```
def test_stack_has_output(stack):
    assert_that(stack, has_output('TestOutputKey1', 'TestOutputValue1'))
    assert_that(stack, has_output(with_key('TestOutputKey1'), with_value('TestOutputValue1')))
    assert_that(stack, has_output(with_key('TestParamKey1'), start_with('TestOutput')))'
```

### has_output_with_key

assert that an output exists

```
def test_stack_has_output_with_key(stack):
    assert_that(stack, has_output_with_key('TestOutputKey1'))
```

## Developer Setup

It is best to use virtualenv to develop this codebase. Please run the following commands from the root of the project:

```
virtualenv venv
source ./venv/bin/activate
pip install -r requirements.txt
```

## Run Unit Tests

```
cd tests
py.test
```
