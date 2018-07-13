"""Match stack parameter values."""

from hamcrest.core.helpers.wrap_matcher import wrap_matcher
from hamcrest.core.base_matcher import BaseMatcher


class StackParameterMatcher(BaseMatcher):
    """Stack Parmater class matcher."""

    def __init__(self, param_key_matcher, param_value_matcher):
        """Init the stack parameter matcher class."""
        self.param_key_matcher = param_key_matcher
        self.param_value_matcher = param_value_matcher

    def _matches(self, item):
        """Do the parameters match."""
        params = item['Parameters']
        for param in params:
            if self.param_key_matcher.matches(param['ParameterKey']) and self.param_value_matcher.matches(param['ParameterValue']):
                return True

        return False

    def describe_to(self, description):
        """Build description object."""
        description.append_text("Stack containing parameter ")
        description.append_text("with ParameterKey ")
        description.append_description_of(self.param_key_matcher)
        description.append_text(" and with ParameterValue ")
        description.append_description_of(self.param_value_matcher)


class StackParameterKeyMatcher(BaseMatcher):
    """Stack Key Parmater class matcher."""

    def __init__(self, param_key_matcher):
        """Init the stack key parameter matcher class."""
        self.param_key_matcher = param_key_matcher

    def _matches(self, item):
        """Do the key parameters match."""
        if not isinstance(item, dict):
            return False

        params = item['Parameters']
        for param in params:
            if self.param_key_matcher.matches(param['ParameterKey']):
                return True

        return False

    def describe_to(self, description):
        """Build description object."""
        description.append_text('Stack containing parameter with ParameterKey ')
        description.append_description_of(self.param_key_matcher)


def has_parameter_with_key(param_key_matcher):
    """Check values of the stacks parameters keys."""
    return StackParameterKeyMatcher(wrap_matcher(param_key_matcher))


def has_parameter(param_key_matcher, param_value_matcher):
    """Check values of the stacks parameters."""
    return StackParameterMatcher(wrap_matcher(param_key_matcher), wrap_matcher(param_value_matcher))
