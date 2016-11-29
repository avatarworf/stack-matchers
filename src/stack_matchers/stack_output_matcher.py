from hamcrest.core.core.anyof import AnyOf
from hamcrest.core.helpers.wrap_matcher import wrap_matcher
from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.helpers.hasmethod import hasmethod

class StackOutputMatcher(BaseMatcher):

    def __init__(self, output_key_matcher, output_value_matcher):
        self.output_key_matcher = output_key_matcher
        self.output_value_matcher = output_value_matcher

    def _matches(self, item):

        outputs = item['Outputs']
        for output in outputs:
            if self.output_key_matcher.matches(output['OutputKey']) and self.output_value_matcher.matches(output['OutputValue']):
                return True

        return False

    def describe_to(self, description):
        description.append_text("Stack containing output ")
        description.append_text("with OutputKey ")
        description.append_description_of(self.output_key_matcher)
        description.append_text(" and with OutputValue ")
        description.append_description_of(self.output_value_matcher)


class StackOutputKeyMatcher(BaseMatcher):

    def __init__(self, output_key_matcher):
        self.output_key_matcher = output_key_matcher

    def _matches(self, item):
        if not type(item) is dict:
            return False
 
        outputs = item['Outputs']
        for output in outputs:
            if self.output_key_matcher.matches(output['OutputKey']):
                return True
 
        return False

    def describe_to(self, description):
        description.append_text('Stack containing Output with OutputKey ')
        description.append_description_of(self.output_key_matcher)    

def has_output_with_key(output_key_matcher):
    return StackOutputKeyMatcher(wrap_matcher(output_key_matcher))

def has_output(output_key_matcher, output_value_matcher):
    return StackOutputMatcher(wrap_matcher(output_key_matcher), wrap_matcher(output_value_matcher))

def with_key(output_key_matcher):
    return output_key_matcher

def with_value(output_value_matcher):
    return output_value_matcher
