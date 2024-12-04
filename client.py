# soap_client.py
import zeep

# URL del servidor SOAP
url = 'http://localhost:5001/soap'

# Crear el cliente SOAP
client = zeep.Client(url)

# Llamar al servicio SOAP
response = client.service.say_hello('Juan')
print(response)
