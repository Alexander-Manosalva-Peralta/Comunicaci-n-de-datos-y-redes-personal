import boto3
import json
import time
import threading
from botocore.exceptions import ClientError

def crear_flujo_datos_kinesis(nombre_flujo, numero_fragmentos):
    kinesis = boto3.client('kinesis')
    try:
        response = kinesis.create_stream(
            StreamName=nombre_flujo,
            ShardCount=numero_fragmentos
        )
        print(f"Flujo de datos '{nombre_flujo}' creado con éxito.")
        return response
    except Exception as e:
        print(f"Error al crear el flujo de datos en Kinesis: {e}")
        return None

def productor_datos(datos, stream_name):
    kinesis = boto3.client('kinesis')
    while True:
        response = kinesis.put_record(
            StreamName=stream_name,
            Data=json.dumps(datos),
            PartitionKey='partition_key'
        )
        print(f"Registro enviado: {response['SequenceNumber']}")
        time.sleep(1)  # Intervalo de tiempo entre envíos (1 segundo en este ejemplo)

def consumidor_datos(stream_name):
    kinesis = boto3.client('kinesis')
    try:
        response = kinesis.describe_stream(StreamName=stream_name)
        shard_id = response['StreamDescription']['Shards'][0]['ShardId']
        
        shard_iterator = kinesis.get_shard_iterator(
            StreamName=stream_name,
            ShardId=shard_id,
            ShardIteratorType='LATEST'
        )['ShardIterator']
        
        while True:
            record_response = kinesis.get_records(ShardIterator=shard_iterator, Limit=2)
            shard_iterator = record_response['NextShardIterator']
            records = record_response['Records']
            for record in records:
                data = json.loads(record['Data'])
                print(f"Datos recibidos: {data}")
            time.sleep(1)
    except ClientError as e:
        print(f"Error al consumir datos de Kinesis: {e}")

# Nombre y número de fragmentos del flujo de datos
nombre_flujo = 'FlujoDeDatos'
numero_fragmentos = 2  # Puedes ajustar según tus necesidades

# Crear el flujo de datos en Amazon Kinesis
stream = crear_flujo_datos_kinesis(nombre_flujo, numero_fragmentos)
if stream is not None:
    status_code = stream['ResponseMetadata']['HTTPStatusCode']
    if status_code == 200:
        print(f"Flujo de datos '{nombre_flujo}' creado correctamente.")
    else:
        print(f"Hubo un problema al crear el flujo de datos '{nombre_flujo}'.")
        
# Datos a enviar
data = {'campo1': 'valor1', 'campo2': 'valor2'}

# Iniciar productor en un hilo separado
productor_thread = threading.Thread(target=productor_datos, args=(data, nombre_flujo))
productor_thread.start()
        
# Iniciar consumidor en un hilo separado
consumidor_thread = threading.Thread(target=consumidor_datos, args=(nombre_flujo,))
consumidor_thread.start()
        
productor_thread.join()
consumidor_thread.join()
