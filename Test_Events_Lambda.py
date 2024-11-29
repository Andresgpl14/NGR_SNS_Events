import boto3
import json

# Configura el cliente Lambda apuntando al endpoint local
#boto3.set_stream_logger('botocore', level='DEBUG')

lambda_client = boto3.client(
    'lambda',
    region_name="us-east-1",
    endpoint_url="http://localhost:3002/"  # Puerto donde escucha serverless-offline para Lambda
)

# Prepara el evento de SNS simulado
payload = {
	"Records": [
		{
			"EventSource": "aws:sns",
			"EventVersion": "1.0",
			"EventSubscriptionArn": "arn:aws:sns:us-east-1:629165914041:SNS_Event_Demo:488808e3-afe5-424e-9c23-94a2de4bccc5",
			"Sns": {
				"Type": "Notification",
				"MessageId": "6aad68cf-a67e-553a-957d-376bfbee1131",
				"TopicArn": "arn:aws:sns:us-east-1:629165914041:SNS_Event_Demo",
				"Subject": "Asunto",
				"Message": "Mensajes procesados correctamente",
				"Timestamp": "2024-11-05T17:52:16.939Z",
				"SignatureVersion": "1",
				"Signature": "YyP4k8c1Wu17HnAwzpcMOm6ia/Ark1a5bivcau4ZGtgNFNO2O/kHZ0ul0PBKzkYQsk8UF6kA7INbfXnW5bCuCOXrPcifj8mHzzaaPOAmb5JAf8BeATSBr3AS7L+JXEZLioMHUP6w95od/QRhSVaT7XPU7OsJJqlFSRdSRjITKnlSG+M6PzhJDO4RIvpQDhij8bRz4k1DQaurXUyG6sF8cSazV2x2Pi7Zniy4561ZWS+fnZYYQfLCcV43amzCR4Zw6lXkqr8iXstQzzjjXEW3f2vQjEK4rQZ9n/VTRp6HOV2YMni8tfqDsKRE91YVRRW1LTRWRV7WD1UGDeX13QwZZA==",
				"SigningCertUrl": "https://sns.us-east-1.amazonaws.com/SimpleNotificationService-9c6465fa7f48f5cacd23014631ec1136.pem",
				"UnsubscribeUrl": "https://sns.us-east-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-1:629165914041:SNS_Event_Demo:488808e3-afe5-424e-9c23-94a2de4bccc5",
				"MessageAttributes": {}
			}
		}
	]
}

# Invoca la función Lambda
response = lambda_client.invoke(
    FunctionName="proyecto-demo-dev-demoSNS",
    InvocationType="RequestResponse", 
    Payload=json.dumps(payload),
)

# Lee la respuesta
response_payload = json.loads(response['Payload'].read())
print("Respuesta de Lambda:", response_payload)
