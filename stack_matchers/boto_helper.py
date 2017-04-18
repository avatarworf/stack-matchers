import boto3


class StackNotFoundError(Exception):
    pass


def get_stack(stack_name, boto_session=boto3.session.Session()):
    client = boto_session.client('cloudformation')

    response = client.describe_stacks(
        StackName=stack_name
    )

    if is_empty(response['Stacks']):
        raise StackNotFoundError("Stack not found")

    for stack in response['Stacks']:
        return stack

    return None


def get_stack_resources(stack_name, boto_session=boto3.session.Session()):
    client = boto_session.client('cloudformation')

    response = client.list_stack_resources(
        StackName=stack_name
    )

    if is_empty(response['StackResourceSummaries']):
        raise StackNotFoundError("Stack not found")

    full_list = []

    full_list.extend(response['StackResourceSummaries'])

    while 'NextToken' in response:
        response = client.list_stack_resources(
            StackName=stack_name,
            NextToken=response['NextToken']
        )
        full_list.extend(response['StackResourceSummaries'])

    return full_list


def is_empty(list):
    return not list
