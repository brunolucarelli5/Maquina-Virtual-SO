def op_A5(parámetros,memoria,xp):
	dirección_destino = int(concatenar_hex(parámetros[1], parámetros[2]), 16)

	if dirección_destino >= 1025 and dirección_destino <= 65534:
		dirección_origen = int(xp, 16)
		contenido = memoria[dirección_origen]
		memoria[dirección_destino] = contenido
		xp = hex(dirección_destino)
		return xp
	else: 
         print(" /!\ Error en la ejecución de A5: Dirección inválida /!\ ")