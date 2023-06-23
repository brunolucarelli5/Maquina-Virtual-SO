"""
MÁQUINA VIRTUAL - SO 2023
Integrantes: Lucarelli, Monti, Mosconi, Terreno
"""

"""
DEFINICIÓN DE FUNCIONES
"""
def cargar(cod_binario, memoria):
    longitud = len(str(cod_binario))
    bandera = False
    instruc = ""
    hexa = ""
    a = 0
    b = 8
    i = 100

    while bandera != True: 
        instruc = str(cod_binario)[a:b]

        cadena = hex(int(instruc, 2)).upper()
        hexa = cadena[2:len(cadena)]
        if len(hexa) == 1:
            hexa = '0' + hexa

        memoria[i] = hexa
        i += 1

        a = b
        if b == (longitud) and i <= 1024:
            bandera = True
        b = b + 8

    return memoria  

def obtener_parámetros(ip,matriz,memoria,parámetros):
    #Inicialización de variables
    ip_decimal = int(ip,16)

    for i in range(filas):
        if memoria[ip_decimal] == matriz[i][0]:
            sigs_params = int(matriz[i][1])
            parámetros[0] = matriz[i][0]    #colocamos la operación en el primer elemento del vector

            for i in range(1,sigs_params+1):
                ip_decimal = ip_decimal + 1
                parámetros[i] = memoria[ip_decimal]
 
    #El puntero ip quedó en la posición del último parámetro. Le sumamos 1 para que quede posicionado en la siguiente instrucción.
    ip_decimal = ip_decimal + 1
    ip = hex(ip_decimal) 

    return ip

def op_A0(parámetros, memoria):
    dirección = str(parámetros[1]) + str(parámetros[2])
    dirección = int(dirección, 16)
    if dirección <= 65534 and dirección >= 1025:
        memoria[dirección] = parámetros[3]

def op_A1(parámetros, memoria):
    dirección = str(parámetros[1]) + str(parámetros[2])
    dirección = int(dirección, 16)
    if dirección <= 65534 and dirección >= 1025:
        memoria[dirección] = ip

def op_A2(parámetros, memoria):
    dirección = str(parámetros[1]) + str(parámetros[2])
    dirección = int(dirección, 16)
    if dirección <= 65534 and dirección >= 1025:
        ip = memoria[dirección]

def op_A3(parámetros, memoria):
    dirección_origen = str(parámetros[1]) + str(parámetros[2])
    dirección_origen = int(dirección_origen,16)
    dirección_destino = str(parámetros[3]) + str(parámetros[4])
    dirección_destino = int(dirección_destino,16)
    if (dirección_origen <= 65534 and dirección_origen >= 1025) and (dirección_destino <= 65534 and dirección_destino >= 1025):
        memoria[dirección_destino] = memoria[dirección_origen]

"""
A continuación se realizará la INICIALIZACIÓN DE VARIABLES, 
según los refinamientos planteados en https://docs.google.com/document/d/1d9OCoB_hRpRdz8k71dXcPaGg0XyF2U0yhzvx864gpnc/edit?usp=sharing
"""
xp = str()  #Registro de propósito general, de 16 bits hexadecimales (ejemplo 00FFh)
ip = hex(0x64)  #Registro que apunta a la siguiente dirección, de 16 bits hexadecimales (ejemplo 77AAh)

#Memoria de 16 bits, que almacena elementos de 8 bits hexadecimales (ejemplo FAh)
#NOTA: De 0 a 99 el espacio es reservado, de 100 a 1024 los usa la función cargar y de 1025 en adelante es de libre uso para programar
memoria = ["00"] * 65535 
parámetros = [""] * 10 #Vector utilizado para extraer parámetros de 8 bits hexadecimales de las operaciones (ejemplo B5h)

#Definimos una matriz que contenga las operaciones
filas = 5
columnas = 2  
matriz = [[str() for ind0 in range(columnas)] for ind1 in range(filas)]

#Inicializamos matriz: La primer columna tiene el código de operación, y el segundo cuántos parámetros hexadecimales de 8 bits le siguen. 
#Los elementos en la segunda columna nos indican cuántos elementos debemos cargar en el vector parámetros.
matriz[0][0] = "FF" #FFh
matriz[0][1] = "0"
matriz[1][0] = "A0" #A0h
matriz[1][1] = "3"
matriz[2][0] = "A1" #A1h
matriz[2][1] = "2"
matriz[3][0] = "A2" #A1
matriz[3][1] = "2"
matriz[4][0] = "A3" #A3h
matriz[4][1] = "4"

"""
A partir de aquí se trabajarán los PROCESOS que permiten el funcionamiento de esta máquina virtual. 
"""

#Cargamos el programa del archivo "ENTRADA.txt" en memoria
archivo = open("ENTRADA.txt","r")
memoria = cargar(archivo.read(),memoria)

#COSA DE PRUEBA - BORRAR DESPUÉS
memoria[int("0077",16)] = "33"

#Cargamos el vector parámetros 
#while parámetros[0] != "FF":
ip = obtener_parámetros(ip,matriz,memoria,parámetros)

print(parámetros)


if parámetros[0] == "A0":
    op_A0(parámetros, memoria)
elif parámetros[0] == "A1":
    op_A1(parámetros, memoria)
elif parámetros[0] == "A2":
    op_A2(parámetros, memoria)
elif parámetros[0] == "A3":
    op_A3(parámetros, memoria)            

print("finalizó ejecución")
#op_FF() #Generamos los archivos

print("debería ser 33:",memoria[int("FFFE",16)])
print("debería ser 16:",memoria[int("00FF", 16)])