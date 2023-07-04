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