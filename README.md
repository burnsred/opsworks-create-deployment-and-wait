# opsworks-create-deployment-and-wait

Creates a deployment command in Opsworks and waits until it finishes. If it
fails, exits with status 1.

Requires the following environmental variables to be set

 * `AWS_ACCESS_KEY_ID`: an AWS access key;
 * `AWS_SECRET_ACCESS_KEY`: the secret key for the above account.

Call as

    opsworks-create-deployment-and-wait <stack_id> <json_of_command> <comment_for_deployment> <app_id>

For example

    opsworks-create-deployment-and-wait aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa "{\"Name\":\"update_custom_cookbooks\"}" "Deploying new cookbooks" aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa

Documentation for the command dictionary syntax max be found in the [AWS CLI
documentation for the create-deployment command](http://docs.aws.amazon.com/cli/latest/reference/opsworks/create-deployment.html).
