#Ejecuta el script y toma nota de la URL de la cola SQS creada.

import boto3

# Configura el cliente de SQS
sqs = boto3.client('sqs')

# Crea una cola SQS
response = sqs.create_queue(QueueName='MiColaSQS')
queue_url = response['QueueUrl']
print(f"arn:aws:sns:us-east-1:105371261454:TopicoSNS: {queue_url}")
