""" About AWS authentication while connecting to s3 - There are two ways to do it. Either add s3 full aws_access_key_id
to the role of the lambda, or explicitly mention the access key/id in the code. Both the options are
below. I think role is used in aws env and access key/id is iused while testing locally """

# import pandas as pd

def transform_data():

    print("In generic_client1")
