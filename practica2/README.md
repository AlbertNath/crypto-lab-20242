# Criptografía y seguridad 
## Semestre 2024-2
### Práctica 2: Explotación de Vulnerabilidades: Desbordamiento de Búfer
------------------
#### Nombres
- Alberto Natanael Medel Piña
- Britny Brito Juárez
- Janet Illescas Coria
- Paola Vargas Bravo

#### Prerequisitos
- VirtualBox
- gcc
- gdb
- bash
- python
- C

#### Descripción
En total se cuenta con 6 archivos. Mismos que se encuentran divididos en dos carpetas:

- exploit-pass: cuenta con el archivo simple-password-verification.c, mismo que tiene  la vulnerabilidad de desbordamiento de búfer. También esta exploit-pass.py que justamente explota la vulnerabilidad de simple-password-verification.c. Y por último en tenemos simple-password-verification-new.c que es la versión sin vulnerabilidad de desbordamiento de búfer de simple-password-verification.c.
- exploit-ver: cuenta con el archivo simple-verification.c, mismo que tiene  la vulnerabilidad de desbordamiento de búfer. También esta exploit-ver.py que justamente explota la vulnerabilidad de simple-verification.c. Y por último en tenemos simple-verification-new.c que es la versión sin vulnerabilidad de desbordamiento de búfer de simple-verification.c.

#### Ejecución
Antes de poder proceder con la ejecución, es necesario desactivar candados de seguridad que buscan mitigar este tipo de ataques. Primero tendremos que desactivar ASLR, una medida de protección para capa de memoria del kernel. 
Podemos desactivarla temporalmente con 

``` sh
$ sudo sysctl -w kernel.randomize_va_space=0
```
Tras un reinicio del sistema, la bandera `kernel.randomize_va_space` volverá a su estado original (valor 2).

Adicionalmente, es necesario desactivar la protección del compilador de `C` contra ataques de desbordamiento; utilizamos el siguiente comando para compilar los archivos `.c` vulnerables

``` sh
$ gcc -fno-stack-protector -z execstack <archivo_vulnerable.c>
```
Con esto, podemos proceder a explotar las vulnerabilidades con los scripts.

Para poder ejecutar el programa de exploit-pass.py:
```sh
$ python exploit-pass.py simple-password-verification.c
```

Para poder ejecutar el programa de exploit-ver.py:
```sh
$ python exploit-ver.py simple-verification.c
```

Para poder ejecutar el programa de simple-password-verification-new.c:
```sh
$ gcc -fno-stack-protector simple-password-verification-new.c
$ ./a.out
```

Para poder ejecutar el programa de simple-verification-new.c:
```sh
$ gcc -fno-stack-protector simple-verification-new.c
$ ./a.out
```
