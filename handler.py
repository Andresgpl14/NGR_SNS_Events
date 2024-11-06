import json

def process_sns(event, context):
    print("+++++++++++++++++++++++++++++++++++++++")
    print(event)
    # for record in event['Records']:
    #     sns_message = record['Sns']
    #     print(f"Mensaje recibido de SNS: {sns_message['Message']}")
    #     # Procesa el mensaje según sea necesario
    #     print(f"Detalles del mensaje completo: {json.dumps(sns_message, indent=2)}")

    # return {
    #     "statusCode": 200,
    #     "body": json.dumps({"message": "Mensajes procesados correctamente"})
    # }
