import base64
import uuid
import fitz
import talina_mapper
import os
from flask import Flask, request, jsonify
from flask_cors import CORS

# Creamos la aplicación Flask
app = Flask(__name__)
CORS(app, origins=['*'])

# Definimos el endpoint que manejará las solicitudes POST
@app.route('/process-pdf', methods=['POST'])
def process_pdf():

    #Obtener base 64 de la consulta
    data = request.get_json()
    pdf_base64 = data['base64']

    # Crear archivo temporal para procesar
    pdfName = str(uuid.uuid4()) + ".pdf"
    with open(pdfName, "wb") as f:
        f.write(base64.b64decode(pdf_base64))
        
        doc = fitz.open(f.name)
        
        page = doc.load_page(0)

        response = jsonify(talina_mapper.process_data(page.get_text()))

        doc.close()

    #Borrar archivo temporal
    os.remove(f.name)

    return response

# Iniciamos la aplicación
if __name__ == '__main__':
    app.run(host='0.0.0.0')
