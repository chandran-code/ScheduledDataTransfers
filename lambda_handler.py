""" About AWS authentication while connecting to s3 - There are two ways to do it. Either add s3 full aws_access_key_id
to the role of the lambda, or explicitly mention the access key/id in the code. Both the options are
below. I think role is used in aws env and access key/id is iused while testing locally """

# import pandas as pd
import generic_client1 as gc1
import generic_client2 as gc2

def lambda_handler(event, context):

    print("In the lambda ")
    gc1.transform_data()
    gc2.transform_data()

    return {
        'statusCode': 200,
        'body': 'Messages processed successfully'
    }

#lambda_handler(None, None)