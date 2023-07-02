def op_C0(dirección, memoria): 
    resultado = ~(int(memoria[dirección],16)) & 255

    if dirección <= 65534 and dirección >= 1025:
       memoria[dirección] = resultado
       xp = dirección
    
       return xp
    else:
       print(" /!\ Error en la ejecución de C0: Dirección inválida /!\ ")


# input: 1010
# output deseado: 0101