import requests
import os

#TOKEN='a8accc0c5a'
#podemos usar directamente el token o sino genera un ingreso
#Se trae desde una variable entorno mediante "os"
TOKEN = os.environ['TOKEN']
API_URL='https://apiperu.dev/api/dni'

dni=input('ingrese el dni:')

data_request={
    "dni":dni
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