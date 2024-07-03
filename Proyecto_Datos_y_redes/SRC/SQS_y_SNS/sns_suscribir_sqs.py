#Script para suscribir la cola SQS al tópico SNS.

import boto3
import json

# Configura los clientes de SNS y SQS
sns = boto3.client('sns')
sqs = boto3.client('sqs')

# ARN del tópico SNS y URL de la cola SQS (reemplaza con tus valores)
topic_arn = 'arn:aws:sns:us-east-1:105371261454:TopicoSNS'
queue_url = 'https://sqs.us-east-1.amazonaws.com/105371261454/MiColaSQS'

# Obtener el ARN de la cola SQS
response = sqs.get_queue_attributes(
    QueueUrl=queue_url,
    AttributeNames=['QueueArn']
)
queue_arn = response['Attributes']['QueueArn']

# Configurar la política de acceso de la cola SQS para permitir mensajes del tópico SNS
policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "sqs:SendMessage",
            "Resource": queue_arn,
            "Condition": {
                "ArnEquals": {
                    "aws:SourceArn": topic_arn
                }
            }
        }
    ]
}

sqs.set_queue_attributes(
    QueueUrl=queue_url,
    Attributes={
        'Policy': json.dumps(policy)
    }
)

# Suscribir la cola SQS al tópico SNS
response = sns.subscribe(
    TopicArn=topic_arn,
    Protocol='sqs',
    Endpoint=queue_arn
)
print(f"Suscripción de la cola SQS al tópico SNS configurada: {response}")


import boto3
import json

# Configura los clientes de SNS y SQS
sns = boto3.client('sns')
sqs = boto3.client('sqs')

# ARN del tópico SNS y URL de la cola SQS (reemplaza con tus valores)
topic_arn = 'arn:aws:sns:us-east-1:105371261454:TopicoSNS'
queue_url = 'https://sqs.us-east-1.amazonaws.com/105371261454/MiColaSQS'

# Obtener el ARN de la cola SQS
response = sqs.get_queue_attributes(
    QueueUrl=queue_url,
    AttributeNames=['QueueArn']
)
queue_arn = response['Attributes']['QueueArn']

# Configurar la política de acceso de la cola SQS para permitir mensajes del tópico SNS
policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "sqs:SendMessage",
            "Resource": queue_arn,
            "Condition": {
                "ArnEquals": {
                    "aws:SourceArn": topic_arn
                }
            }
        }
    ]
}

sqs.set_queue_attributes(
    QueueUrl=queue_url,
    Attributes={
        'Policy': json.dumps(policy)
    }
)

# Suscribir la cola SQS al tópico SNS
response = sns.subscribe(
    TopicArn=topic_arn,
    Protocol='sqs',
    Endpoint=queue_arn
)
print(f"Suscripción de la cola SQS al tópico SNS configurada: {response}")


import boto3
import json

# Configura los clientes de SNS y SQS
sns = boto3.client('sns')
sqs = boto3.client('sqs')

# ARN del tópico SNS y URL de la cola SQS (reemplaza con tus valores)
topic_arn = 'arn:aws:sns:us-east-1:105371261454:TopicoSNS'
queue_url = 'https://sqs.us-east-1.amazonaws.com/105371261454/MiColaSQS'

# Obtener el ARN de la cola SQS
response = sqs.get_queue_attributes(
    QueueUrl=queue_url,
    AttributeNames=['QueueArn']
)
queue_arn = response['Attributes']['QueueArn']

# Configurar la política de acceso de la cola SQS para permitir mensajes del tópico SNS
policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "sqs:SendMessage",
            "Resource": queue_arn,
            "Condition": {
                "ArnEquals": {
                    "aws:SourceArn": topic_arn
                }
            }
        }
    ]
}

sqs.set_queue_attributes(
    QueueUrl=queue_url,
    Attributes={
        'Policy': json.dumps(policy)
    }
)

# Suscribir la cola SQS al tópico SNS
response = sns.subscribe(
    TopicArn=topic_arn,
    Protocol='sqs',
    Endpoint=queue_arn
)
print(f"Suscripción de la cola SQS al tópico SNS configurada: {response}")
