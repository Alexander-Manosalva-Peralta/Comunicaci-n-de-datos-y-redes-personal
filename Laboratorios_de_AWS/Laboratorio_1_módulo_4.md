# Laboratorio 1 del módulo 4: Lanzamiento de una instancia de EC2

## Información general sobre el laboratorio

En este laboratorio, crearás una instancia de Amazon Elastic Compute Cloud (Amazon EC2) que aloja un sitio web sencilplo.

## Tarea 1. Comenzar a crear la instancia y asignarle un nombre

Selecciona el menú **Servicios**, localiza los servicios de **Computación** y selecciona **EC2**.

![Seleccionar EC2](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/Ec1.png?raw=true)

Selecciona el botón **Lanzar instancia** en medio de la página y luego selecciona **Lanzar instancia** en el menú desplegable.

![Botón Lanzar instancia](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/Ec2.png)

Pon un nombre a la instancia:
Llámala **Web Server 1**

![Name](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/ec3.3.png)

## Tarea 2. Imágenes de aplicación y SO

Selecciona una AMI a partir de la cual crear la instancia:

En la lista de AMI disponibles de Quick Start, mantén la AMI predeterminada de Amazon Linux seleccionada.

Además, mantén seleccionada la Amazon Linux 2023 AMI x86_64 (HVM) predeterminada.

El tipo de imagen de máquina de Amazon (AMI) que selecciones determina el sistema operativo (SO) que se ejecutará en la instancia de EC2 que inicies. En este caso, has seleccionado Amazon Linux 2023 como SO invitado.

![Des](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/ec3.png?raw=true)

## Tarea 3. Elegir el tipo de instancia

Especifica un tipo de instancia:

En el panel Tipo de instancia, mantén el tipo predeterminado **t2.micro** seleccionado.

El Tipo de instancia define los recursos de hardware asignados a la instancia. Este tipo de instancia tiene 1 unidad de procesamiento central virtual (CPU) y 1 GiB de memoria.

![Des](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/ec4.png)

## Tarea 4. Seleccionar un par de claves

Selecciona el par de claves que quieras asociar con la instancia:

En el menú Nombre del par de claves, selecciona **vockey**.

El par de claves vockey que has seleccionado te permitirá conectarte a esta instancia mediante SSH después de que se haya iniciado. Aunque no tendrás que hacer eso en este laboratorio, sigue siendo necesario para identificar un par de claves existente, crear uno nuevo o al lanzar una instancia.

![Des](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/ec5.png)

## Tarea 5. Configuración de red

Junto a la configuración de red, selecciona **Editar**.

Mantén los ajustes predeterminados para VPC y subred. Mantén también el ajuste de Asignar automáticamente la IP pública como Habilitar.

La red indica la nube virtual privada (VPC) en la que quieres lanzar la instancia. Puede tener varias redes; por ejemplo, una para desarrollo, una segunda para pruebas y una tercera para producción.

En Firewall (grupos de seguridad), selecciona el valor predeterminado La opción **Crear grupo de seguridad** está seleccionada.

![Des](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/ec6.png?raw=true)

Configura un nuevo grupo de seguridad:

Mantén la selección predeterminada **Crear un nuevo grupo de seguridad**.

Nombre del grupo de seguridad: borra el texto e introduce **Web Server**

![Des](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/ec7.png?raw=true)

Descripción: borra el texto e introduce **Security group for my web server**

![Des](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/ec8.png?raw=true)

Selecciona **Eliminar** para eliminar la regla de entrada SSH predeterminada.

Un grupo de seguridad actúa como un firewall virtual que controla el tráfico de una o varias instancias. Cuando inicias una instancia, la asocias a uno o varios grupos de seguridad. Añades reglas a cada grupo de seguridad que permiten que el tráfico fluya a sus instancias asociadas o desde ellas. Las reglas de un grupo de seguridad se pueden modificar en cualquier momento. Las nuevas reglas se aplican automáticamente a todas las instancias que estén asociadas al grupo de seguridad.

## Tarea 6. Configurar el almacenamiento

En la sección Configurar almacenamiento, mantén la configuración predeterminada.

Iniciarás la instancia de Amazon EC2 usando un volumen predeterminado de disco de Elastic Block Store (EBS). Este será tu volumen raíz (denominado también volumen de arranque) que alojará el sistema operativo invitado de Amazon Linux 2023 que especificaste antes. Se ejecutará en un disco duro SSD de uso general (gp2) de 8 GiB de tamaño. Como alternativa, podrías añadir más volúmenes de almacenamiento, aunque eso no resulta necesario en este laboratorio.

![Des](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/ec9.png?raw=true)

## Tarea 7: Detalles avanzados

Configura un script para que se ejecute en la instancia cuando se inicie:

Expande el panel **Detalles avanzados**.

Desplázate hacia la parte inferior de la página y copia y pega el código que se muestra a continuación en la casilla **Datos de usuario**:

```
yum update -y
yum -y install httpd
systemctl enable httpd
systemctl start httpd
echo '<html><h1>Hello World!</h1></html>' > /var/www/html/index.html
```
![Des](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/ec10.png?raw=true)

## Tarea 8: Revisar la instancia y lanzarla

En la parte inferior del panel **Resumen** en la parte derecha de la pantalla, selecciona **Lanzar instancia**

![Des](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/ec11.png?raw=true)

Verás un mensaje de éxito.
Selecciona **Ver todas las instancias**

![Des](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/ec12.png?raw=true)

La instancia aparecerá primero en estado **Pendiente**, que significa que se está lanzando. Después, el estado cambiará a **En ejecución**, lo que indica que la instancia se ha iniciado. La instancia tarda unos minutos en arrancar.
Selecciona la instancia **Web Server 1** y revisa la información de la pestaña **Detalles** que se muestra en el panel inferior.

![Des](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/ec13.png?raw=true)

Observa que la instancia tiene una dirección DNS de IPv4 pública. Puedes utilizar esta dirección IP para comunicarte con la instancia desde Internet.

Antes de continuar, espera a que la instancia muestre lo siguiente:

- Estado de la instancia: **En ejecución**
- Comprobación de estado: **2/2 comprobaciones superadas**

Es posible que esto tarde unos minutos. Selecciona el icono de actualización en la parte superior de la página cada 30 segundos para informarte más rápidamente del último estado de la instancia.

![Des](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/ec14.png?raw=true)

## Tarea 9: Acceder a la instancia de EC2

Cuando lanzaste la instancia de EC2, proporcionaste un script que instaló un servidor web y creó una página web sencilla. En esta tarea, intentarás acceder al contenido desde el servidor web.

En la pestaña **Detalles**, copia el valor de la **Dirección IPv4 pública** de la instancia en el portapapeles.

![Des](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/ec15.png?raw=true)

## Tarea 10: Actualizar el grupo de seguridad

No puedes acceder al servidor web porque el grupo de seguridad no permite el tráfico entrante en el puerto 80, que se utiliza para las solicitudes web HTTP. En esta tarea, actualizarás el grupo de seguridad.

![Des](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/ec16.png?raw=true)

Vuelve a la pestaña del navegador de la Consola de administración de EC2.
En el panel de navegación izquierdo, en **Red y seguridad**, selecciona **Grupos de seguridad**
Selecciona el grupo de seguridad **Web Server** que creaste al lanzar la instancia de EC2.

![Des](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/ec17.png?raw=true)

En el panel inferior, selecciona la pestaña **Reglas de entrada**.

![Des](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/ec18.png?raw=true)

## Tarea 11: Crear una regla de entrada

Selecciona **Editar reglas de entrada** y, a continuación, selecciona **Añadir regla**.

![Des](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/ec19.png?raw=true)

Configura lo siguiente:

- Tipo: **HTTP**
- Fuente: **Cualquier lugar-IPv4**

Selecciona **Guardar reglas**

![Des](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/ec19.png?raw=true)

La nueva regla HTTP de entrada crea una entrada para las direcciones IP IPv4 IP (0.0.0.0/0) y IPv6 (::/0).

## Tarea 12: Probar la regla

Vuelve a la pestaña que utilizaste para intentar conectarte al servidor web.
Actualiza la página.
Debería mostrar la página del servidor web con el mensaje Hello World!

![DDes](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/ec21.png?raw=true)

## Laboratorio completado

¡Enhorabuena! Has completado el laboratorio.
