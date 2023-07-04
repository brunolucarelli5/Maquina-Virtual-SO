def op_A1(parámetros, memoria,ip):
    error = "0"
    dirección = concatenar_hex(parámetros[1],parámetros[2])
    dirección = int(dirección, 16)
    if dirección <= 65534 and dirección >= 1025:
        if len(ip) == 4:
            ip = "0x0" + ip[len(ip) - 2 :]
        
        ip1 = hex(int(ip[3:4], 16))
        ip2 = hex(int(ip[len(ip)-2:], 16))

        memoria[dirección] = ip1
        memoria[dirección + 1] = ip2
        
        return error
    else:
        error = "1"
        print(" /!\ Error en la ejecución de A1: Dirección inválida /!\ ")
        return error