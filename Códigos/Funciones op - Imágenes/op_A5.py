def op_A5(parámetros,memoria):
	dirección_destino = int(concatenar_hex(parámetros[1], parámetros[2]), 16)
	destino_decimal = int(dirección_destino, 16)
	if destino_decimal >=1025 and destino_decimal <= 65534:
		dirección_origen = int(xp, 16)
		contenido = memoria[dirección_origen]
		memoria[dirección_destino] = contenido
		xp = hex(dirección_destino)
		return xp
	else: 
		print(" /!\ Error en la ejecución de A5: Dirección inválida /!\ ")