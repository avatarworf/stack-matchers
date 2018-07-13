"""Match stack status values."""

from hamcrest.core.core.anyof import AnyOf
from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.helpers.wrap_matcher import wrap_matcher


class StackStatusMatcher(BaseMatcher):
    """Stack Status class matcher."""

    def __init__(self, stack_status_matcher):
        """Init the stack status matcher class."""
        self.stack_status_matcher = stack_status_matcher

    def _matches(self, item):
        """Do the two statuses match."""
        if not isinstance(item, dict):
            return False

        return self.stack_status_matcher.matches(item['StackStatus'])

    def describe_to(self, description):
        """Build description object."""
        description.append_text('Stack with StackStatus')
        description.append_description_of(self.stack_status_matcher)


def has_status(stack_status_matcher):
    """Check stack has a status."""
    return StackStatusMatcher(wrap_matcher(stack_status_matcher))


def has_status_in(*stack_statuses):
    """Check stack has a status in."""
    matchers = []

    for stack_status in stack_statuses:
        matchers.append(has_status(stack_status))

    return AnyOf(*matchers)
