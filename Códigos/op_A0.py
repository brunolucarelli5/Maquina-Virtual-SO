def op_A0(parametro):
    dirección = str(parámetros[1]) + str(parámetros[2])
    dirección = int(dirección, 16)
    if dirección <= 65534 and dirección >= 1025:
        memoria[dirección] = parámetros[3]
    


