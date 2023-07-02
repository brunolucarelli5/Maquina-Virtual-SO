def op_B1(parámetros, memoria):
    dirección_salto = concatenar_hex(parámetros[0], parámetros[1])
    dirección_salto = int(dirección_salto, 16)
    ip_int = int(ip, 16)
    if direccion_salto >= 100 and direccion_salto <= 1025:
        return hex(direccion_salto)
    else:
        ip_int += 1
        return hex(ip_int), xp