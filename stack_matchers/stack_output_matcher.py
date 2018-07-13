"""Match stack output values."""

from hamcrest.core.helpers.wrap_matcher import wrap_matcher
from hamcrest.core.base_matcher import BaseMatcher


class StackOutputMatcher(BaseMatcher):
    """Output class."""

    def __init__(self, output_key_matcher, output_value_matcher):
        """Init the stack output matcher class."""
        self.output_key_matcher = output_key_matcher
        self.output_value_matcher = output_value_matcher

    def _matches(self, item):
        """Do the two stacks match."""
        outputs = item['Outputs']
        for output in outputs:
            if self.output_key_matcher.matches(output['OutputKey']) and self.output_value_matcher.matches(output['OutputValue']):
                return True

        return False

    def describe_to(self, description):
        """Build description object."""
        description.append_text("Stack containing output ")
        description.append_text("with OutputKey ")
        description.append_description_of(self.output_key_matcher)
        description.append_text(" and with OutputValue ")
        description.append_description_of(self.output_value_matcher)


class StackOutputKeyMatcher(BaseMatcher):
    """Output Key class."""

    def __init__(self, output_key_matcher):
        """Init the stack output key macher class."""
        self.output_key_matcher = output_key_matcher

    def _matches(self, item):
        """Do the two output keys match."""
        if not isinstance(item, dict):
            return False

        outputs = item['Outputs']
        for output in outputs:
            if self.output_key_matcher.matches(output['OutputKey']):
                return True

        return False

    def describe_to(self, description):
        """Build description object."""
        description.append_text('Stack containing Output with OutputKey ')
        description.append_description_of(self.output_key_matcher)


def has_output_with_key(output_key_matcher):
    """Check values of the stacks output keys."""
    return StackOutputKeyMatcher(wrap_matcher(output_key_matcher))


def has_output(output_key_matcher, output_value_matcher):
    """Check values of the stacks outputs."""
    return StackOutputMatcher(wrap_matcher(output_key_matcher), wrap_matcher(output_value_matcher))


def with_key(output_key_matcher):
    """Check does it have a key."""
    return output_key_matcher


def with_value(output_value_matcher):
    """Check does it have a value."""
    return output_value_matcher
