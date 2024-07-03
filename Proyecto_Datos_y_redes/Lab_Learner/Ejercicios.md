# Ejercicios Prácticos con AWS Lab Learner

## Ejercicio 1: Configuración de Amazon SQS

### Objetivo
Configurar una cola de mensajes en Amazon SQS y enviar/recibir mensajes.

### Pasos
1. **Crear una Cola de SQS**:
    - Accede a la consola de Amazon SQS.
    - Crea una nueva cola con el nombre `MiColaSQS`.
2. **Enviar Mensajes a la Cola**:
    - Utiliza el siguiente script en Python para enviar mensajes a la cola:

    ```python
    import boto3

    # Configura el cliente de SQS
    sqs = boto3.client('sqs')

    # URL de la cola SQS
    queue_url = 'URL_DE_TU_COLA'

    # Enviar un mensaje
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody='Este es un mensaje de prueba.'
    )

    print(f'Mensaje enviado: {response["MessageId"]}')
    ```

3. **Recibir y Procesar Mensajes de la Cola**:
    - Utiliza el siguiente script en Python para recibir y procesar mensajes:

    ```python
    import boto3
    import time

    # Configura el cliente de SQS
    sqs = boto3.client('sqs')

    # URL de la cola SQS
    queue_url = 'URL_DE_TU_COLA'

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
    ```

## Ejercicio 2: Publicación y Suscripción con Amazon SNS

### Objetivo
Crear un tópico en Amazon SNS, suscribirse al tópico y publicar mensajes.

### Pasos
1. **Crear un Tópico en SNS**:
    - Accede a la consola de Amazon SNS.
    - Crea un nuevo tópico con el nombre `MiTópicoSNS`.

2. **Suscribirse al Tópico**:
    - Utiliza el siguiente script en Python para suscribirse al tópico:

    ```python
    import boto3

    # Configura el cliente de SNS
    sns = boto3.client('sns')

    # ARN del tópico SNS
    topic_arn = 'ARN_DE_TU_TOPICO'

    # Crear una suscripción
    response = sns.subscribe(
        TopicArn=topic_arn,
        Protocol='email',
        Endpoint='tu_correo@example.com'
    )

    print(f'Suscripción creada: {response["SubscriptionArn"]}')
    ```

3. **Publicar Mensajes en el Tópico**:
    - Utiliza el siguiente script en Python para publicar mensajes en el tópico:

    ```python
    import boto3

    # Configura el cliente de SNS
    sns = boto3.client('sns')

    # ARN del tópico SNS
    topic_arn = 'ARN_DE_TU_TOPICO'

    # Publicar un mensaje
    response = sns.publish(
        TopicArn=topic_arn,
        Message='Este es un mensaje de prueba.'
    )

    print(f'Mensaje publicado: {response["MessageId"]}')
    ```

## Ejercicio 3: Procesamiento de Datos en Tiempo Real con Kinesis

### Objetivo
Configurar un flujo de datos en Amazon Kinesis y procesar los datos en tiempo real.

### Pasos
1. **Crear un Stream de Kinesis**:
    - Accede a la consola de Amazon Kinesis.
    - Crea un nuevo stream con el nombre `MiStreamKinesis`.

2. **Enviar Datos al Stream**:
    - Utiliza el siguiente script en Python para enviar datos al stream:

    ```python
    import boto3
    import json

    # Configura el cliente de Kinesis
    kinesis = boto3.client('kinesis')

    # Nombre del stream de Kinesis
    stream_name = 'MiStreamKinesis'

    # Enviar datos al stream
    response = kinesis.put_record(
        StreamName=stream_name,
        Data=json.dumps({'mensaje': 'Este es un mensaje de prueba'}),
        PartitionKey='1'
    )

    print(f'Datos enviados: {response["SequenceNumber"]}')
    ```

3. **Procesar Datos del Stream**:
    - Utiliza el siguiente script en Python para procesar datos del stream:

    ```python
    import boto3

    # Configura el cliente de Kinesis
    kinesis = boto3.client('kinesis')

    # Nombre del stream de Kinesis
    stream_name = 'MiStreamKinesis'

    # Procesar datos del stream
    response = kinesis.get_shard_iterator(
        StreamName=stream_name,
        ShardId='shardId-000000000000',
        ShardIteratorType='LATEST'
    )

    shard_iterator = response['ShardIterator']

    while True:
        response = kinesis.get_records(
            ShardIterator=shard_iterator,
            Limit=1
        )

        if response['Records']:
            for record in response['Records']:
                print(f'Dato recibido: {record["Data"]}')
        else:
            print('No hay datos disponibles')

        shard_iterator = response['NextShardIterator']
    ```
