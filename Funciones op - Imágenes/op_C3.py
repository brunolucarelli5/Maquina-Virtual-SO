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