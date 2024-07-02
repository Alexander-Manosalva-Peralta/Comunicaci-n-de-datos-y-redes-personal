# Proyecto en AWS Cloud9: Sistema de Mensajería con SQS, SNS y Kinesis

## Descripción del Proyecto

Este proyecto utiliza servicios de AWS (Amazon SQS, SNS y Kinesis) para implementar un sistema de mensajería asincrónica y procesamiento de datos en tiempo real.

## Estructura del Repositorio

El repositorio está organizado de la siguiente manera:

| Carpeta / Archivo        | Descripción                                             |
|--------------------------|---------------------------------------------------------|
| `AWS_SQS/`               | Scripts y archivos relacionados con Amazon SQS          |
| `AWS_SNS/`               | Scripts y archivos relacionados con Amazon SNS          |
| `AWS_Kinesis/`           | Scripts y archivos relacionados con Amazon Kinesis      |
| `README.md`              | Documentación principal del proyecto (este archivo)     |

## Configuración del Entorno Cloud9

### Requisitos Previos

- Cuenta de AWS con acceso a AWS Cloud9.
- Permisos adecuados para utilizar Amazon SQS, SNS y Kinesis.

### Instrucciones para Configurar el Entorno

1. **Crear un Entorno Cloud9:**
   - Inicia sesión en la [Consola de AWS](https://aws.amazon.com/console/).
   - Navega a Cloud9 y crea un nuevo entorno basado en EC2.

2. **Configurar AWS CLI:**
   - Configura AWS CLI en tu entorno Cloud9 con las credenciales adecuadas.

## Ejecución del Proyecto

### Ejercicio 1: Configuración de Amazon SQS

1. **Crear Colas en Amazon SQS:**
   - Utiliza los scripts proporcionados en `AWS_SQS/crear_colas.py` para crear varias colas con diferentes configuraciones.

2. **Enviar y Leer Mensajes:**
   - Ejecuta `AWS_SQS/productor.py` para enviar mensajes a las colas.
   - Ejecuta `AWS_SQS/consumidor.py` para leer y procesar mensajes desde las colas.

### Ejercicio 2: Configuración de Amazon SNS

1. **Crear Tópicos en Amazon SNS:**
   - Utiliza `AWS_SNS/sns_crear_topico.py` para crear tópicos de SNS.

2. **Gestionar Suscripciones:**
   - Usa `AWS_SNS/sns_suscripcion.py` para configurar suscripciones a los tópicos.

### Ejercicio 3: Integración de SQS y SNS

1. **Configurar Mensajería entre SQS y SNS:**
   - Modifica `AWS_SQS/consumidor.py` para integrar la recepción de mensajes desde tópicos de SNS.

### Ejercicio 4: Configuración de Amazon Kinesis

1. **Crear Flujos de Datos en Amazon Kinesis:**
   - Utiliza `AWS_Kinesis/kinesis_flujo_datos.py` para configurar y enviar datos a flujos de Kinesis.

2. **Procesamiento en Tiempo Real:**
   - Implementa productores y consumidores en `AWS_Kinesis/kinesis_productor.py` y `AWS_Kinesis/kinesis_consumidor.py`.

## Colaboración y Contribución

- Si deseas colaborar en este proyecto, comparte el entorno Cloud9 con los usuarios adecuados desde la interfaz de Cloud9.
- Contribuye mejorando la documentación, corrigiendo errores o implementando nuevas funcionalidades.

## Soporte

Si tienes alguna pregunta o problema técnico, no dudes en abrir un issue en este repositorio o contactar al equipo de desarrollo.
