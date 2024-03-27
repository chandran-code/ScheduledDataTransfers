#### ScheduledDataTransfers ####
ScheduledDataTransfers

A template to run an AWS Lambda function for data ingestion from multiple sources.
Simply replace the codes in generic_ABC.py and generic_DEF.py with the actual data
transfer code written in FTP/SFTP/SQL pull etc.

The name of the sub-script is passed as a parameter into the main script lambda_handler.py.In an AWS environment these parameters can be passed from Event Bridge scheduler.


#### Commands to test locally ####
```
docker build -t scheduleddatatransfers .

docker run -p 9000:8080 scheduleddatatransfers:latest

curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d "{\"script\":\"generic_ABC\"}"


```
