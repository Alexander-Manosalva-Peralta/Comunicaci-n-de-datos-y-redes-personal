#Se crea un tópico, que es aquel que agrupa a todos los susccriptores interesados

import boto3
from botocore.exceptions import ClientError

# Configura el cliente de SNS
sns = boto3.client('sns')

# Intenta crear el tópico
try:
    response = sns.create_topic(Name='MiTopicoSNS')
    print(f"Tópico creado: {response['TopicArn']}")
except ClientError as e:
    print(f"Error al crear el tópico: {e}")
