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




#Cosas que ya están en main
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

#Cargamos memoria con un programa de ejemplo
memoria[100] = "A3" #op_A3(parámetros)
memoria[101] = "00"
memoria[102] = "77"
memoria[103] = "FF"
memoria[104] = "FF" 

memoria[105] = "A0" #op_A0(parámetros)
memoria[106] = "00"
memoria[107] = "FF"
memoria[108] = "16"

memoria[109] = "FF" #op_FF()

print("INICIO")
print(parámetros)

print("PRIMERA")
print(ip)
ip = obtener_parámetros(ip,matriz,memoria,parámetros)
print(parámetros)

print("SEGUNDA")
print(ip)
ip = obtener_parámetros(ip,matriz,memoria,parámetros)
print(parámetros)

print("TERCERA")
print(ip)
ip = obtener_parámetros(ip,matriz,memoria,parámetros)
print(parámetros)