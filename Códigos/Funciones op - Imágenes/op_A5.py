def op_A5(parámetros,memoria):
	dirección_destino = concatenar_hex(parámetros[1], parámetros[2])
	destino_decimal = int(dirección_destino, 16)
	if destino_decimal >=1025 and destino_decimal <= 65534:
		dirección_origen = xp
		contenido = memoria[dirección_origen]
		memoria[dirección_destino] = contenido
		xp = dirección_destino
		estado = 0 
	else:
		estado = 5
    return estado
