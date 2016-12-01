## Synopsis

This project provides a number of hamcrest matchers that allow testing of cloudformation stacks in Python. 

Please take a look at [PyHamcrest](https://github.com/hamcrest/PyHamcrest) for documentation of how matchers work.

## Installing the matchers package

TODO: How to install using pip from github

## Usage Examples

The module stack_matchers.matchers provides a number of methods to create matchers that can verify stack properties. 

### 1) Import the matcher functions:
```
import pytest
from hamcrest import *
from stack_matchers.matchers import *
```

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

assert that the value of a stack output

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
