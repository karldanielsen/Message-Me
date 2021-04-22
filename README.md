# Message Me

A Cloudformation template that automatically creates a lambda
proxy API to send text messages.

Once the template is deployed, check API gateway deployments for
the endpoint URL. The http POST request body passed to the URL
is texted to the provided phone number.

The form of the API endpoint is:
https://{ID}.execute-api.us-east-1.amazonaws.com/{NAME}/message

A quick deployment (once your CLI is setup) can be achieved in two
steps:

### 1a. If you want to edit the base template, pull this repo and run
the following:

        $ aws cloudformation package \
          --template-file template.yml \
          --s3-bucket {s3 Bucket Name} \
          --output-template-file output.yml
          
### 1b. If you just want to deploy the existing template, retrieve a
prebuilt template with:

        $ wget https://message-me-template-bucket.s3.amazonaws.com/output.yml

### 2. After packaging or retrieving a template, deploy it with:

        $ aws cloudformation deploy \
          --template-file output.yml \
          --stack-name {MessageMeStackName} \
          --capabilities=CAPABILITY_IAM
          --parameter-overrides "apiGatewayName={Name}" \
                        "snsName={Name}" \
                        "phoneNum={Num w/ country code}" \
                        "originServers={* or URL}" \
                        "lambdaName={Name}"

NOTE: Be sure to select names that will not overlap with other AWS resources.

NOTE: Be careful setting originServers to *, CORS exists for a reason.

