from flask import Flask, request, jsonify
import os

app = Flask(__name__)
BASE_DIR = os.path.join(os.getcwd(), "uploads")
os.makedirs(BASE_DIR, exist_ok=True)

@app.route('/ruta', methods=['POST'])
def generar_ruta():
    data = request.get_json()
    partes = data.get("partes", [])

    ruta = os.path.join(BASE_DIR, *partes)
    os.makedirs(ruta, exist_ok=True)

    return jsonify({"ruta": ruta})

@app.route('/existe', methods=['POST'])
def verificar_existencia():
    data = request.get_json()
    partes = data.get("partes", [])
    nombre = data.get("nombre", "")

    ruta = os.path.join(BASE_DIR, *partes)
    path_completo = os.path.join(ruta, nombre)

    return jsonify({"existe": os.path.exists(path_completo)})

@app.route('/subir', methods=['POST'])
def subir_archivo():
    partes = request.form.get("partes", "").split("/")
    archivo = request.files.get("archivo")

    if not archivo:
        return "Archivo no recibido", 400

    ruta = os.path.join(BASE_DIR, *partes)
    os.makedirs(ruta, exist_ok=True)

    destino = os.path.join(ruta, archivo.filename)
    archivo.save(destino)

    return jsonify({"mensaje": f"Archivo subido como {archivo.filename}"})

if __name__ == "__main__":
    print(f"Servidor escuchando en http://0.0.0.0:5000")
    app.run(host="0.0.0.0", port=5000)