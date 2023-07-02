def op_B1(parámetros):
    dirección_salto = concatenar_hex(parámetros[1], parámetros[2])
    dirección_salto = int(dirección_salto, 16)

    if (dirección_salto <= 1024 and dirección_salto >= 100):
        ip = hex(dirección_salto)
    else:
        print(" /!\ Error en la ejecución de B0: Dirección inválida /!\ ")

    return ip