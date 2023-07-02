def operacionOR (dirOrigen, dirDestino, memoria): 
    resultado = int(memoria[dirOrigen], 16) | int(memoria[dirDestino], 16)

    if (dirOrigen <= 65534 and dirOrigen >= 1025) and (dirDestino <= 65534 and dirDestino >= 1025):
       memoria[dirDestino] = resultado
       xp = dirDestino
    
       return xp
    else:
       print(" /!\ Error en la ejecución de C2: Dirección inválida /!\ ")