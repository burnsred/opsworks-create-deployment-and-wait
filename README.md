# opsworks-create-deployment-and-wait

Creates a deployment command in Opsworks and waits until it finishes. If it
fails, exits with status 1.

Requires the following environmental variables to be set

 * `AWS_ACCESS_KEY_ID`: an AWS access key;
 * `AWS_SECRET_ACCESS_KEY`: the secret key for the above account.

Call as

    opsworks-create-deployment-and-wait --stack-id <stack_id> --command <json_of_command> --comment <comment_for_deployment> [--layer-id <layer_id>] [--app-id <app_id>]

For example

    opsworks-create-deployment-and-wait --stack-id aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa --command "{\"Name\":\"update_custom_cookbooks\"}" --comment "Deploying new cookbooks"

Documentation for the command dictionary syntax max be found in the [AWS CLI
documentation for the create-deployment command](http://docs.aws.amazon.com/cli/latest/reference/opsworks/create-deployment.html).

If a layer id is provided the command will find all instances in that layer and
use those in the deployment. If just stack id is provided, all instances will
be included.