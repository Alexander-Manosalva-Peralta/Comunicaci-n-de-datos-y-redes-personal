# Actividad 2: Implementación de una conectividad básica

## Tabla de asignación de direcciones

| Dispositivo | Interfaz | Dirección IP | Máscara de subred |
|-------------|----------|--------------|-------------------|
| S1          | VLAN 1   | 192.168.1.253 | 255.255.255.0  |
| S2          | VLAN 1   | 192.168.1.254 | 255.255.255.0  |
| PC1         | NIC      | 192.168.1.1   | 255.255.255.0  |
| PC2         | NIC      | 192.168.1.2   | 255.255.255.0  |

### Parte 1: Realizar una configuración básica en S1 y S2

1. **Configuración básica en S1:**
   - Configuré el nombre de host del S1 como S1.
   - Establecí contraseñas cifradas para la consola y el modo EXEC privilegiado.
   - Configuré un aviso de MOTD.
   - Guardé la configuración en la NVRAM.

   <img src="URL_de_la_imagen_S1.png" alt="Imagen de S1" style="width:300px;height:200px;">

2. **Configuración básica en S2:**
   - Repetí los pasos anteriores para S2.

   <img src="URL_de_la_imagen_S2.png" alt="Imagen de S2" style="width:300px;height:200px;">

### Parte 2: Configurar las PC

1. **Configuración de PC1 y PC2:**
   - Configuré las direcciones IP de PC1 y PC2 según la tabla de asignación.

   <img src="URL_de_la_imagen_PC.png" alt="Imagen de configuración de PC" style="width:300px;height:200px;">

2. **Prueba de conectividad a los switches:**
   - Realicé pruebas de ping desde PC1 y PC2 hacia S1 y S2 para verificar la conectividad.

   <img src="URL_de_la_imagen_ping.png" alt="Imagen de prueba de ping" style="width:300px;height:200px;">

### Parte 3: Configurar la interfaz de administración de switches

1. **Configuración de dirección IP en S1:**
   - Configuré la interfaz VLAN 1 de S1 con la dirección IP asignada.

   <img src="URL_de_la_imagen_S1_ipconfig.png" alt="Imagen de configuración de IP en S1" style="width:300px;height:200px;">

2. **Configuración de dirección IP en S2:**
   - Repetí los pasos anteriores para configurar la dirección IP en S2.

   <img src="URL_de_la_imagen_S2_ipconfig.png" alt="Imagen de configuración de IP en S2" style="width:300px;height:200px;">

### Verificación de resultados

- Verifiqué la conectividad de la red mediante pruebas de ping desde las PC hacia los switches y viceversa.
- Todos los pings fueron exitosos, lo que indica que la configuración y la conectividad básica fueron exitosas.

   <img src="URL_de_la_imagen_resultado_ping.png" alt="Imagen de resultados de ping" style="width:300px;height:200px;">

