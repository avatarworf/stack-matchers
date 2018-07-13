"""Match stack resource values."""

from hamcrest.core.core.anyof import any_of
from hamcrest.core.helpers.wrap_matcher import wrap_matcher
from hamcrest.core.base_matcher import BaseMatcher


class StackResourceMatcher(BaseMatcher):
    """Stack Resource class matcher."""

    def __init__(self, resource_type_matcher, resource_logical_id_matcher):
        """Init the stack resource matcher class."""
        self.resource_type_matcher = resource_type_matcher
        self.resource_logical_id_matcher = resource_logical_id_matcher
        self.resource_status_matcher = any_of('UPDATE_COMPLETE', 'CREATE_COMPLETE')

    def _matches(self, item):
        """Do the two resources match."""
        resources = item
        for resource in resources:
            if all([self.resource_type_matcher.matches(resource['ResourceType']),
                    self.resource_logical_id_matcher.matches(resource['LogicalResourceId']),
                    self.resource_status_matcher.matches(resource['ResourceStatus'])]):
                return True

        return False

    def describe_to(self, description):
        """Build description object."""
        description.append_text("Stack containing resource ")
        description.append_text("with ResourceType ")
        description.append_description_of(self.resource_type_matcher)
        description.append_text(", with LogicalResourceId ")
        description.append_description_of(self.resource_logical_id_matcher)
        description.append_text(" and with ResourceStatus one of ")
        description.append_description_of(self.resource_status_matcher)


def has_resource(resource_type_matcher, resource_logical_id_matcher):
    """Check for resource."""
    return StackResourceMatcher(wrap_matcher(resource_type_matcher), wrap_matcher(resource_logical_id_matcher))


def with_type(resource_type_matcher):
    """Check resource type."""
    return resource_type_matcher


def with_logical_id(resource_logical_id_matcher):
    """Check resource id."""
    return resource_logical_id_matcher
