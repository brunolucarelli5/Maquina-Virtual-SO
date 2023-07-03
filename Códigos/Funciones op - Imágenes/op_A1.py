def op_A1(parámetros, memoria,ip):
    dirección = concatenar_hex(parámetros[1],parámetros[2])
    dirección = int(dirección, 16)
    if dirección <= 65534 and dirección >= 1025:
        memoria[dirección] = hex(int(ip,16) - int("0x1",16))     #restamos 2 porque el puntero se coloca al final de los parámetros después de leerlos 

        xp = hex(dirección)
        return xp
    else:
        print(" /!\ Error en la ejecución de A1: Dirección inválida /!\ ")