"""
MÁQUINA VIRTUAL - SO 2023
Integrantes: Lucarelli, Monti, Mosconi, Terreno
Refinamientos: Planteados en https://docs.google.com/document/d/1d9OCoB_hRpRdz8k71dXcPaGg0XyF2U0yhzvx864gpnc/edit?usp=sharing
"""

"""
F U N C I O N E S
"""
def cargar(nombre_archivoBin, memoria,ip):
    #Leemos el binario nombre_archivoBin
    binario = open(nombre_archivoBin,"rb")
    #Esta forma de leer nos extrae una cadena con solo los caracteres hexadecimales, que agruparemos de a 2
    binario = binario.read().hex()

    ip_dec = 100

    for i in range(0,len(binario),2):
        memoria[ip_dec] = hex(int(binario[i:i+2],16))
        ip_dec = ip_dec + 1

    return hex(ip_dec)    

def obtener_parámetros(ip,matriz,memoria,parámetros):
    #Inicialización de variables
    ip_decimal = int(ip,16) #La posición del puntero ip nos permite determinar dónde empezar a leer.

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

def concatenar_hex(más_significativo, menos_significativo):
    a = más_significativo[2:len(más_significativo)]
    b = menos_significativo[2:len(menos_significativo)]

    if len(a) != 2:
        a = "0" + a
    if len(b) != 2:
        b = "0" + b

    concatenado = "0x" + (a+b)

    return concatenado

def op_F0(memoria,xp,ip):
    # Si no existe, se crea el archivo
    archivo = open("memory_dump.txt", "w+")

    archivo.write("------------------------REGISTROS-------------------\n")
    archivo.write("xp, " + str(xp) + "\n")
    archivo.write("ip, " + str(ip) + "\n")

    archivo.write("------------------------MEMORIA---------------------\n")
    archivo.write("DIR,VAL"+"\n")

    for i in range(65535):
        archivo.write(str(hex(i))+","+str(memoria[i])+"\n")

    archivo.close()

def op_A0(parámetros, memoria):
    dirección = concatenar_hex(parámetros[1],parámetros[2])
    dirección = int(dirección, 16)
    if dirección <= 65534 and dirección >= 1025:
        memoria[dirección] = parámetros[3]
        return 0 #Operación exitosa: Devolvemos 0
    else:
        return 1 #Operación fallida: Devolvemos un entero positivo acorde a la documentación                  

def op_A1(parámetros, memoria):
    dirección = concatenar_hex(parámetros[1],parámetros[2])
    dirección = int(dirección, 16)
    if dirección <= 65534 and dirección >= 1025:
        memoria[dirección] = ip
        return 0 #Operación exitosa
    else:
        return 2 #Operación fallida

def op_A2(parámetros, memoria):
    dirección = concatenar_hex(parámetros[1],parámetros[2])
    dirección = int(dirección, 16)
    if dirección <= 65534 and dirección >= 1025:
        ip = memoria[dirección]
        return 0 #Operación exitosa
    else:
        return 3 #Operación fallida

def op_A3(parámetros, memoria):
    dirección_origen = concatenar_hex(parámetros[1],parámetros[2])
    dirección_origen = int(dirección_origen,16)
    dirección_destino = concatenar_hex(parámetros[3],parámetros[4])
    dirección_destino = int(dirección_destino,16)
    if (dirección_origen <= 65534 and dirección_origen >= 1025) and (dirección_destino <= 65534 and dirección_destino >= 1025):
        memoria[dirección_destino] = memoria[dirección_origen]
        return 0 #Operación exitosa
    else:
        return 4 #Operación fallida  


"""
I N I C I A L I Z A C I Ó N  D E  V A R I A B L E S
"""
#LIBRERÍAS
import os.path


#CARGA DE DATOS DE ENTRADA
inválido = False
dirección = "0"
valor = "0"
estado = 0 #nos informa el estado de ejecución de las funciones op. 0 es correcto, entero postivo es error.


#REGISTROS
xp = hex(0x0)  #Registro de propósito general, de 16 bits hexadecimales (ejemplo 00FFh)
ip = hex(0x0)  #Registro que apunta a la siguiente dirección, de 16 bits hexadecimales (ejemplo 77AAh)

#MEMORIA de 16 bits, que almacena elementos de 8 bits hexadecimales (ejemplo FAh)
#NOTA: De 0 a 99 el espacio es reservado, de 100 a 1024 los usa la función cargar y de 1025 en adelante es de libre uso para programar
memoria = [hex(0x0)] * 65535
parámetros = [""] * 10 #Vector utilizado para extraer parámetros de 8 bits hexadecimales de las operaciones (ejemplo B5h)

#MANEJADOR: Definimos una matriz que contenga las operaciones
filas = 5
columnas = 2  
matriz = [[str() for ind0 in range(columnas)] for ind1 in range(filas)]

#Inicializamos matriz: La primer columna tiene el código de operación, y el segundo cuántos parámetros hexadecimales de 8 bits le siguen. 
#Los elementos en la segunda columna nos indican cuántos elementos debemos cargar en el vector parámetros.
matriz[0][0] = "0xf1"
matriz[0][1] = "0"
matriz[1][0] = "0xa0"
matriz[1][1] = "3"
matriz[2][0] = "0xa1"
matriz[2][1] = "2"
matriz[3][0] = "0xa2"
matriz[3][1] = "2"
matriz[4][0] = "0xa3"
matriz[4][1] = "4"

"""
E N T R A D A S
Aquí se cargarán las entradas, que el código que se cargará en memoria usará para trabajar. 
"""

archivo = str(input("Ingrese el nombre del archivo a leer, extensión incluída: "))
while os.path.isfile(archivo) == False or archivo[len(archivo)-3:len(archivo)] != "bin":
    archivo = str(input("El archivo ingresado es inválido. Ingrese el nombre nuevamente, con extensión incluída: "))

os.system("cls")

print("Ingrese los datos de entrada que usará",archivo,", brindando la dirección y el valor en hexadecimal. Ejemplo: ")
print("Ingrese una dirección: 0xdd77")
print("Ingrese el valor en esa dirección: 0x33")

while dirección != "":
    print("--------------------------------------------------------------------------------------------------------------")
    dirección = str(input("Ingrese una dirección. Deje vacío para continuar: ")).lower()
    if dirección != "": 
        if int(dirección,16) >= 1025 and int(dirección,16) <= 65534 and len(dirección) == 6:
            print("---Dirección VÁLIDA---")
        else:
            invalido = True
            print("DIRECCIÓN INVÁLIDA, intente nuevamente:")
            while invalido == True:
                dirección = str(input("Ingrese una dirección. Deje vacío para continuar: ")).lower()
                if int(dirección,16) >= 1025 and int(dirección,16) <= 65534 and len(dirección) == 6:
                    print("---Dirección VÁLIDA---")
                    invalido = False
                else:
                    invalido = True
                    print("DIRECCIÓN INVÁLIDA, intente nuevamente:")

        invalido = False
        if dirección != "":
            valor = str(input("Ingrese el valor a cargar en la dirección: ")).lower()
            if int(valor,16) >= 0 and int(valor,16) <= 255 and len(valor) == 4:
                print("---Valor VÁLIDO---")
            else:
                invalido = True
                print("VALOR INVÁLIDO, intente nuevamente:")

                while invalido == True:
                    valor = str(input("Ingrese un valor. Deje vacío para salir: ")).lower()
                    if int(valor,16) >= 0 and int(valor,16) <= 255 and len(valor) == 4:
                        print("---Valor VÁLIDO---")
                        invalido = False
                    else:
                        invalido = True
                        print("VALOR INVÁLIDO, intente nuevamente:")

        memoria[int(dirección,16)] = hex(int(valor,16))
        print("El valor",valor,"fue cargado exitosamente en la dirección",dirección)

print("DATOS DE ENTRADA CARGADOS")
print("--------------------------------------------------------------------------------------------------------------")


"""
P R O C E S O S
"""
#Cargamos el programa del archivo dado por el usuario en memoria
print("Cargando programa",archivo)
ip = cargar(archivo,memoria,ip)
print("¡PROGRAMA CARGADO!")
print("--------------------------------------------------------------------------------------------------------------")


print("INICIO DE EJECUCIÓN")
#Cargamos el vector parámetros. Para ello tenemos que volver ip a la dirección donde inicia el programa (la n° 100)
ip = "0x64"
while parámetros[0] != "0xf1" and estado == 0:
    ip = obtener_parámetros(ip,matriz,memoria,parámetros)
    #print(ip,int(ip,16),parámetros) #permite ver la evolución del registro ip y el vector parámetros
    if parámetros[0] == "0xa0":
        estado = op_A0(parámetros, memoria)
        if estado != 0:
            print(" /!\ Error en la ejecución de A0: Dirección inválida /!\ ")

    elif parámetros[0] == "0xa1":
        estado = op_A1(parámetros, memoria)
        if estado != 0:
            print(" /!\ Error en la ejecución de A1: Dirección inválida /!\ ")

    elif parámetros[0] == "0xa2":
        estado = op_A2(parámetros, memoria)
        if estado != 0:
            print(" /!\ Error en la ejecución de A2: Dirección inválida /!\ ")

    elif parámetros[0] == "0xa3":
        estado = op_A3(parámetros, memoria)           
        if estado != 0:
            print(" /!\ Error en la ejecución de A3: Dirección inválida /!\ ")

print("FIN DE EJECUCIÓN --- Archivo memory_dump generado :)")
op_F0(memoria,xp,ip) #Generamos el archivo memory_dump, que nos mostrará cómo quedó la memoria después del programa