import requests
import os

SERVER = "ServerIP:5000"  # Cambia esto por la IP del servidor

def obtener_ruta(partes):
    print("\n📡 Conectando al servidor...")
    response = requests.post(f"{SERVER}/ruta", json={"partes": partes})
    if response.status_code == 200:
        ruta = response.json()["ruta"]
        print(" Ruta generada:", ruta)
        return ruta
    else:
        print(" Error al obtener la ruta:", response.text)
        return None

def archivo_existe_en_servidor(partes, nombre_archivo):
    data = {"partes": partes, "archivo": nombre_archivo}
    response = requests.post(f"{SERVER}/existe", json=data)
    if response.status_code == 200:
        return response.json()["existe"]
    else:
        print(" Error al verificar si el archivo existe:", response.text)
        return False

def subir_archivo(partes, path_archivo, nuevo_nombre=None):
    if not os.path.exists(path_archivo):
        print(" El archivo no existe en tu PC:", path_archivo)
        return

    nombre_para_subir = nuevo_nombre if nuevo_nombre else os.path.basename(path_archivo)

    with open(path_archivo, 'rb') as f:
        files = {'archivo': (nombre_para_subir, f)}
        data = {'partes': '/'.join(partes)}
        response = requests.post(f"{SERVER}/subir", files=files, data=data)

    if response.status_code == 200:
        print( response.json()["mensaje"])
    else:
        print("Error al subir archivo:", response.text)

def menu():
    while True:
        print("\n=== CLIENTE DE SUBIDA DE ARCHIVOS ===")
        print("1. Subir archivo")
        print("2. Salir")
        opcion = input("Selecciona una opción: ") 

        if opcion == "1":
            carpetas = input("  Ingresa las carpetas destino separadas por '/' (ej: sub1/sub2): ").split('/')
            archivo = input(" Ingresa el nombre del archivo a subir (ej: documento.txt): ")
            ruta = obtener_ruta(carpetas)

            if ruta:
                existe = archivo_existe_en_servidor(carpetas, archivo)
                if existe:
                    print(f" El archivo '{archivo}' ya existe en el servidor.")
                    print("¿Qué deseas hacer?")
                    print("1. Sobrescribir")
                    print("2. Cambiar el nombre")
                    print("3. Cancelar")
                    decision = input("Selecciona una opción: ")

                    if decision == "1":
                        subir_archivo(carpetas, archivo, archivo)
                    elif decision == "2":
                        nuevo_nombre = input(" Ingresa el nuevo nombre del archivo (incluye la extensión): ")
                        subir_archivo(carpetas, archivo, nuevo_nombre)
                    else:
                        print(" Subida cancelada.")
                else:
                    subir_archivo(carpetas, archivo)
        elif opcion == "2":
            print("Saliendo del cliente...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()