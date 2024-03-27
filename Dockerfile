FROM public.ecr.aws/lambda/python:3.8

COPY requirements.txt ./
RUN pip3 install -r requirements.txt
COPY lambda_handler.py generic_ABC.py generic_DEF.py config.ini ./

CMD ["lambda_handler.lambda_handler"]
