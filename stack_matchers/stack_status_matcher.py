from hamcrest.core.core.anyof import AnyOf
from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.helpers.hasmethod import hasmethod

class StackStatusMatcher(BaseMatcher):

    def __init__(self, stack_status):
        self.stack_status = stack_status

    def _matches(self, item):
        if not type(item) is dict:
            return False
 
        return item['StackStatus'] == self.stack_status

    def describe_to(self, description):
        description.append_text('Stack with StackStatus = {0}'.format(self.stack_status))    

def has_stack_status_equal_to(stack_status):
    return StackStatusMatcher(stack_status)

def has_stack_status_in(*stack_statuses):
    matchers = []

    for stack_status in stack_statuses:
        matchers.append(StackStatusMatcher(stack_status))

    return AnyOf(*matchers)
 
