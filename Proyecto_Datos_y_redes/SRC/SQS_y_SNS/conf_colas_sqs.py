#Ejecuta el script y toma nota del ARN del tópico SNS creado. Asegúrate de que el código no tenga errores.

import boto3

# Configura el cliente de SNS
sns = boto3.client('sns')

# Crea un tópico SNS
response = sns.create_topic(Name='TopicoSNS')
topic_arn = response['TopicArn']
print(f"ARN del tópico SNS creado: {topic_arn}")
