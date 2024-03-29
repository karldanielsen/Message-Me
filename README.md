# Message Me

A Cloudformation template that automatically creates a lambda
proxy API to send text messages.

Once the template is deployed, the API endpoint can be found in the
AWS console or by running:

        $ aws cloudformation describe-stacks --stack-name {MessageMeStackName}

and finding the "outputs" section.
Any http POST request body passed to this endpoint will be forwarded
to the provided phone number.

The form of the API endpoint is:
https://{ID}.execute-api.us-east-1.amazonaws.com/{NAME}/message

A quick deployment (once your CLI is setup) can be achieved in two
steps:
#
_1a. If you want to edit the base template, pull this repo and run the following:_

        $ aws cloudformation package \
          --template-file template.yml \
          --s3-bucket {s3 Bucket Name} \
          --output-template-file output.yml
          
_1b. If you just want to deploy the existing template, retrieve a prebuilt template with:_

        $ wget https://message-me-template-bucket.s3.amazonaws.com/output.yml
#
_2. After packaging or retrieving a template, deploy it with:_

        $ aws cloudformation deploy \
          --template-file output.yml \
          --stack-name {MessageMeStackName} \
          --capabilities=CAPABILITY_IAM
          --parameter-overrides "apiGatewayName={Name}" \
                        "snsName={Name}" \
                        "phoneNum={Num w/ country code}" \
                        "originServers={* or URL}" \
                        "lambdaName={Name}"
#

NOTE: Be sure to select names that will not overlap with other AWS resources.

NOTE: Be careful setting originServers to *, CORS exists for a reason.
