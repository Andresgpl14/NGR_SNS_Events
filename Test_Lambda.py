import boto3
import json

# Configura el cliente Lambda apuntando al endpoint local
lambda_client = boto3.client(
    'lambda',
    region_name="us-east-1",
    endpoint_url="http://localhost:3002",  # Puerto donde escucha serverless-offline para Lambda
)

# Prepara el evento de S3 simulado
payload = {
    "Records": [
        {
            "s3": {
                "bucket": {"name": "local-bucket"},
                "object": {"key": "yourfile4.txt"}
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
