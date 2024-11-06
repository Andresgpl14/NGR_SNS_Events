# Título del Proyecto

_Demostración del simulador SNS_

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

Mira **Deployment** para conocer como desplegar el proyecto.


### Pre-requisitos 📋

_Instalar las dependecias para el uso de Serverless framework_
```
npm install
```

### Instalación 🔧


_inicializar servicio_
```
serverless offline start
```

_En bash se muestra la URL de los servicios activos_
```

   ┌──────────────────────────────────────────────────────────────────────────────┐
   │                                                                              │
   │   GET  | http://localhost:3000/dev/hello                                     │
   │   POST | http://localhost:3000/2015-03-31/functions/hello/invocations        │
   │   POST | http://localhost:3000/dev/estudiante                                │
   │   POST | http://localhost:3000/2015-03-31/functions/estudiante/invocations   │
   │                                                                              │
   └──────────────────────────────────────────────────────────────────────────────┘

Server ready: http://localhost:3000 🚀
```

## Ejecutando las pruebas ⚙️

_Realizar llamada al servicio para registrar los datos de la persona_
```
curl --location 'http://localhost:3000/dev/registrar' \
--header 'Content-Type: application/json' \
--data-raw '{
    "persona_id":"70435646",
    "nombre":"Andres",
    "apellido":"Pinto",
    "edad":"36",
    "email":"andres@correo.com"
```

_Escanear tabla para revisar resultados_
```
aws dynamodb scan --table-name Persona --endpoint-url http://localhost:8000
```

## Construido con 🛠️

_Menciona las herramientas que utilizaste para crear tu proyecto_

* [Serverless Framework](https://www.serverless.com/) 
