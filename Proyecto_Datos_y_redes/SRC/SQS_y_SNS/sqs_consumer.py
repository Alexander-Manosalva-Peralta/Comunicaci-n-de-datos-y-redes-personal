#Para leer y procesar los mensajes de la cola SQS.

import boto3
import time

# Configura el cliente de SQS
sqs = boto3.client('sqs')

# URL de la cola SQS (reemplaza con tu valor)
queue_url = 'https://sqs.us-east-1.amazonaws.com/105371261454/MiColaSQS'

# Leer y procesar mensajes de la cola de forma continua
while True:
    response = sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=1,
        WaitTimeSeconds=20
    )

    if 'Messages' in response:
        for message in response['Messages']:
            # Procesar el mensaje
            print(f'Received message: {message["Body"]}')
            
            # Eliminar el mensaje de la cola
            sqs.delete_message(
                QueueUrl=queue_url,
                ReceiptHandle=message['ReceiptHandle']
            )
    else:
        print('No messages available')
    time.sleep(5)
