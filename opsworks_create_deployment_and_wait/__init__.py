import time
from boto import opsworks

connection = opsworks.connect_to_region('us-east-1')

def create_deployment(stack_id, command, comment, app_id=None, layer_id=None):
    instance_ids = None

    if layer_id is not None:
        results = connection.describe_instances(layer_id=layer_id)
        instance_ids = [instance['InstanceId'] for instance in results['Instances']]

    deployment = connection.create_deployment(
        stack_id,
        command,
        comment=comment,
        app_id=app_id,
        instance_ids=instance_ids
    )

    return deployment['DeploymentId']

def get_status_of_deployment(deployment_id):
    result = connection.describe_deployments(deployment_ids=[deployment_id])
    return result['Deployments'][0]['Status']

def wait_until_deployment_is_finished(deployment_id, poll_interval=2):
    status = get_status_of_deployment(deployment_id)
    while status != "failed" and status != "successful":
        time.sleep(poll_interval)
        status = get_status_of_deployment(deployment_id)
    return status

