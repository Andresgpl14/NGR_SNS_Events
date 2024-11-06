import boto3
import json

# Crear el cliente de SNS con un endpoint local
sns = boto3.client(
    'sns',
    endpoint_url='http://127.0.0.1:4002',
    region_name='us-east-1'
)

# Formatear el mensaje con la clave "default"
message_payload = {
    "default": json.dumps({"key": "hello!"})
}

# Publicar un mensaje en el tópico
response = sns.publish(
    Message=json.dumps(message_payload),  # Convertir el objeto en un string JSON
    MessageStructure='json',
    TopicArn='arn:aws:sns:us-east-1:123456789012:test-topic'
)
print(response)
print("ping")
