def op_B0(parámetros, memoria):
    dirección_salto = concatenar_hex(parámetros[0], parámetros[1])
    dirección_salto = int(dirección_salto, 16)
    dirección_memoria = concatenar_hex(parámetros[2], parámetros[3])
    dirección_memoria = int(dirección_memoria, 16)
    if direccion_salto >= 100 and direccion_salto <= 1025:
        valor_memoria = memoria[direccion_memoria]
        if valor_memoria == 0:
            ip_int = int(direccion_salto, 16)
            xp = 0
            return hex(ip_decimal), xp
    ip_int = int(ip, 16)
    ip_int += 1
    xp = 0
    return hex(ip_int), xp