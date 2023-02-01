Stack Matchers
==============

Synopsis
--------

This project provides a number of hamcrest matchers that allow testing
of cloudformation stacks in Python.

Please take a look at
`PyHamcrest <https://github.com/hamcrest/PyHamcrest>`__ for
documentation of how matchers work.

Installing stack-matchers
-------------------------

To install manually:

.. code:: bash

   pip install git+ssh://git@github.com/Financial-Times/stack-matchers

or add the following line to requirements.txt

.. code:: sh

   git+ssh://git@github.com/Financial-Times/stack-matchers

Usage Examples
--------------

The module stack_matchers.matchers provides a number of methods to
create matchers that can verify stack properties.

Imports
~~~~~~~

.. code:: python

   import pytest
   from hamcrest import *
   from stack_matchers.matchers import *

Retrieve a stack using boto
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The utility module stack_matchers.boto_helper provides a function
get_stack(stack_name) that can be used to create a pytest fixture e.g.

.. code:: python

   from stack_matchers.boto_helper import get_stack

   @pytest.fixture
   def stack():
       return get_stack("FT-Tech-Infra_dev-Account")

Retrieve stack resources using boto
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The utility module stack_matchers.boto_helper provides a function
get_stack_resources(stack_name) that can be used to create a pytest
fixture e.g.

.. code:: python

   from stack_matchers.boto_helper import get_stack_resources

   @pytest.fixture
   def stack_resources():
       return get_stack_resources("FT-Tech-Infra_dev-Account")

Note the stack and stack_resources fixtures are used in the stack
matcher reference below.

Stack Matchers Reference
------------------------

has status
~~~~~~~~~~

assert the stack status of a cloudformation stack

.. code:: python

   def test_stack_has_status(stack):
       assert_that(stack, has_status('UPDATE_COMPLETE'))
       assert_that(stack, has_status(equal_to('UPDATE_COMPLETE')
       assert_that(stack, has_status(ends_with('_COMPLETE')
       assert_that(stack, has_status(any_of('UPDATE_COMPLETE', 'CREATE_COMPLETE')))

has_status_in
~~~~~~~~~~~~~

assert that the stack status of a cloudformation stack is one of a
number of values

.. code:: python

   def test_stack_has_status(stack):
       assert_that(stack, has_status_in('UPDATE_COMPLETE', 'CREATE_COMPLETE'))

has_resource
~~~~~~~~~~~~

assert that the stack has created a resource with a cloudformation type
and logical id

.. code:: python

   def test_stack_has_resource(stack_resources):
       assert_that(stack_resources, has_resource("AWS::CloudFormation::Stack", "TestResource1"))
       assert_that(stack_resources, has_resource(with_type("AWS::CloudFormation::Stack"), with_logical_id("TestResource1")))

Note the asserts require the stack_resources fixture rather than the
stack fixture

has_parameter
~~~~~~~~~~~~~

assert the value of a stack parameter that was used during stack
execution

.. code:: python

   def test_stack_has_parameter(stack):
       assert_that(stack, has_parameter('TestParamKey1', 'TestParamValue1'))
       assert_that(stack, has_parameter(with_key('TestParamKey1'), with_value('TestParamValue1')))
       assert_that(stack, has_parameter(with_key('TestParamKey1'), ends_with('Value1')))

has_parameter_with_key
~~~~~~~~~~~~~~~~~~~~~~

assert that a parameter with a key was supplied

.. code:: python

   def test_stack_has_parameter_with_key(stack):
       assert_that(stack, has_parameter_with_key('TestParamKey1'))

has_output
~~~~~~~~~~

assert the value of a stack output

.. code:: python

   def test_stack_has_output(stack):
       assert_that(stack, has_output('TestOutputKey1', 'TestOutputValue1'))
       assert_that(stack, has_output(with_key('TestOutputKey1'), with_value('TestOutputValue1')))
       assert_that(stack, has_output(with_key('TestParamKey1'), start_with('TestOutput')))

has_output_with_key
~~~~~~~~~~~~~~~~~~~

assert that an output exists

.. code:: python

   def test_stack_has_output_with_key(stack):
       assert_that(stack, has_output_with_key('TestOutputKey1'))

Development
-----------

It is best to use virtualenv to develop this codebase. Please run the
following commands from the root of the project:

.. code:: bash

   mkvirtualenv --python=$(command -v python3.6) temp_venv
   pip install -U -e \
       "git+ssh://git@github.com/Financial-Times/aws-composer-pipeline-scripts-general.git@main#egg=aws_composer_general[python_release]" \
       -r requirements.txt \
       --process-dependency-links
   export AWS_DEFAULT_REGION=eu-west-1

You can verify tests by:

.. code:: bash

   composer run-tests --coverage --cov_dir="$(python3 setup.py --name)" tests/

Licence
-------

This software is published by the Financial Times under the `MIT
licence <http://opensource.org/licenses/MIT>`__.

Notice to non-FT developers
---------------------------

This software is made available by the FT under an MIT licence but, as
is our right under that licence, we do not take any responsibility for
what you do with it, and currently do not intend to engage with any
external efforts to contribute to it. We are always delighted to hear
from you if you find it useful, but please understand that we may not
respond to issues raised here on GitHub. Open source projects on which
we actively engage with the open source community can be found on
github.com/ftlabs.
