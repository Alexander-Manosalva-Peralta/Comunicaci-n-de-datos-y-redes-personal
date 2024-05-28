# Laboratorio 1 del Módulo 4: Lanzamiento de una Instancia de EC2

## Información General sobre el Laboratorio

En este laboratorio, crearás una instancia de Amazon Elastic Compute Cloud (Amazon EC2) que aloja un sitio web sencillo.

### Duración

El tiempo estimado para completar este laboratorio es de 30 minutos.

### Acceso a la Consola de Administración de AWS

Para comenzar la sesión de laboratorio, selecciona **Start Lab (Iniciar laboratorio)** en la esquina superior derecha de la página.

1. Comienza la sesión del laboratorio.
2. En la esquina superior derecha de esta página aparece un temporizador que muestra el tiempo que queda de la sesión.

**Sugerencia:** Para actualizar la duración de la sesión en cualquier momento, vuelve a seleccionar **Start Lab (Iniciar laboratorio)** antes de que el temporizador llegue a 0:00.

Antes de continuar, espera hasta que el entorno de laboratorio esté listo. El entorno está listo cuando aparecen los detalles del laboratorio en el lado derecho de la página y el icono del círculo junto al enlace de AWS en la esquina superior izquierda pasa a ser verde.

Para volver a estas instrucciones, selecciona el enlace **Readme (Léeme)** en la esquina superior derecha.

Para conectarte a la consola de administración de AWS, selecciona el enlace de AWS en la esquina superior izquierda, encima de la ventana del terminal. Se abrirá una nueva pestaña del navegador que te conecta a la consola de administración de AWS.

**Sugerencia:** Si no se abre una pestaña nueva del navegador, generalmente aparece un banner o un icono en la parte superior de este, el cual indica que el navegador no permite que se abran ventanas emergentes en el sitio. Elige el banner o el icono y, a continuación, selecciona **Permitir elementos emergentes**.

## Tarea 1. Comenzar a Crear la Instancia y Asignarle un Nombre

Selecciona el menú **Servicios**, localiza los servicios de Computación y selecciona **EC2**.

Selecciona el botón **Lanzar instancia** en medio de la página y luego selecciona **Lanzar instancia** en el menú desplegable.

Pon un nombre a la instancia:
- Llámala **Web Server 1**

Las etiquetas te permiten clasificar los recursos de AWS de diferentes maneras: por ejemplo, por finalidad, propietario o entorno. Esto es útil cuando tienes muchos recursos del mismo tipo: puedes identificar rápidamente un recurso específico en función de las etiquetas que le hayas asignado. Cada etiqueta consta de una clave y un valor, que tú defines.

**Nota:** Name es otra etiqueta diferente. La clave de esta etiqueta es **Name** y el valor es **Web Server 1**.

## Tarea 2. Imágenes de Aplicación y SO

Selecciona una AMI a partir de la cual crear la instancia:
- En la lista de AMI disponibles de **Quick Start**, mantén la AMI predeterminada de **Amazon Linux** seleccionada.
- Además, mantén seleccionada la **Amazon Linux 2023 AMI x86_64 (HVM)** predeterminada.

El tipo de imagen de máquina de Amazon (AMI) que selecciones determina el sistema operativo (SO) que se ejecutará en la instancia de EC2 que inicies. En este caso, has seleccionado **Amazon Linux 2023** como SO invitado.

## Tarea 3. Elegir el Tipo de Instancia

Especifica un tipo de instancia:
- En el panel **Tipo de instancia**, mantén el tipo predeterminado **t2.micro** seleccionado.

El tipo de instancia define los recursos de hardware asignados a la instancia. Este tipo de instancia tiene 1 unidad de procesamiento central virtual (CPU) y 1 GiB de memoria.

## Tarea 4. Seleccionar un Par de Claves

Selecciona el par de claves que quieras asociar con la instancia:
- En el menú **Nombre del par de claves**, selecciona **vockey**.

El par de claves **vockey** que has seleccionado te permitirá conectarte a esta instancia mediante SSH después de que se haya iniciado. Aunque no tendrás que hacer eso en este laboratorio, sigue siendo necesario para identificar un par de claves existente, crear uno nuevo o al lanzar una instancia.

## Tarea 5. Configuración de Red

Junto a la configuración de red, selecciona **Editar**.

Mantén los ajustes predeterminados para VPC y subred. Mantén también el ajuste de **Asignar automáticamente la IP pública** como **Habilitar**.

La red indica la nube virtual privada (VPC) en la que quieres lanzar la instancia. Puede tener varias redes; por ejemplo, una para desarrollo, una segunda para pruebas y una tercera para producción.

En **Firewall (grupos de seguridad)**, selecciona el valor predeterminado **Crear grupo de seguridad**.

Configura un nuevo grupo de seguridad:
- Mantén la selección predeterminada **Crear un nuevo grupo de seguridad**.
- **Nombre del grupo de seguridad:** borra el texto e introduce **Web Server**
- **Descripción:** borra el texto e introduce **Security group for my web server**
- Selecciona **Eliminar** para eliminar la regla de entrada SSH predeterminada.

**Nota:** Vas a configurar una regla de entrada diferente más adelante en este laboratorio.

Un grupo de seguridad actúa como un firewall virtual que controla el tráfico de una o varias instancias. Cuando inicias una instancia, la asocias a uno o varios grupos de seguridad. Añades reglas a cada grupo de seguridad que permiten que el tráfico fluya a sus instancias asociadas o desde ellas. Las reglas de un grupo de seguridad se pueden modificar en cualquier momento. Las nuevas reglas se aplican automáticamente a todas las instancias que estén asociadas al grupo de seguridad.

## Tarea 6. Configurar el Almacenamiento

En la sección **Configurar almacenamiento**, mantén la configuración predeterminada.

Iniciarás la instancia de Amazon EC2 usando un volumen predeterminado de disco de Elastic Block Store (EBS). Este será tu volumen raíz (denominado también volumen de arranque) que alojará el sistema operativo invitado de Amazon Linux 2023 que especificaste antes. Se ejecutará en un disco duro SSD de uso general (gp2) de 8 GiB de tamaño. Como alternativa, podrías añadir más volúmenes de almacenamiento, aunque eso no resulta necesario en este laboratorio.

## Tarea 7. Detalles Avanzados

Configura un script para que se ejecute en la instancia cuando se inicie:

1. Expande el panel **Detalles avanzados**.
2. Desplázate hacia la parte inferior de la página y copia y pega el código que se muestra a continuación en la casilla **Datos de usuario**:

    ```bash
    #!/bin/bash
    yum update -y
    yum -y install httpd
    systemctl enable httpd
    systemctl start httpd
    echo '<html><h1>Hello World!</h1></html>' > /var/www/html/index.html
    ```

Este script bash se ejecutará sin permisos de usuario raíz en el SO invitado de la instancia. Se ejecutará automáticamente cuando la instancia se inicie por primera vez. Este script hace lo siguiente:
- Actualiza el servidor.
- Instala un servidor web Apache (httpd).
- Configura el servidor web para que comience automáticamente durante el arranque.
- Activa el servidor web.
- Crea una página web sencilla.

## Tarea 8. Revisar la Instancia y Lanzarla

En la parte inferior del panel **Resumen** en la parte derecha de la pantalla, selecciona **Lanzar instancia**.

Verás un mensaje de éxito.

Selecciona **Ver todas las instancias**.

La instancia aparecerá primero en estado **Pendiente**, que significa que se está lanzando. Después, el estado cambiará a **En ejecución**, lo que indica que la instancia se ha iniciado. La instancia tarda unos minutos en arrancar.

Selecciona la instancia **Web Server 1** y revisa la información de la pestaña **Detalles** que se muestra en el panel inferior.

Observa que la instancia tiene una dirección DNS de IPv4 pública. Puedes utilizar esta dirección IP para comunicarte con la instancia desde Internet.

Antes de continuar, espera a que la instancia muestre lo siguiente:
- **Estado de la instancia:** En ejecución.
- **Comprobación de estado:** 2/2 comprobaciones superadas.

Es posible que esto tarde unos minutos. Selecciona el icono de actualización en la parte superior de la página cada 30 segundos para informarte más rápidamente del último estado de la instancia.

## Tarea 9. Acceder a la Instancia de EC2

Cuando lanzaste la instancia de EC2, proporcionaste un script que instaló un servidor web y creó una página web sencilla. En esta tarea, intentarás acceder al contenido desde el servidor web.

1. En la pestaña **Detalles**, copia el valor de la **Dirección IPv4 pública** de la instancia en el portapapeles.

**Nota:** Una dirección pública significa que se puede acceder a la instancia desde Internet. Cada instancia que recibe una dirección IP pública también recibe un nombre de host DNS externo: por ejemplo, ec2-xxx-xxx-xxx-xxx.compute-1.amazonaws.com. AWS resuelve un nombre de host DNS externo en la dirección IP pública de la instancia cuando se la comunicación proviene de fuera de su VPC. Cuando la comunicación proviene de dentro de su VPC, el nombre de host DNS se resuelve en la dirección IPv4 privada.

2. Abre una nueva pestaña en el navegador web, pega la dirección IP pública que acabas de copiar y, a continuación, pulsa **Intro**.

La página web no se carga. Debes actualizar el grupo de seguridad para poder acceder a la página.

## Tarea 10. Actualizar el Grupo de Seguridad

No puedes acceder al servidor web porque el grupo de seguridad no permite el tráfico entrante en el puerto 80, que se utiliza para las solicitudes web HTTP. En esta tarea, actualizarás el grupo de seguridad.

1. Vuelve a la pestaña del navegador de la **Consola de administración de EC2**.
2. En el panel de navegación izquierdo, en **Red y seguridad**, selecciona **Grupos de seguridad**.
3. Selecciona el grupo de seguridad **Web Server** que creaste al lanzar la instancia de EC2.
4. En el panel inferior, selecciona la pestaña **Reglas de entrada**.

## Tarea 11. Crear una Regla de Entrada

1. Selecciona **Editar reglas de entrada** y, a continuación, selecciona **Añadir regla**.
2. Configura lo siguiente:
    - **Tipo:** HTTP
    - **Fuente:** Cualquier lugar-IPv4
3. Selecciona **Guardar reglas**.

La nueva regla HTTP de entrada crea una entrada para las direcciones IP IPv4 (0.0.0.0/0) y IPv6 (::/0).

## Tarea 12. Probar la Regla

1. Vuelve a la pestaña que utilizaste para intentar conectarte al servidor web.
2. Actualiza la página.

Debería mostrar la página del servidor web con el mensaje **Hello World!**

## Laboratorio Completado

¡Enhorabuena! Has completado el laboratorio.

1. Cierra la sesión de la consola de administración de AWS.
    - En la esquina superior derecha de la página, elige tu nombre de usuario. Tu nombre de usuario comienza por **voclabs/user**.
    - Selecciona **Cerrar sesión**.
2. Selecciona **Finalizar laboratorio** en la parte superior de esta página y, a continuación, selecciona **Sí** para confirmar que quieres dar por concluido el laboratorio.
