# soap_server.py
from flask import Flask, request, Response
from spyne import Application, rpc, ServiceBase, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

app = Flask(__name__)

class HelloWorldService(ServiceBase):
    @rpc(Unicode, _returns=Unicode)
    def say_hello(ctx, name):
        return f"Hello, {name}!"

# Crear la aplicación SOAP
soap_application = Application(
    [HelloWorldService],
    tns='http://example.com/hello',
    in_protocol=Soap11(),
    out_protocol=Soap11()
)

# Crear el servidor WSGI de Spyne
wsgi_application = WsgiApplication(soap_application)

@app.route('/soap', methods=['POST'])
def soap():
    # Conectar el servicio SOAP al endpoint
    response = wsgi_application(request.environ, start_response)
    return Response(response, content_type='text/xml')

def start_response(status, headers):
    """Función necesaria para el WSGI"""
    return None

if __name__ == '__main__':
    app.run(debug=True, port=5001)
