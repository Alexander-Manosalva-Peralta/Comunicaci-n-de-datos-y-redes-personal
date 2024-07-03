import boto3

# Configura el cliente de SQS
sqs = boto3.client('sqs')

# Nombre y configuración de las colas SQS
queue_configs = [
    {
        'QueueName': 'MiColaSQS3',
        'Attributes': {
            'VisibilityTimeout': '45',    # Tiempo de visibilidad en segundos
            'MessageRetentionPeriod': '172800'  # Retención de mensajes en segundos (2 días)
        }
    },
    {
        'QueueName': 'MiColaSQS4',
        'Attributes': {
            'VisibilityTimeout': '30',    # Tiempo de visibilidad en segundos
            'MessageRetentionPeriod': '86400'  # Retención de mensajes en segundos (1 día)
        }
    },
    {
        'QueueName': 'MiColaSQS5',
        'Attributes': {
            'VisibilityTimeout': '60',    # Tiempo de visibilidad en segundos
            'MessageRetentionPeriod': '43200'  # Retención de mensajes en segundos (12 horas)
        }
    },
    {
        'QueueName': 'MiColaSQS6',
        'Attributes': {
            'VisibilityTimeout': '40',    # Tiempo de visibilidad en segundos
            'MessageRetentionPeriod': '129600'  # Retención de mensajes en segundos (1.5 días)
        }
    },
    {
        'QueueName': 'MiColaSQS7',
        'Attributes': {
            'VisibilityTimeout': '55',    # Tiempo de visibilidad en segundos
            'MessageRetentionPeriod': '259200'  # Retención de mensajes en segundos (3 días)
        }
    }
]

# Crear las colas
for queue_config in queue_configs:
    response = sqs.create_queue(
        QueueName=queue_config['QueueName'],
        Attributes=queue_config['Attributes']
    )
    print(f"Cola creada: {response['QueueUrl']}")

