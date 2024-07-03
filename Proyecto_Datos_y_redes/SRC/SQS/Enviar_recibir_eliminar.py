#Envía mensaje, recibe el mensaje y elimina el mensaje.

import boto3

# Configura el cliente de SQS
sqs = boto3.client('sqs')

# URL de la cola SQS
queue_url = 'https://sqs.us-east-1.amazonaws.com/105371261454/MiColaSQS'

def send_message():
    # Enviar mensaje a la cola SQS
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody='Hola, este es un mensaje de prueba!'
    )
    print(f'Mensaje enviado: {response["MessageId"]}')

def receive_and_delete_message():
    # Recibir y procesar mensaje de la cola SQS 
    response = sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=1,
        WaitTimeSeconds=20
    )

    if 'Messages' in response:
        for message in response['Messages']:
            # Procesar el mensaje recibido
            print(f'Received message: {message["Body"]}')
            
            # Eliminar el mensaje de la cola
            sqs.delete_message(
                QueueUrl=queue_url,
                ReceiptHandle=message['ReceiptHandle']
            )
