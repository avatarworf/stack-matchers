from hamcrest.core.core.anyof import AnyOf
from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.helpers.hasmethod import hasmethod
from hamcrest.core.helpers.wrap_matcher import wrap_matcher

class StackStatusMatcher(BaseMatcher):

    def __init__(self, stack_status_matcher):
        self.stack_status_matcher = stack_status_matcher

    def _matches(self, item):
        if not type(item) is dict:
            return False
 
        return self.stack_status_matcher.matches(item['StackStatus'])

    def describe_to(self, description):
        description.append_text('Stack with StackStatus')
        description.append_description_of(self.stack_status_matcher)    

def has_status(stack_status_matcher):
    return StackStatusMatcher(wrap_matcher(stack_status_matcher))

def has_status_in(*stack_statuses):
    matchers = []

    for stack_status in stack_statuses:
        matchers.append(has_status(stack_status))

    return AnyOf(*matchers)
 
