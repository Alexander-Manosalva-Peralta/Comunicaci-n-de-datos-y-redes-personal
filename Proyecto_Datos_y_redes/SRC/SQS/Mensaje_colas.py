import boto3

# Configura el cliente de SQS
sqs = boto3.client('sqs')

# URL de cada cola SQS
queue_urls = [
    'https://sqs.us-east-1.amazonaws.com/105371261454/MiColaSQS3',
    'https://sqs.us-east-1.amazonaws.com/105371261454/MiColaSQS4',
    'https://sqs.us-east-1.amazonaws.com/105371261454/MiColaSQS5',
    'https://sqs.us-east-1.amazonaws.com/105371261454/MiColaSQS6',
    'https://sqs.us-east-1.amazonaws.com/105371261454/MiColaSQS7'
]

# Enviar mensajes de prueba a cada cola
for queue_url in queue_urls:
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody='Este es un mensaje de prueba'
    )
    print(f"Mensaje enviado a {queue_url}: {response['MessageId']}")
