import boto3

class StackNotFoundError(Exception):
    pass

def get_stack(stack_name):
    client = boto3.client('cloudformation')

    response = client.describe_stacks(
        StackName=stack_name
    )
    
    if is_empty(response['Stacks']):
        raise StackNotFoundError("Stack not found")

    for stack in response['Stacks']:
        return stack

    return None

def get_stack_resources(stack_name):
    client = boto3.client('cloudformation')

    response = client.list_stack_resources(
        StackName=stack_name
    )

    if is_empty(response['StackResourceSummaries']):
        raise StackNotFoundError("Stack not found")

    return response['StackResourceSummaries']

def is_empty(list):
    return not list
