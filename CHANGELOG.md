# Change Log created on 2018-10-23

### 2018-10-23
  * refactor python package creation to push version to nexus
  * correct dir
  * correct pip install

### 2018-10-08
  * correction to pulling in context
  * remove import
  * update license
  * update supporting files

### 2018-09-25
  * updates
  * updated to use aws-composer-general package

### 2018-09-21
  * Add license details

### 2018-07-24
  * stack matcher not required here
  * for now 60% coverage ok

### 2018-07-13
  * place test requirements into different file, plus typo correction
  * add coverage
  * correction
  * add GoCD pipeline test
  * typo
  * PEP8 a bit ; mostly adding docstrings plus change the way the include within matchers.py works. currently in GOCD there is this error:
  * update team info and bump to 0.0.2

### 2017-04-24
  * add optional boto_session argument to allow for use of assumed role sessions

### 2017-04-18
  * Updates boto helper to deal with list_resource_stacks results that are paginated

### 2017-03-10

### 2016-12-02
  * Fixed grammar
  * Added code block around get_resource example
  * Fixed typo
  * Fixed import in doco
  * Fixed import in doco
  * Added details of stack and stack_resources fixtures
  * Added boto3 dependency for boto_helper module
  * Added a simple helper functions for retrieval of a stack and stack resources using boto
  * Add doco for has_resource matcher
  * Tweak heading
  * Tweak heading
  * Added pip installation commands for stack-matchers module
  * Updates to make module usable from another project
  * Adding setup.py
  * Added code block formatting
  * Added details for matchers
  * Added matcher variants for stack status

### 2016-12-01
  * Updated stack_status_matcher to accept other matchers
  * Moved stack_matchers module to root, and removed src directory

### 2016-11-30
  * Fixed broken test
  * Added matcher for stack resources
  * Added matcher for stack parameters
  * Added instructions for running unit tests
  * Initial version with matchers for stack status and stack outputs
