#Publica mensaje en todos los usuarios que están dentro de ese t´´opido y administra a los suscriptores

import boto3
from botocore.exceptions import ClientError

# Configura el cliente de SNS
sns = boto3.client('sns')

# ARN del tópico (reemplaza 'arn_del_topico' con el ARN real)
topic_arn = 'arn:aws:sns:us-east-1:105371261454:MiTopicoSNS'

def publicar_mensaje_en_topico(mensaje):
    try:
        # Publica el mensaje en el tópico especificado
        response = sns.publish(
            TopicArn=topic_arn,
            Message=mensaje
        )
        print(f"Mensaje publicado en el tópico: {response['MessageId']}")
    except ClientError as e:
        print(f"Error al publicar mensaje en el tópico: {e}")

def gestionar_suscripciones():
    # Intenta configurar una suscripción por correo electrónico
    try:
        response = sns.subscribe(
            TopicArn=topic_arn,
            Protocol='email',
            Endpoint='yojan.manosalva@upch.pe'
        )
        print(f"Suscripción por correo electrónico creada: {response['SubscriptionArn']}")
    except ClientError as e:
        print(f"Error al crear la suscripción por correo electrónico: {e}")

    # Intenta configurar una suscripción por HTTP/HTTPS
    try:
        response = sns.subscribe(
            TopicArn=topic_arn,
            Protocol='https',
            Endpoint='https://webhook.site/df82483f-44ae-48f8-82a6-4ef84f930e1c' 
        )
        print(f"Suscripción por HTTP/HTTPS creada: {response['SubscriptionArn']}")
    except ClientError as e:
        print(f"Error al crear la suscripción por HTTP/HTTPS: {e}")

# Ejemplo de uso: publicar un mensaje en el tópico y gestionar suscripciones
if __name__ == "__main__":
    mensaje = "Este es un mensaje de prueba para el tópico SNS"
    publicar_mensaje_en_topico(mensaje)
    gestionar_suscripciones()
