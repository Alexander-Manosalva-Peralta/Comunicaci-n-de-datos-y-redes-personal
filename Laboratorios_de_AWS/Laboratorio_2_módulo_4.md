# Laboratorio 2 del Módulo 4: Creación de un Bucket de S3

## Información General sobre el Laboratorio

En este laboratorio, seguirás los pasos para crear un bucket de Amazon Simple Storage Service (Amazon S3) para alojar un sitio web estático. 

## Tarea 1. Crear un Bucket de S3

1. Selecciona el menú **Servicios**, localiza los servicios de **Almacenamiento** y selecciona **S3**.

![Descripción de la imagen](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/tarea1.png)

2. Selecciona **Crear bucket** en la parte derecha de la página.

![Descripción de la imagen](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/tarea1.1.png)

3. En **Nombre del bucket**, introduce un nombre exclusivo compatible con el sistema de nombres de dominio (DNS) para el nuevo bucket.

![Descripción de la imagen](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/tarea1.2.png)

### Configuración de Seguridad

1. Quita la marca de la casilla **Bloquear todo el acceso público**.
2. Marca la casilla junto a **Confirmo que...**.

![Descrip](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/tarea%201.3.png)

3. Desplázate hasta la parte inferior de la página y selecciona **Crear bucket**.

![Descrp](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/tarea1.4.png?raw=true)

4. El nuevo bucket aparece en la lista **Buckets**.

![Descrip](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/1.5.png)

## Tarea 2. Añadir una Política de Bucket para que el Contenido esté Disponible Públicamente

1. Elige el enlace para el nombre del bucket y, a continuación, selecciona la pestaña **Permisos**.

![Descrip](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/2.1.png?raw=true)

2. En la sección **Política de bucket**, selecciona **Editar**.

![Descrip](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/2.2.png?raw=true)

3. Copia la siguiente política de bucket y pégala en el editor de políticas.
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::example-bucket/*"
            ]
        }
    ]
}
```
![Descrip](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/tarea2.3.png?raw=true)

## Tarea 3. Subir un documento HTML

1. Abre el menú contextual (clic derecho) para el siguiente enlace y después selecciona Guardar enlace como: [index.html](URL_DEL_ENLACE).

![Descrip](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/tarea3.1.png?raw=true)
   
2. Guarda el archivo `index.html` en el equipo local.
3. En la consola, selecciona la pestaña Objetos.

![Descrip](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/3.2.png?raw=true)

4. Carga el archivo `index.html` en tu bucket.
    - Selecciona **Cargar**.
    - Arrastra y suelta el archivo `index.html` en la página de carga.
    - Como alternativa, selecciona **Añadir archivos**, navega al archivo y selecciona **Abrir**.

![Descrip](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/3.3.png?raw=true)

5. Amplía la sección Propiedades.
6. Asegúrate de que está seleccionada la clase de almacenamiento **Estándar**.

![Descrip](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/3.4.png?raw=true)

7. En la parte inferior de la página, selecciona **Cargar**.

![Descrip](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/3.5.png?raw=true)

8. Selecciona **Cerrar**.

![Descrip](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/3.6.png?raw=true)

El archivo `index.html` aparece en la lista Objetos.

![Descrip](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/3.7.png?raw=true)

## Tarea 4. Probar el sitio web

1. Selecciona la pestaña Propiedades y desplázate a la sección **Alojamiento de sitios web estáticos**.
2. Selecciona **Editar**.

![Descrip](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/4.1.png?raw=true)
	
3. Selecciona **Habilitar**.

![Descrip](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/4.2.png?raw=true)

4. En el cuadro de texto **Documento de índice**, introduce `index.html`.

![Descrip](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/4.3.png?raw=true)

5. Selecciona **Guardar cambios**.

6. Desplázate de nuevo hacia abajo hasta la sección **Alojamiento de sitios web estáticos** y copia la URL del **Punto de enlace de sitio web** del bucket en el portapapeles.

![Descrip](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/4.4.png?raw=true)

7. Abre una nueva pestaña en el navegador web, pega la URL que acabas de copiar y pulsa Intro.
Debería abrirse la página web "Hello World". Has alojado correctamente un sitio web estático mediante un bucket de S3.

![Descrip](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/4.5.png?raw=true)

8. Adicional agregado por mí
*Index editado por mí*

![Descrip](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/4.6.png?raw=true)

## Laboratorio completado

¡Enhorabuena! Has completado el laboratorio.
