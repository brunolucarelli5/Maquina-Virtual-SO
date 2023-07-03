def op_C0(parámetros, memoria):
   error = "0"
   dirección = int(concatenar_hex(parámetros[1], parámetros[2]),16)
   
   if dirección <= 65534 and dirección >= 1025:
      rdo_not = bin(int(memoria[dirección],16) ^ int("0xff",16)) #hacemos la compuerta not con un xor a ff
      memoria[dirección] = hex(int(rdo_not,2))
      
      return error
   
   else:
      error = "1"
      print(" /!\ Error en la ejecución de C0: Dirección inválida /!\ ")
      return error