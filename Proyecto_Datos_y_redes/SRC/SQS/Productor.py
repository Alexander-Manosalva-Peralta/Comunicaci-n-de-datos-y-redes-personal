#Envia mensajes a la cola creada desde AWS
import boto3

# Configura el cliente de SQS
sqs = boto3.client('sqs')

# URL de la cola SQS
queue_url = 'https://sqs.us-east-1.amazonaws.com/105371261454/MiColaSQS'

# Función para enviar mensajes a la cola
def send_message_to_sqs(message):
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=message
    )
    print(f'Message sent with ID: {response["MessageId"]}')

# Bloque principal para ejecutar el script
if __name__ == "__main__":
    # Ejemplo de envío de mensajes
    for i in range(10):
        send_message_to_sqs(f'Message {i}')
