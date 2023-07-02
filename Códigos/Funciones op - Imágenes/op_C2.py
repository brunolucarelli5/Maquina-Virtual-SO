def op_C2(parámetros, memoria):

   dirOrigen = int(concatenar_hex(parámetros[1], parámetros[2]),16)
   dirDestino = int(concatenar_hex(parámetros[3], parámetros[4]),16)

   if (dirOrigen <= 65534 and dirOrigen >= 1025) and (dirDestino <= 65534 and dirDestino >= 1025):
      resultado = int(memoria[dirOrigen], 16) | int(memoria[dirDestino], 16)
      memoria[dirDestino] = hex(resultado)
      xp = hex(dirDestino)
    
      return xp
   else:
       print(" /!\ Error en la ejecución de C2: Dirección inválida /!\ ")