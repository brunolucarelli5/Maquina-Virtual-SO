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

    return hex(int(xp,16))


#Operaciones de movimiento
def op_A0(parámetros, memoria):
    error = "0"
    dirección = concatenar_hex(parámetros[1],parámetros[2])
    dirección = int(dirección, 16)
    if dirección <= 65534 and dirección >= 1025:
        memoria[dirección] = parámetros[3]
        
        return error
    else:
        error = "1"
        print(" /!\ Error en la ejecución de A0: Dirección inválida /!\ ")
        return error

def op_A1(parámetros, memoria,ip):
    error = "0"
    dirección = concatenar_hex(parámetros[1],parámetros[2])
    dirección = int(dirección, 16)
    if dirección <= 65533 and dirección >= 1025:
        if len(ip) == 4:
            ip = "0x0" + ip[len(ip) - 2 :]
        
        ip1 = hex(int(ip[2:3], 16))
        ip2 = hex(int(ip[len(ip)-2:], 16) - 1)

        memoria[dirección] = ip1
        memoria[dirección + 1] = ip2
        
        return error
    else:
        error = "1"
        print(" /!\ Error en la ejecución de A1: Dirección inválida /!\ ")
        return error

def op_A2(parámetros, memoria,ip):
    error = "0"
    vector_auxiliar = [""] * 2

    dirección = concatenar_hex(parámetros[1],parámetros[2])
    dirección = int(dirección, 16)

    if dirección <= 65533 and dirección >= 1025:

        valor_ip = hex(int(concatenar_hex(memoria[dirección],memoria[dirección+1]),16))

        if int(valor_ip,16) <= 1024 and int(valor_ip,16) >= 100:

            vector_auxiliar[0] = error
            vector_auxiliar[1] = valor_ip
            
            return vector_auxiliar
    else:
        error = "1"
        print(" /!\ Error en la ejecución de A2: Dirección inválida /!\ ")
        vector_auxiliar[0] = error
        vector_auxiliar[1] = ip
            
        return vector_auxiliar

def op_A3(parámetros, memoria):
    error = "0"
    dirección_origen = concatenar_hex(parámetros[1],parámetros[2])
    dirección_origen = int(dirección_origen,16)
    dirección_destino = concatenar_hex(parámetros[3],parámetros[4])
    dirección_destino = int(dirección_destino,16)
    if (dirección_origen <= 65534 and dirección_origen >= 1025) and (dirección_destino <= 65534 and dirección_destino >= 1025):
        memoria[dirección_destino] = memoria[dirección_origen]
        return error
    else:
        error = "1"
        print(" /!\ Error en la ejecución de A3: Dirección inválida /!\ ")
        return error

def op_A4(parámetros, memoria):
    error = "0"
    dirección_origen = int(concatenar_hex(parámetros[1], parámetros[2]),16)
    
    if dirección_origen >= 1025 and dirección_origen <= 65534:
        contenido = memoria[dirección_origen]
        dirección_destino = int(xp, 16)

        memoria[dirección_destino] = contenido

        return error

    else:
        error = "1"
        print(" /!\ Error en la ejecución de A4: Dirección inválida /!\ ")
        return error

def op_A5(parámetros, memoria):
    error = "0"
    dirección_destino = int(concatenar_hex(parámetros[1], parámetros[2]), 16)

    if dirección_destino >= 1025 and dirección_destino <= 65534:
        dirección_origen = int(xp, 16)
        contenido = memoria[dirección_origen]
        memoria[dirección_destino] = contenido

        return error
    else: 
        error = "1"
        print(" /!\ Error en la ejecución de A5: Dirección inválida /!\ ")
        return error

def op_A6(parámetros, memoria):
    error = "0"
    dirección_destino = int(concatenar_hex(parámetros[1], parámetros[2]), 16)
    dirección_destino_siguiente = dirección_destino + 1

    if dirección_destino >=1025 and dirección_destino <= 65533:
        x = hex(int(xp[2:4],16))
        p = hex(int(xp[4:len(xp)],16))
        memoria[dirección_destino] = x
        memoria[dirección_destino_siguiente] = p

        return error
    else: 
        error = "1"
        print(" /!\ Error en la ejecución de A6: Dirección inválida /!\ ")
        return error

def op_A7(parámetros, memoria,xp):
    error = "0"
    vector_auxiliar = [""] * 2
    dirección_origen = int(concatenar_hex(parámetros[1], parámetros[2]), 16) 
    dirección_origen_siguiente = dirección_origen + 1
        
    if dirección_origen >= 1025 and dirección_origen <= 65533:
        contenido = memoria[dirección_origen] + memoria[dirección_origen_siguiente][2:]
        xp = contenido
        vector_auxiliar[0] = error
        vector_auxiliar[1] = xp

        return vector_auxiliar
    else: 
        error = "1"
        print(" /!\ Error en la ejecución de A7: Dirección inválida /!\ ")
        vector_auxiliar[0] = error
        vector_auxiliar[1] = xp

        return vector_auxiliar

#OPERACIONES DE SALTO
def op_B0(parámetros, memoria,ip):
    #El primer elemento del vector es el estado de ejecución, el segundo es el valor de IP
    error = "0"
    vector_auxiliar = [""] * 2

    dirección_salto = concatenar_hex(parámetros[1], parámetros[2])
    dirección_salto = int(dirección_salto, 16)

    dirección_verificación = concatenar_hex(parámetros[3], parámetros[4])
    dirección_verificación = int(dirección_verificación, 16)

    if (dirección_salto <= 1024 and dirección_salto >= 100) and (dirección_verificación <= 65534 and dirección_verificación >= 1025):

        if memoria[dirección_verificación] == hex(0x0):
            ip = hex(dirección_salto)

            vector_auxiliar[0] = error
            vector_auxiliar[1] = ip
            return vector_auxiliar
        
        else:
            vector_auxiliar[0] = error
            vector_auxiliar[1] = ip
            return vector_auxiliar
            
    else:
        error = "1"
        print(" /!\ Error en la ejecución de B0: Dirección inválida /!\ ")
        vector_auxiliar[0] = error
        vector_auxiliar[1] = ip

        return vector_auxiliar

def op_B1(parámetros,ip):
    error = "0"
    vector_auxiliar = [""] * 2
    dirección_salto = concatenar_hex(parámetros[1], parámetros[2])
    dirección_salto = int(dirección_salto, 16)

    if (dirección_salto <= 1024 and dirección_salto >= 100):
        ip = hex(dirección_salto)
        vector_auxiliar[0] = error
        vector_auxiliar[1] = ip
    else:
        error = "1"
        print(" /!\ Error en la ejecución de B1: Dirección inválida /!\ ")
        vector_auxiliar[0] = error
        vector_auxiliar[1] = ip

        return vector_auxiliar

"""
OPERACIONES LÓGICAS
"""
def op_C0(parámetros, memoria):
   error = "0"
   dirección = int(concatenar_hex(parámetros[1], parámetros[2]),16)
   
   if dirección <= 65534 and dirección >= 1025:
      rdo_not = bin(int(memoria[dirección],16) ^ int("0xff",16)) #hacemos la compuerta not con un xor a ff
      memoria[dirección] = hex(int(rdo_not,2))
      
      return error
   
   else:
      error = "1"
      print(" /!\ Error en la ejecución de C0: Dirección inválida /!\ ")
      return error

def op_C1(parámetros, memoria):
   error = "0"
   dirOrigen = int(concatenar_hex(parámetros[1], parámetros[2]),16)
   dirDestino = int(concatenar_hex(parámetros[3], parámetros[4]),16)

   if (dirOrigen <= 65534 and dirOrigen >= 1025) and (dirDestino <= 65534 and dirDestino >= 1025):
      resultado = int(memoria[dirOrigen], 16) & int(memoria[dirDestino], 16)
      memoria[dirDestino] = hex(resultado)
    
      return error
   else:
       error = "1"
       print(" /!\ Error en la ejecución de C1: Dirección inválida /!\ ")
       return error

def op_C2(parámetros, memoria):
    error = "0"
    dirOrigen = int(concatenar_hex(parámetros[1], parámetros[2]),16)
    dirDestino = int(concatenar_hex(parámetros[3], parámetros[4]),16)

    if (dirOrigen <= 65534 and dirOrigen >= 1025) and (dirDestino <= 65534 and dirDestino >= 1025):
        resultado = int(memoria[dirOrigen], 16) | int(memoria[dirDestino], 16)
        memoria[dirDestino] = hex(resultado)

        return error
    else:
        error = "1"
        print(" /!\ Error en la ejecución de C2: Dirección inválida /!\ ")
        return error

def op_C3(parámetros, memoria):
    error = "0"
    dirOrigen = int(concatenar_hex(parámetros[1], parámetros[2]),16)
    dirDestino = int(concatenar_hex(parámetros[3], parámetros[4]),16)

    if (dirOrigen <= 65534 and dirOrigen >= 1025) and (dirDestino <= 65534 and dirDestino >= 1025):
        resultado = int(memoria[dirOrigen], 16) ^ int(memoria[dirDestino], 16)
        memoria[dirDestino] = hex(resultado)

        return error
    else:
        error = "1"
        print(" /!\ Error en la ejecución de C3: Dirección inválida /!\ ")
        return error


"""
OPERACIONES ARITMÉTICAS
"""
def op_D0(parámetros, memoria):
    error = "0"
    dirección_origen = int(concatenar_hex(parámetros[1],parámetros[2]), 16)
    dirección_destino = int(concatenar_hex(parámetros[3],parámetros[4]), 16)

    if (dirección_origen <= 65534 and dirección_origen >= 1025) and (dirección_destino <= 65534 and dirección_destino >= 1025):
        sumando1 = int(memoria[dirección_origen], 16)
        sumando2 = int(memoria[dirección_destino], 16)
        suma = sumando1 + sumando2
        
        #Se toman los bits más significativos en caso de ser necesario
        if suma > 255 or suma < 0:
            suma = hex(suma)
            suma = "0x" + suma[len(suma) - 2 :]
        else:
            suma = hex(suma)
        memoria[dirección_destino] = suma   
        
        return error
    else:
        error = "1"
        print(" /!\ Error en la ejecución de D0: Dirección inválida /!\ ")
        return error

def op_D1(parámetros, memoria):
    error = "0"
    dirección_origen = concatenar_hex(parámetros[1],parámetros[2])
    dirección_origen = int(dirección_origen, 16)
    dirección_destino = concatenar_hex(parámetros[3],parámetros[4])
    dirección_destino = int(dirección_destino,16)

    if (dirección_origen <= 65534 and dirección_origen >= 1025) and (dirección_destino <= 65534 and dirección_destino >= 1025):
        resultado = int(memoria[dirección_origen],16) - int(memoria[dirección_destino],16)
        resultado = hex(abs(resultado))

        #Tomamos el bit menos significativo
        if int(resultado,16) > 255 or int(resultado,16) < 0:
            resultado = hex(resultado)
            resultado = "0x"+resultado[len(resultado)-2:len(resultado)]

        memoria[dirección_destino] = hex(int(resultado,16))

        return error
    else:
        error = "1"
        print(" /!\ Error en la ejecución de D1: Dirección inválida /!\ ")
        return error

def op_D2(parámetros, memoria):
    error = "0"
    dirección_origen = concatenar_hex(parámetros[1],parámetros[2])
    dirección_origen = int(dirección_origen, 16)
    dirección_destino = concatenar_hex(parámetros[3],parámetros[4])
    dirección_destino = int(dirección_destino,16)

    if (dirección_origen <= 65534 and dirección_origen >= 1025) and (dirección_destino <= 65534 and dirección_destino >= 1025):
        resultado = int(memoria[dirección_destino],16) % int(memoria[dirección_origen],16)

        #MOD nunca será mayor a 0xff, por lo que no hace falta verificar
        memoria[dirección_destino] = hex(resultado)

        return error
    else:
        error = "1"
        print(" /!\ Error en la ejecución de D2: Dirección inválida /!\ ")
        return error


"""
I N I C I A L I Z A C I Ó N  D E  V A R I A B L E S
"""
#LIBRERÍAS
import os.path


#CARGA DE DATOS DE ENTRADA
inválido = False    #Ayuda a cargar datos de entrada
error = "0"  #Determina si la ejecución de una función fue fuera de las direcciones permitidas. 1 = hubo un error.
dirección = "0"
valor = "0"


#REGISTROS
xp = hex(0x0)  #Registro de propósito general, de 16 bits hexadecimales (ejemplo 00FFh)
ip = hex(0x0)  #Registro que apunta a la siguiente dirección, de 16 bits hexadecimales (ejemplo 77AAh)

#MEMORIA de 16 bits, que almacena elementos de 8 bits hexadecimales (ejemplo FAh)
#NOTA: De 0 a 99 el espacio es reservado, de 100 a 1024 los usa la función cargar y de 1025 en adelante es de libre uso para programar
memoria = [hex(0x0)] * 65535
parámetros = [""] * 10 #Vector utilizado para extraer parámetros de 8 bits hexadecimales de las operaciones (ejemplo B5h)

#Definimos una matriz que contenga las operaciones
filas = 19
columnas = 2  
matriz = [[str() for ind0 in range(columnas)] for ind1 in range(filas)]

#Inicializamos matriz: La primer columna tiene el código de operación, y el segundo cuántos parámetros hexadecimales de 8 bits le siguen. 
#Los elementos en la segunda columna nos indican cuántos elementos debemos cargar en el vector parámetros.
matriz[0][0] = "0xf0" #Memory dump
matriz[0][1] = "0"
matriz[1][0] = "0xf1" #HLT
matriz[1][1] = "0"
matriz[2][0] = "0xa0"
matriz[2][1] = "3"
matriz[3][0] = "0xa1"
matriz[3][1] = "2"
matriz[4][0] = "0xa2"
matriz[4][1] = "2"
matriz[5][0] = "0xa3"
matriz[5][1] = "4"      
matriz[6][0] = "0xa4"
matriz[6][1] = "2"
matriz[7][0] = "0xa5"
matriz[7][1] = "2"
matriz[8][0] = "0xa6"
matriz[8][1] = "2"
matriz[9][0] = "0xa7"
matriz[9][1] = "2"
matriz[10][0] = "0xb0"
matriz[10][1] = "4"
matriz[11][0] = "0xb1"
matriz[11][1] = "2"
matriz[12][0] = "0xc0"
matriz[12][1] = "2"
matriz[13][0] = "0xc1"
matriz[13][1] = "4"
matriz[14][0] = "0xc2"
matriz[14][1] = "4"
matriz[15][0] = "0xc3"
matriz[15][1] = "4"
matriz[16][0] = "0xd0"
matriz[16][1] = "4"
matriz[17][0] = "0xd1"
matriz[17][1] = "4"
matriz[18][0] = "0xd2"
matriz[18][1] = "4"

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

#MANEJADOR DE FUNCIONES
while parámetros[0] != "0xf1" and error == "0":
    error = "0"
    ip = obtener_parámetros(ip,matriz,memoria,parámetros)
    #print(ip,int(ip,16),parámetros) #permite ver la evolución del registro ip y el vector parámetros

    if parámetros[0] == "0xf0":
        op_F0(memoria,xp,ip) #Generamos el archivo memory_dump, que nos mostrará cómo quedó la memoria después del programa
    
    #Operaciones de movimiento
    elif parámetros[0] == "0xa0":
        error = op_A0(parámetros, memoria)
    elif parámetros[0] == "0xa1":
        error = op_A1(parámetros, memoria,ip)
    elif parámetros[0] == "0xa2":
        vector_auxiliar = [""] * 2
        vector_auxiliar = op_A2(parámetros,memoria,ip)
        
        error = vector_auxiliar[0]
        ip = vector_auxiliar[1]
        
    elif parámetros[0] == "0xa3":
        error = op_A3(parámetros, memoria)
    elif parámetros[0] == "0xa4":
        error = op_A4(parámetros, memoria)
    elif parámetros[0] == "0xa5":
        error = op_A5(parámetros, memoria)
    elif parámetros[0] == "0xa6":
        error = op_A6(parámetros, memoria)
        
    elif parámetros[0] == "0xa7":
        vector_auxiliar = [""] * 2
        vector_auxiliar = op_A7(parámetros,memoria,xp)
        
        error = vector_auxiliar[0]
        xp = vector_auxiliar[1]
         
    #Operación JMP
    elif parámetros[0] == "0xb0":
        vector_auxiliar = [""] * 2
        vector_auxiliar = op_B0(parámetros,memoria,ip)
        
        error = vector_auxiliar[0]
        ip = vector_auxiliar[1]

    elif parámetros[0] == "0xb1":
        ip = op_B1(parámetros,ip)
    
    #Operaciones lógicas
    elif parámetros[0] == "0xc0":
        error = op_C0(parámetros, memoria) 
    elif parámetros[0] == "0xc1":
        error = op_C1(parámetros, memoria)
    elif parámetros[0] == "0xc2":
        error = op_C2(parámetros, memoria)
    elif parámetros[0] == "0xc3":
        error = op_C3(parámetros, memoria)
    
    #Operaciones aritméticas
    elif parámetros[0] == "0xd0":
        error = op_D0(parámetros, memoria)
    elif parámetros[0] == "0xd1":
        error = op_D1(parámetros, memoria) 
    elif parámetros[0] == "0xd2":
        error = op_D2(parámetros, memoria)               
            
print("FIN DE EJECUCIÓN")