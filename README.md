#### ScheduledDataTransfers
ScheduledDataTransfers

* Learn how to run lambda on docker container and deploy Base image on ECR and use on Lambda 


#### Commands 
```
docker build -t scheduleddatatransfers .

docker run -p 9000:8080 scheduleddatatransfers:latest

curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d "{\"script\":\"generic_ABC\"}"


```
