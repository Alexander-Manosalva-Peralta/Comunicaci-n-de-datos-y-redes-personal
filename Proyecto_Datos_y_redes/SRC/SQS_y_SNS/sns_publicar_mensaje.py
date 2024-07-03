#script para publicar un mensaje en el tópico SNS.

import boto3

# Configura el cliente de SNS
sns = boto3.client('sns')

# ARN del tópico SNS (reemplaza con tu valor)
topic_arn = 'arn:aws:sns:us-east-1:105371261454:TopicoSNS'

# Publicar un mensaje en el tópico SNS
mensaje = "Este es un mensaje enviado al tópico de SNS"
response = sns.publish(
    TopicArn=topic_arn,
    Message=mensaje
)
print(f"Mensaje publicado en el tópico SNS: {response['MessageId']}")
