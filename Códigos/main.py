"""
MÁQUINA VIRTUAL - SO 2023
Integrantes: Lucarelli, Monti, Mosconi, Terreno
"""


"""
A continuación se realizará la INICIALIZACIÓN DE VARIABLES, 
según los refinamientos planteados en https://docs.google.com/document/d/1d9OCoB_hRpRdz8k71dXcPaGg0XyF2U0yhzvx864gpnc/edit?usp=sharing
"""
xp = str()  #Registro de propósito general, de 16 bits hexadecimales (ejemplo 00FFh)
ip = hex(0x64)  #Registro que apunta a la siguiente dirección, de 16 bits hexadecimales (ejemplo 77AAh)

#Memoria de 16 bits, que almacena elementos de 8 bits hexadecimales (ejemplo FAh)
#NOTA: De 0 a 99 el espacio es reservado, de 100 a 1024 los usa la función cargar y de 1025 en adelante es de libre uso para programar
memoria = [hex(0x0)] * 65534 
parámetros = [""] * 10 #Vector utilizado para extraer parámetros de 8 bits hexadecimales de las operaciones (ejemplo B5h)

#Definimos una matriz que contenga las operaciones
filas = 5
columnas = 2  
matriz = [[str() for ind0 in range(columnas)] for ind1 in range(filas)]

#Inicializamos matriz: La primer columna tiene el código de operación, y el segundo cuántos parámetros hexadecimales de 8 bits le siguen. 
#Los elementos en la segunda columna nos indican cuántos elementos debemos cargar en el vector parámetros.
matriz[0][0] = "FF"
matriz[0][1] = "0"
matriz[1][0] = "A0"
matriz[1][1] = "3"
matriz[2][0] = "A1"
matriz[2][1] = "2"
matriz[3][0] = "A2"
matriz[3][1] = "2"
matriz[4][0] = "A3"
matriz[4][1] = "4"

"""
A partir de aquí se trabajarán los PROCESOS que permiten el funcionamiento de esta máquina virtual. 
"""

#Copiar archivo que contiene función "cargar"

#Copiar archivo que contiene función "obtener_parámetros"

#Copiar archivos de funciones que definan las operaciones