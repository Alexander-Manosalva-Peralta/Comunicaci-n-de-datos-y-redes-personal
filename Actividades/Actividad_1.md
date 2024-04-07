# Actividad 1: Creación de una red simple.

## Tabla de direccionamiento

| Dispositivo | Interface | Dirección IP | Máscara de subred |
|-------------|-----------|--------------|-------------------|
| PC-A        | NIC       | 192.168.1.10 | 255.255.255.0    |
| PC-B        | NIC       | 192.168.1.11 | 255.255.255.0    |

### Parte 1: Configuración de la topología de la red

a. **Configurar los dispositivos:**
   - Cambié el nombre del switch a S1 y los nombres de las PCs a PC-A y PC-B respectivamente.

<img src="/Comunicacion-de-datos-y-redes-personal/Imagenes/Switch1.png" alt="Texto alternativo" style="width:300px;height:200px;">

b. **Cableado:**
   - Utilicé cables Ethernet Straight-Through para conectar PC-A al puerto F0/6 de S1 y PC-B al puerto F0/1 de S1.

<img src="/Comunicacion-de-datos-y-redes-personal/Imagenes/Cableado.png" alt="Texto alternativo" style="width:300px;height:200px;">


## Parte 2: Configuración de hosts en las PC

a. **Configuración de PC-A:**
   - Ingresé a la interfaz de PC-A y abrí el Command Prompt.
   - Verifiqué la configuración con el comando `ipconfig /all`.

b. **Ping desde PC-A a PC-B:**
   - Utilicé el comando `ping 192.168.1.11` desde PC-A para verificar la conectividad con PC-B.
   - Confirmé que recibí respuestas, lo que indica que la comunicación entre PC-A y PC-B es exitosa.

<img src="/Comunicacion-de-datos-y-redes-personal/Imagenes/Confipc.png" alt="Texto alternativo" style="width:300px;height:200px;">

c. **Configuración de PC-B:**
   - Repetí los mismos pasos en PC-B: verifiqué la configuración con `ipconfig /all`.

d. **Ping desde PC-B a PC-A:**
   - Usé el comando `ping 192.168.1.10` desde PC-B para verificar la conectividad con PC-A.
   - Confirmé que recibí respuestas, lo que indica que la comunicación en ambos sentidos es exitosa.

<img src="/Comunicacion-de-datos-y-redes-personal/Imagenes/Commad.png" alt="Texto alternativo" style="width:300px;height:200px;">

## Resultados

- La configuración y el cableado se realizaron correctamente.
- Se estableció la comunicación entre PC-A y PC-B mediante ping en ambos sentidos.

<img src="/Comunicacion-de-datos-y-redes-personal/Imagenes/Resultado.png" alt="Texto alternativo" style="width:300px;height:200px;">
