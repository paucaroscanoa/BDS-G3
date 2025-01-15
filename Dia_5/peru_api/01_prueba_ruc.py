import requests
import os

#TOKEN='a8accc0c5a779e7078a10cc88bc8ac2ba7df6a335f2358ca81e8585625904fa'
#podemos usar directamente el token o sino genera un ingreso
#Se trae desde una variable entorno
TOKEN = os.environ['TOKEN']
API_URL='https://apiperu.dev/api/ruc'

ruc=input('ingrese el ruc:')

data_request={
    "ruc":ruc
    }

headers={
    "Authorization":f"Bearer {TOKEN}",
    "Content-Type":"aplicaction/json"
}

response=requests.post(API_URL,json=data_request,headers=headers)

if response.status_code==200:
    print(response.json())
else:
    print(f"Error:{response.status_code}-{response.text}")