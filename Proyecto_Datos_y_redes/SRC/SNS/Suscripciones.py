#Suscribe diferentes tipos de usuarios, como gmail o HTTPS

import boto3 from botocore.exceptions import ClientError

# Configura el cliente de SNS
sns = boto3.client('sns')

# ARN del tópico (reemplaza 'arn_del_topico' con el ARN real)
topic_arn = 'arn:aws:sns:us-east-1:105371261454:MiTopicoSNS'

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
        Endpoint='https://eook9az39jyzqwe.m.pipedream.net/' 
    )
    print(f"Suscripción por HTTP/HTTPS creada: {response['SubscriptionArn']}")
except ClientError as e:
    print(f"Error al crear la suscripción por HTTP/HTTPS: {e}")
