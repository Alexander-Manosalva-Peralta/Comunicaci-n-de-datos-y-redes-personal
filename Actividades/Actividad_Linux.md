# Escribir nuestro primer guión y hacerlo funcionar

Para escribir con éxito un script de shell, tenemos que hacer tres cosas:

1. Escribir un guion
2. Darle permiso al shell para ejecutarlo.
3. Ponerlo en algún lugar donde el caparazón pueda encontrarlo.

## Escribir un guión

Un script de shell es un archivo que contiene texto ASCII. Para crear un script de shell, utilizamos un editor de texto. Hay muchos editores de texto disponibles para sistemas Linux. Aquí hay una lista de algunos comunes:

| Nombre | Descripción | Interfaz |
|--------|-------------|----------|
| vi, vim | El abuelo de los editores de texto Unix, famoso por su interfaz de usuario. | Línea de comando |
| Emacs | El verdadero gigante en el mundo de los editores de texto. | Línea de comando |
| nano | Un clon gratuito del editor de texto suministrado con el programa de correo electrónico Pine. | Línea de comando |
| gedit | El editor suministrado con el entorno de escritorio GNOME. | Gráfico |
| kwrite | El "editor avanzado" suministrado con KDE. | Gráfico |

Iniciemos nuestro editor de texto y escribamos nuestro primer script de la siguiente manera:

```bash
#!/bin/bash
# Mi primer script repite "¡Hola mundo!"
echo "¡Hola mundo!"

## Escribir nuestro primer guión y hacerlo funcionar

cat <<'EOF' > hello_world.sh
#!/bin/bash
# Mi primer script repite "¡Hola mundo!"
echo "¡Hola mundo!"
EOF

[![Texto alternativo](URL_de_la_imagen)](URL_del_enlace)

## Comando para editar el script sysinfo_page

[![Texto alternativo](URL_de_la_imagen)](URL_del_enlace)

## Mostrar el nombre de host del sistema

[![Texto alternativo](URL_de_la_imagen)](URL_del_enlace)

## Obtener la marca de tiempo actual

[![Texto alternativo](URL_de_la_imagen)](URL_del_enlace)

## Comando para editar el script sysinfo_page con funciones

[![Texto alternativo](URL_de_la_imagen)](URL_del_enlace)

## Verificar el contenido del script sysinfo_page con funciones

[![Texto alternativo](URL_de_la_imagen)](URL_del_enlace)
