# Laboratorio del módulo 6: Asociar un volumen de EBS

## Información general sobre el laboratorio
En este laboratorio, crearás una instancia de Amazon Elastic Compute Cloud (Amazon EC2) y, a continuación, le adjuntarás un volumen de Amazon Elastic Block Store (Amazon EBS)

## Tarea 1. Comenzar a crear la instancia y asignarle un nombre

1. Selecciona el menú **Servicios**, localiza los servicios de **Computación** y selecciona **EC2**.

![mod6_1](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/mod6_1.png)

2. Selecciona el botón **Lanzar instancia** en medio de la página y luego selecciona **Lanzar instancia** en el menú desplegable.
3. Pon un nombre a la instancia:
   - Llámala `Web Server`

![mod6_2](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/mod6_2.png)

## Tarea 2. Imágenes de aplicación y SO
1. Selecciona una AMI a partir de la cual crear la instancia:
   - En la lista de AMI disponibles de **Quick Start**, mantén la AMI predeterminada de **Amazon Linux** seleccionada.
   - Además, mantén seleccionada la **Amazon Linux 2023 AMI x86_64 (HVM)** predeterminada.

![mod6_3](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/mod6_3.png)

El tipo de imagen de máquina de Amazon (AMI) que selecciones determina el sistema operativo (SO) que se ejecutará en la instancia de EC2 que inicies. En este caso, has seleccionado **Amazon Linux 2023** como SO invitado.

## Tarea 3. Elegir el tipo de instancia
1. Especifica un tipo de instancia:
   - En el panel **Tipo de instancia**, mantén el tipo predeterminado `t2.micro` seleccionado.

![mod6_4](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/mod6_4.png)

El Tipo de instancia define los recursos de hardware asignados a la instancia. Este tipo de instancia tiene 1 unidad de procesamiento central virtual (CPU) y 1 GiB de memoria.

## Tarea 4. Seleccionar un par de claves
1. Selecciona el par de claves que quieras asociar con la instancia:
   - En el menú **Nombre del par de claves**, selecciona `vockey`.

![mod6_5](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/mod6_5.png)

El par de claves `vockey` que has seleccionado te permitirá conectarte a esta instancia mediante SSH después de que se haya iniciado. Aunque no tendrás que hacer eso en este laboratorio, sigue siendo necesario para identificar un par de claves existente, crear uno nuevo o al lanzar una instancia.

## Tarea 5. Configuración de red
1. Junto a la configuración de red, selecciona **Editar**.
2. Mantén los ajustes predeterminados para **VPC** y **subred**. Mantén también el ajuste de **Asignar automáticamente la IP pública** como **Habilitar**.
3. En **Firewall (grupos de seguridad)**, selecciona el valor predeterminado:
   - La opción **Crear grupo de seguridad** está seleccionada.

![mod6_6](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/mod6_6.png)

4. Configura un nuevo grupo de seguridad:
   - Mantén la selección predeterminada **Crear un nuevo grupo de seguridad**.
   - **Nombre del grupo de seguridad:** borra el texto e introduce `Web Server`.
   - **Descripción:** borra el texto e introduce `Security group for my web server`.

5. Selecciona **Eliminar** para eliminar la regla de entrada SSH predeterminada.

![mod6_7](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/mod6_7.png)

## Tarea 6. Configurar el almacenamiento
1. En la sección **Configurar almacenamiento**, mantén la configuración predeterminada.

![mod6_8](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/mod6_8.png)

Iniciarás la instancia de Amazon EC2 usando un volumen predeterminado de disco de Elastic Block Store (EBS). Este será tu volumen raíz (denominado también volumen de arranque) que alojará el sistema operativo invitado de Amazon Linux 2023 que especificaste antes. Se ejecutará en un disco duro SSD de uso general (gp2) de 8 GiB de tamaño. Como alternativa, podrías añadir más volúmenes de almacenamiento, aunque eso no resulta necesario en este laboratorio.

## Tarea 7: Detalles avanzados
1. Configura un script para que se ejecute en la instancia cuando se inicie:
   - Expande el panel **Detalles avanzados**.
   - Desplázate hacia la parte inferior de la página y copia y pega el siguiente código en la casilla **Datos de usuario**:

```
yum update -y
yum -y install httpd
systemctl enable httpd
systemctl start httpd
echo '<html><h1>Hello World!</h1></html>' > /var/www/html/index.htmL
```

![mod6_9](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/mod6_9.png)

Este script bash se ejecutará sin permisos de usuario raíz en el SO invitado de la instancia. Se ejecutará automáticamente cuando la instancia se inicie por primera vez. Este script hace lo siguiente:

- Actualiza el servidor
- Instala un servidor web Apache (httpd)
- Configura el servidor web para que comience automáticamente durante el arranque
- Activa el servidor web
- Crea una página web sencilla

## Tarea 8: Revisar la instancia y lanzarla

1. En la parte inferior del panel Resumen en la parte derecha de la pantalla, selecciona **Lanzar instancia**.

![mod6_10](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/mod6_10.png)

2. Verás un mensaje de éxito.

![mod6_11](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/mod6_11.png)

3. Selecciona **Ver todas las instancias**.
4. La instancia aparecerá primero en estado **Pendiente**, que significa que se está lanzando. Después, el estado cambiará a **En ejecución**, lo que indica que la instancia se ha iniciado. La instancia tarda unos minutos en arrancar.
5. Selecciona la instancia **Web Server** y revisa la información de la pestaña **Detalles** que se muestra en el panel inferior.
6. Observa que la instancia tiene una dirección DNS de IPv4 pública. Puedes utilizar esta dirección IP para comunicarte con la instancia desde Internet.

Antes de continuar, espera a que la instancia muestre lo siguiente:

- **Estado de la instancia**: En ejecución
- **Comprobación de estado**: 2/2 comprobaciones superadas

![mod6_12](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/mod6_12.png)

## Tarea 9. Acceder a la instancia de EC2

1. Cuando lanzaste la instancia de EC2, proporcionaste un script que instaló un servidor web y creó una página web sencilla. En esta tarea, intentarás acceder al contenido desde el servidor web.
2. En la pestaña **Detalles**, copia el valor de la **Dirección IPv4 pública** de la instancia en el portapapeles.

![mod6_13](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/mod6_13.png)

> **Nota**: Una dirección pública significa que se puede acceder a la instancia desde Internet. Cada instancia que recibe una dirección IP pública también recibe un nombre de host DNS externo: por ejemplo, `ec2-xxx-xxx-xxx-xxx.compute-1.amazonaws.com`. AWS resuelve un nombre de host DNS externo en la dirección IP pública de la instancia cuando la comunicación proviene de fuera de su VPC. Cuando la comunicación proviene de dentro de su VPC, el nombre de host DNS se resuelve en la dirección IPv4 privada.

3. Abre una nueva pestaña en el navegador web, pega la dirección IP pública que acabas de copiar y, a continuación, pulsa **Intro**.
4. La página web no se carga. Debes actualizar el grupo de seguridad para poder acceder a la página.

![mod6_14](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/mod6_14.png)

## Tarea 10. Actualizar el grupo de seguridad

No puedes acceder al servidor web porque el grupo de seguridad no permite el tráfico entrante en el puerto 80, que se utiliza para las solicitudes web HTTP. En esta tarea, actualizarás el grupo de seguridad.

1. Vuelve a la pestaña del navegador de la **Consola de administración de EC2**.
2. En el panel de navegación izquierdo, en **Red y seguridad**, selecciona **Grupos de seguridad**.
3. Selecciona el grupo de seguridad **Web Server** que creaste al lanzar la instancia de EC2.
4. En el panel inferior, selecciona la pestaña **Reglas de entrada**

![mod6_15](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/mod6_15.png)

## Tarea 11: Crear una regla de entrada

1. Selecciona **Editar reglas de entrada** y, a continuación, selecciona **Añadir regla**.

![mod6_16](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/mod6_16.png)

2. Configura lo siguiente:
    - **Tipo**: HTTP
    - **Fuente**: Cualquier lugar-IPv4
3. Selecciona **Guardar reglas**.

![mod6_17](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/mod6_17.png)

La nueva regla HTTP de entrada crea una entrada para las direcciones IP IPv4 IP (0.0.0.0/0) y IPv6 (::/0).

## Tarea 12. Probar la regla

1. Vuelve a la pestaña que utilizaste para intentar conectarte al servidor web.
2. Actualiza la página.

![mod6_18](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/mod6_18.png)

Debería mostrar la página del servidor web con el mensaje **Hello World!**

## Tarea 13: Adjuntar un volumen de EBS a la instancia de EC2

1. Vuelve a la pestaña del navegador de la **Consola de administración de EC2**.
2. En el panel de navegación izquierdo, en **Instancias**, selecciona **Instancias**.
3. Selecciona la instancia **Web Server** y, en la pestaña **Redes** que aparece debajo, toma nota de la **Zona de disponibilidad** en la que se ejecuta la instancia.
    - El volumen de EBS que vas a crear pronto tendrá que estar en la misma zona de disponibilidad.

![mod6_19](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/mod6_19.png)

4. En el panel de navegación izquierdo, en **Elastic Block Store**, selecciona **Volúmenes**.
5. Selecciona **Crear volumen**.

![mod6_20](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/mod6_20.png)

6. En **Tamaño**, introduce 1 para crear un volumen con 1 GiB.

![mod6_21](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/mod6_21.png)

7. En **Zona de disponibilidad**, selecciona la misma zona de disponibilidad en la que se ejecuta la instancia de EC2.
8. Desplázate hacia abajo y selecciona **Crear volumen**.
    - El nuevo volumen aparece en la lista de volúmenes con el estado **Disponible**.

![mod6_22](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/mod6_21.png)

9. Selecciona el nuevo volumen con un tamaño de 1 GiB. A continuación, elige **Acciones** y **Asociar volumen**.
10. Selecciona el menú desplegable **Instancia** y selecciona tu instancia de EC2. La lista de instancias se rellenará automáticamente.

![mod6_23](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/mod6_23.png)

11. Selecciona **Asociar volumen**.

![mod6_24](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/mod6_24.png)

El estado del volumen cambia a **en uso**. El nuevo volumen se ha adjuntado a la instancia de EC2.

## Laboratorio completado

¡Enhorabuena! Has completado el laboratorio.
