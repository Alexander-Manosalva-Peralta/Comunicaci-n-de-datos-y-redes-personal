# Amazon SNS (Simple Notification Service)

## Introducción
Amazon SNS (Simple Notification Service) es un servicio de mensajería totalmente gestionado que coordina la entrega de mensajes a suscriptores en múltiples servicios y dispositivos.

## Conceptos Clave
| Concepto              | Descripción                                                                                     |
|-----------------------|-------------------------------------------------------------------------------------------------|
| **Tópicos**           | SNS utiliza tópicos para entregar mensajes a un conjunto de suscriptores. |
| **Suscripciones**     | Los usuarios o servicios pueden suscribirse a un tópico para recibir mensajes.          |
| **Protocolos de Entrega** | SNS soporta múltiples protocolos de entrega, incluidos HTTP/S, correo electrónico, SMS, y AWS Lambda. |

## Beneficios
- **Entrega en Tiempo Real**: SNS ofrece una entrega de mensajes de baja latencia a millones de suscriptores.
- **Alta Disponibilidad**: SNS está diseñado para proporcionar una alta disponibilidad y durabilidad.
- **Escalabilidad**: SNS puede escalar automáticamente para manejar una gran cantidad de mensajes.

## Casos de Uso
- **Notificaciones en Tiempo Real**: Enviar alertas y notificaciones en tiempo real a usuarios o sistemas.
- **Integración de Servicios**: Facilitar la comunicación entre diferentes servicios de AWS.
- **Automatización de Flujos de Trabajo**: Activar flujos de trabajo automáticos en respuesta a eventos.

## Ejemplos de Uso
- **Alertas y Monitoreo**: Enviar alertas de monitoreo a administradores de sistemas.
- **Notificaciones Móviles**: Enviar notificaciones push a aplicaciones móviles.
- **Integración con AWS Lambda**: Ejecutar funciones Lambda en respuesta a mensajes publicados en un tópico SNS.
