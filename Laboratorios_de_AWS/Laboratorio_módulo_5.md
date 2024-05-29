# Laboratorio del Módulo 5: Uso de CloudFront como CDN para un Sitio Web

## Información General sobre el Laboratorio

En este laboratorio, utilizarás Amazon CloudFront como red de entrega de contenido (CDN) para un sitio web almacenado en Amazon Simple Storage Service (Amazon S3).

## Tarea 1. Crear un Bucket de S3 mediante AWS CLI

En esta tarea, crearás un bucket de S3 mediante la Interfaz de la línea de comandos de AWS (AWS CLI). AWS CLI es una herramienta de código abierto que puedes utilizar para interactuar con los servicios de AWS mediante comandos en tu shell de línea de comandos.

1. Elige **Servicios** y **Herramientas para desarrolladores** y, después, **CloudShell**.
2. Si aparece una ventana emergente de bienvenida, selecciona **Cerrar**.

![Des](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/mod5_1.png)

AWS CloudShell es un shell basado en navegador que da acceso a la línea de comandos para los recursos de AWS en la región de AWS seleccionada.
3. Copia y pega el siguiente código en un editor de texto:

```
cd ~
aws s3api create-bucket --bucket (bucket-name) --region us-east-1
```
![Des](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/mod5_2.png)

4. Ejecuta el código actualizado en el terminal de CloudShell.
El resultado debe tener un aspecto similar al siguiente:
```
{
   "Location": "/mylabbucket12345"
}
```

![Des](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/mod5_3.png)

## Tarea 2: Añadir una política de bucket

En esta tarea, añadirás una política de bucket a través de AWS CLI para que el contenido esté disponible públicamente.

1. En la consola, selecciona el menú **Servicios**, localiza la sección **Almacenamiento** y elige **S3**.

![mod5_4](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/mod5_4.png)

2. Elige el nombre del bucket que acabas de crear.

![mod5_5](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/mod5_5.png)

3. Selecciona la pestaña **Permisos**. En **Bloquear acceso público (configuración del bucket)**, selecciona **Editar**.
4. Desactiva la casilla de **Bloquear todo el acceso público**. Elige **Guardar cambios**. Confirma los cambios.

![mod5_6](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/mo5_6.png)

5. Desplázate hasta **Propiedad del objeto** y selecciona **Editar**. Selecciona **ACL habilitadas**. Comprueba el reconocimiento y selecciona **Guardar cambios**.

![mod5_7](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/mod5_7.png)

6. En la sección **Política del bucket**, selecciona **Editar**.

![mod5_8](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/mod5_8.png)

7. Para conceder acceso de lectura pública a tu sitio web, copia y pega la siguiente política del bucket en el editor de políticas:

```json
{
   "Version":"2012-10-17",
   "Statement":[
      {
         "Sid":"PublicReadForGetBucketObjects",
         "Effect":"Allow",
         "Principal":"*",
         "Action":[
            "s3:GetObject"
         ],
         "Resource":[
            "arn:aws:s3:::example-bucket/*"
         ]
      }
   ]
}
```

![mod5_9](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/mod5_9.png)

En la política, reemplaza example-bucket por el nombre del bucket.
En la parte inferior de la página, selecciona Guardar cambios.

## Tarea 3. Subir un documento HTML
En esta tarea, subirás el archivo `index.html` de tu página web en el bucket de S3.

1. Abre el menú contextual (haz clic con el botón derecho) del siguiente enlace y, a continuación, elige **Save link as (Guardar enlace como)**: [index.html](https://example.com/index.html)

2. Guarda el archivo `index.html` en el equipo local.

3. En la consola, selecciona la pestaña **Objetos**.

4. Carga el archivo `index.html` en tu bucket.
   - Selecciona **Cargar**.
   - Arrastra y suelta el archivo `index.html` en la página de carga. También puedes seleccionar **Añadir archivos**, buscar el archivo y usar la opción **Abrir**.


![mod5_10](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/mod5_10.png)

5. Expande la sección **Permisos**.
   - En **ACL predefinidas**, selecciona **Conceder acceso de lectura público**.

![mod5_11](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/mod5_11.png)

   - Debajo de la configuración seleccionada aparece un mensaje parecido a este: _No se recomienda otorgar acceso de lectura público_.
   - Marca la casilla que aparece junto a _Entiendo que..._ debajo del mensaje de advertencia.

![mod5_12](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/mod5_12.png)

6. En la parte inferior de la página, selecciona **Cargar**.

7. Selecciona **Cerrar**.

El archivo `index.html` aparece en la lista **Objetos**.

## Tarea 4. Probar el sitio web
1. Selecciona la pestaña **Propiedades** y desplázate a la sección **Alojamiento de sitios web estáticos**.
2. Selecciona **Editar**.
3. Selecciona **Habilitar**.

![mod5_13](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/mod5_13.png)

4. En el cuadro de texto **Documento de índice**, introduce `index.html`.
5. Selecciona **Guardar cambios**.

![mod5_14](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/mod5_14.png)

6. Desplázate de nuevo hacia abajo hasta la sección **Alojamiento de sitios web estáticos** y copia la URL del **Punto de enlace de sitio web del bucket** en el portapapeles.
7. Abre una nueva pestaña en el navegador web, pega la URL que acabas de copiar y pulsa **Intro**.
Debería abrirse la página web **Hello World**. Has alojado correctamente un sitio web estático mediante un bucket de S3.

![mod5_15](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/mod5_15.png)

## Tarea 5. Crear una distribución de CloudFront para servir al sitio web
En esta tarea, crearás una distribución de Amazon CloudFront para servir al sitio web.

1. Selecciona el menú **Servicios**, localiza la sección **Redes y entrega de contenido** y selecciona **CloudFront**.

![mod5_16](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/mod5_16.png)

2. Selecciona **Crear una distribución de CloudFront**.

![mod5_17](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/mod5_17.png)

3. En la sección **Origen**, selecciona el cuadro de texto que aparece junto a **Dominio de origen** y selecciona el punto de enlace de tu bucket de S3.

![mod5_18](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/mod5_18.png)

4. Para **Viewer Protocol Policy (Política de protocolo de visor)**, asegúrate de que **HTTP y HTTPS** estén seleccionados.

![mod5_19](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/mod5_19.png)

5. En **Web Application Firewall (WAF)**, selecciona **Do not enable security protections (No habilitar protecciones de seguridad)**.

![mod5_20](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/mod5_20.png)

6. Desplázate hasta la parte inferior de la página y selecciona **Crear distribución**.
Se muestra una nueva distribución de CloudFront en la lista de distribuciones. El **Estado** será **Implementando** hasta que el sitio web se haya distribuido. Puede tardar hasta 20 minutos.
Cuando el **Estado** sea **Habilitado**, puedes probar la distribución.

![mod5_21](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/mod5_21.png)

1. Copia el valor de **Nombre de dominio** de la distribución y guárdalo en un editor de texto para utilizarlo en un paso posterior.

![mod5_22](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/mod5_22.png)

2. Crea un nuevo archivo HTML para probar la distribución.
   - Busca y descarga una imagen de Internet.
   - Navega hasta el bucket de S3 y carga el archivo de imagen en el bucket, asegurándote de otorgar acceso público tal como lo hiciste al subir el archivo HTML antes en este laboratorio.

![mod5_23](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/mod5_23.png)

![mod5_24](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/mod5_24.png)

   - Crea un nuevo archivo de texto con el Bloc de notas y copia en él el siguiente texto:

     ```html
     <html>
         <head>My CloudFront Test</head>
         <body>
             <p>My test content goes here.</p>
             <p><img src="http://domain-name/object-name" alt="my test image">
         </body>
     </html>
     ```

   - Reemplaza `domain-name` por el nombre de dominio que copiaste antes para la distribución de CloudFront.
   - Reemplaza `object-name` por el nombre del archivo de imagen que cargaste en el bucket de S3.
   - La línea de código editada debe tener un aspecto similar al siguiente:

     ```html
     <p><img src="http://d2f1zrxb2zaf30.cloudfront.net/picture.jpg" alt="my test image">
     ```

   - Guarda el archivo de texto con extensión HTML.

![mod5_25](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/mod5_25.png)

   - Utiliza un navegador de Internet para abrir el archivo HTML que acabas de crear.

Si se muestra la imagen que cargaste, la distribución de CloudFront se realizó correctamente. Si no es así, repite el laboratorio.

![mod5_26](https://github.com/Alexander-Manosalva-Peralta/Comunicacion-de-datos-y-redes-personal/blob/main/Imagenes/mod5_26.png)

## Laboratorio completado
¡Enhorabuena! Has completado el laboratorio.


