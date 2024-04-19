## Actividad: Repaso de protocolos

**Objetivos:**
- Relacionar los protocolos de red de la computadora con las reglas que se usan en la comunicación diaria.
- Definir las reglas que gobiernan el envío e interpretación de mensajes de texto.
- Explicar las posibles consecuencias si el emisor y el receptor no están de acuerdo en los detalles del protocolo.

### Aspectos básicos

Antes de cualquier comunicación, establecemos reglas o acuerdos que rigen la conversación. Estas reglas, o protocolos, deben respetarse para que el mensaje se envíe y comprenda correctamente. Entre las características de los protocolos que rigen una comunicación humana satisfactoria se encuentran:

- Un emisor y un receptor identificados.
- Un método de comunicación acordado.
- Idioma y gramática común.
- Velocidad y momento de entrega.
- Requisitos de confirmación o acuse de recibo.

Las técnicas utilizadas en las comunicaciones de red comparten estos fundamentos con las conversaciones humanas.

### Protocolo de mensajería de texto

| Requisito del protocolo | ¿Qué significa esto? | ¿Cómo se implementa en su protocolo? |
|-------------------------|-----------------------|--------------------------------------|
| Un emisor y un receptor identificados |¿Cómo sabe de quién es el mensaje de texto? ¿Cómo sabe la persona en el otro extremo que usted recibió el mensaje? ¿Va dirigido a una persona o a un grupo? | En la mensajería de texto, el emisor y el receptor se identifican mediante direcciones únicas, como números de teléfono o identificadores de usuario. Esto se implementa mediante el protocolo SMS (Short Message Service) o aplicaciones de mensajería instantánea que requieren autenticación y registro de usuarios. Los mensajes pueden ser dirigidos a un destinatario específico o a un grupo según el formato del mensaje y los datos de destino especificados en los encabezados del protocolo. |
| Un método de comunicación acordado | ¿Solo enviamos texto? ¿Enviamos y recibimos fotos? ¿Y los emoticones y emoji? | En la mensajería de texto, el protocolo define la estructura y el formato de los mensajes que pueden incluir texto, multimedia como fotos, videos y archivos, así como emojis y emoticones. Esto se logra mediante la especificación de formatos de mensajes compatibles, como el estándar de mensajes multimedia (MMS) para contenido multimedia y extensiones de protocolo para incluir emojis y emoticones en mensajes de texto. |
| Idioma y gramática común | ¿Usamos acrónimos? ¿Es aceptable el argot? ¿Cuál es el idioma materno de los participantes? | El protocolo permite el uso de diferentes idiomas, acrónimos y términos de jerga según las preferencias y la comprensión mutua de los participantes. Esto se logra mediante la codificación de caracteres y la especificación de reglas de gramática y ortografía en los mensajes, lo que permite la interpretación adecuada del contenido por parte del receptor. |
| Velocidad y momento de entrega | ¿Qué determina con qué velocidad llega el mensaje al destinatario? ¿Con qué velocidad esperamos recibir una respuesta? | La velocidad de entrega de los mensajes de texto está determinada por factores como la congestión de la red, la priorización de mensajes y la calidad de la conexión. Los protocolos de red utilizados para la transmisión de mensajes definen mecanismos de entrega y retransmisión que garantizan la entrega oportuna de los mensajes al destinatario. La respuesta esperada depende de la disponibilidad y la tasa de respuesta del destinatario, así como de la priorización de la comunicación en tiempo real. |
| Requisitos de confirmación o acuse de recibo | ¿Cómo sabe que se recibió el mensaje? ¿Cómo sabe que la conversación terminó? | El protocolo de mensajería de texto incluye mecanismos de confirmación de entrega y notificaciones de lectura para garantizar la entrega y la recepción exitosa de los mensajes. Estos mecanismos están integrados en los protocolos de transporte de mensajes y en las aplicaciones de mensajería para proporcionar retroalimentación al remitente sobre el estado de entrega y lectura de los mensajes. La conversación se considera concluida cuando se reciben señales explícitas de finalización o cuando no hay actividad en la comunicación durante un período de tiempo determinado, lo que se puede implementar mediante temporizadores de inactividad en los protocolos de sesión y aplicación. |

### Preguntas

1. **Ahora que has descrito los protocolos utilizados para enviar y leer mensajes de texto, ¿crees que estos protocolos serían los mismos si estuvieras comunicándote con amigos en comparación con tus padres o profesores? Explica tu respuesta.**

   *Respuesta:* Los protocolos pueden variar según el contexto y la relación entre los participantes. Por ejemplo, en una comunicación informal con amigos, es probable que se utilicen más emojis, abreviaturas y un tono más relajado. En contraste, al comunicarse con padres o profesores, es probable que se prefiera un lenguaje más formal y respetuoso, con menos abreviaturas y una estructura gramatical más cuidada. En términos de protocolos de red, esto podría reflejarse en el uso de diferentes tipos de servicios de mensajería con distintas configuraciones de privacidad y funciones de seguridad, así como en la aplicación de políticas de filtrado de contenido o control de acceso para garantizar la comunicación adecuada en cada contexto.

2. **¿Cuáles crees que serían las consecuencias si no hubiera estándares de protocolo acordados para los diferentes métodos de comunicación?**

   *Respuesta:* Sin estándares de protocolo acordados, habría falta de interoperabilidad entre diferentes plataformas de mensajería, lo que dificultaría la comunicación entre usuarios que utilizan servicios diferentes. Además, la falta de estándares podría dar lugar a vulnerabilidades de seguridad, como la falta de autenticación o la exposición de datos sensibles. Esto podría resultar en la interceptación de mensajes, el robo de identidad o la propagación de malware a través de mensajes no seguros. En términos más generales, la falta de estándares podría generar confusión y malentendidos en la comunicación, lo que dificultaría la colaboración efectiva y la toma de decisiones basada en la información transmitida.

3. **Comparte las reglas de protocolo con tus compañeros de equipo. ¿Hay diferencias entre tus protocolos y los de ellos? Si es así, ¿podrían estas diferencias producir malentendidos de los mensajes?**

   *Respuesta:* Al compartir las reglas de protocolo con mis compañeros de equipo, podríamos notar diferencias en la configuración de privacidad, la preferencia de aplicaciones de mensajería y el uso de funciones como la confirmación de lectura. Estas diferencias podrían causar malentendidos si no se establecen expectativas claras sobre el comportamiento y las preferencias de comunicación de cada parte.

