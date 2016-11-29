from hamcrest.core.core.anyof import AnyOf
from hamcrest.core.helpers.wrap_matcher import wrap_matcher
from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.helpers.hasmethod import hasmethod

class StackParameterMatcher(BaseMatcher):

    def __init__(self, param_key_matcher, param_value_matcher):
        self.param_key_matcher = param_key_matcher
        self.param_value_matcher = param_value_matcher

    def _matches(self, item):

        params = item['Parameters']
        for param in params:
            if self.param_key_matcher.matches(param['ParameterKey']) and self.param_value_matcher.matches(param['ParameterValue']):
                return True

        return False

    def describe_to(self, description):
        description.append_text("Stack containing parameter ")
        description.append_text("with ParameterKey ")
        description.append_description_of(self.param_key_matcher)
        description.append_text(" and with ParameterValue ")
        description.append_description_of(self.param_value_matcher)


class StackParameterKeyMatcher(BaseMatcher):

    def __init__(self, param_key_matcher):
        self.param_key_matcher = param_key_matcher

    def _matches(self, item):
        if not type(item) is dict:
            return False
 
        params = item['Parameters']
        for param in params:
            if self.param_key_matcher.matches(param['ParameterKey']):
                return True
 
        return False

    def describe_to(self, description):
        description.append_text('Stack containing parameter with ParameterKey ')
        description.append_description_of(self.param_key_matcher)    

def has_parameter_with_key(param_key_matcher):
    return StackParameterKeyMatcher(wrap_matcher(param_key_matcher))

def has_parameter(param_key_matcher, param_value_matcher):
    return StackParameterMatcher(wrap_matcher(param_key_matcher), wrap_matcher(param_value_matcher))

