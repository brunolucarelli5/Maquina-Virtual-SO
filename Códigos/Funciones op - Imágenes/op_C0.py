def op_C0(parámetros, memoria): 

   dirección = int(concatenar_hex(parámetros[1], parámetros[2]),16)
   

   if dirección <= 65534 and dirección >= 1025:
      resultado = ~(int(memoria[dirección],16)) & 255
      memoria[dirección] = hex(resultado)
      xp = hex(dirección)
    
      return xp
   else:
      print(" /!\ Error en la ejecución de C0: Dirección inválida /!\ ")