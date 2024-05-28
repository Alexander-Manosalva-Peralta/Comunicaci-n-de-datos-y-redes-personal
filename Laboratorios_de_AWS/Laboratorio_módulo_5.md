# Laboratorio del Módulo 5: Uso de CloudFront como CDN para un Sitio Web

## Información General sobre el Laboratorio

En este laboratorio, utilizarás Amazon CloudFront como red de entrega de contenido (CDN) para un sitio web almacenado en Amazon Simple Storage Service (Amazon S3).

### Duración

El tiempo estimado para completar este laboratorio es de 40 minutos.

### Acceso a la Consola de Administración de AWS

Para comenzar la sesión de laboratorio, elige **Start Lab (Iniciar laboratorio)** en la esquina superior derecha de la página.

1. Comienza la sesión del laboratorio.
2. En la esquina superior derecha de esta página aparece un temporizador que muestra el tiempo que queda de la sesión.

**Consejo:** Para actualizar la duración de la sesión en cualquier momento, vuelve a seleccionar **Start Lab (Iniciar laboratorio)** antes de que el temporizador llegue a 0:00.

Antes de continuar, espera hasta que el entorno de laboratorio esté listo. El entorno está listo cuando aparecen los detalles del laboratorio en el lado derecho de la página y el icono del círculo junto al enlace de AWS en la esquina superior izquierda pasa a ser verde.

Para volver a estas instrucciones, elige el enlace **Readme (Léeme)** en la esquina superior derecha.

Para conectarte a la consola de administración de AWS, selecciona el enlace de AWS situado en la esquina superior izquierda, sobre la ventana del terminal.

Se abre una nueva pestaña del navegador que te conecta a la consola de administración de AWS.

**Consejo:** Si no se abre una nueva pestaña del navegador, es posible que haya un banner o un icono en la parte superior del navegador con un mensaje que indique que el navegador está impidiendo que el sitio abra ventanas emergentes. Elige el banner o el icono y, a continuación, **Allow pop-ups (Permitir elementos emergentes)**.

**Nota:** Vas a utilizar la consola en el entorno de laboratorio, por lo que no incurrirás en ningún gasto real. Sin embargo, en el mundo real, cuando se utiliza una cuenta personal o de empresa para acceder a la consola, los usuarios incurren en gastos por el uso de servicios específicos de AWS.

## Tarea 1. Crear un Bucket de S3 mediante AWS CLI

En esta tarea, crearás un bucket de S3 mediante la Interfaz de la línea de comandos de AWS (AWS CLI). AWS CLI es una herramienta de código abierto que puedes utilizar para interactuar con los servicios de AWS mediante comandos en tu shell de línea de comandos.

1. Elige **Servicios** y **Herramientas para desarrolladores** y, después, **CloudShell**.
2. Si aparece una ventana emergente de bienvenida, selecciona **Cerrar**.

AWS CloudShell es un shell basado en navegador que da acceso a la línea de comandos para los recursos de AWS en la región de AWS seleccionada.

3. Copia y pega el siguiente código en un editor de texto:

```
cd ~
aws s3api create-bucket --bucket (bucket-name) --region us-east-1
```
