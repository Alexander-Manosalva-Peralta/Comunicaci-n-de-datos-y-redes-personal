# Desarrollo de problemas y codigo

##  En la gestión de proyectos, el proceso de Definir el Alcance es crucial para establecer los límites, entregables y criterios de éxito del proyecto. Una definición clara del alcance garantiza que todos los interesados ​​comprendan qué se incluye y qué queda fuera del proyecto. En esta presentación, exploraremos en detalle este proceso fundamental y su importancia en el éxito del proyecto.

Conceptos: Cliente, Servidor, Protocolo, TCP/IP

Escribe una función en Python que simule la comunicación entre un cliente y un servidor usando la programación funcional. El cliente debería ser capaz de enviar mensajes y el servidor de responder de acuerdo con un protocolo simple (por ejemplo, eco, reverso del mensaje, etc.).

- Implementa funciones separadas para el comportamiento del cliente y del servidor.
- Simula el envío y recepción de mensajes.
- Aplica conceptos de TCP/IP en un contexto abstracto.

### Respuestas dadas por el docente:

*Paso 1: Definir las funciones del servidor:*

```
def servidor(mensaje):
    """Procesa los mensajes enviados por el cliente según el comando especifico."""
    comando, _, contenido = mensaje.partition(':')
    if comando.strip().lower() == 'eco':
        return contenido.strip() 
    elif comando.strip().lower() == 'reverso':
        return contenido.strip()[::-1]
    else:
        return "Comando no reconocido."
```
El servidor debe ser capaz de interpretar el mensaje recibido y responder de acuerdo a un comando especificado en el mensaje.

*Paso 2: Definir el cliente*    

``` 
def cliente(mensaje):
    """Envia mensajes al servidor y procesa la respuesta."""
    respuesta = servidor(mensaje)
    print(f"Servidor dice: {respuesta}")
```

