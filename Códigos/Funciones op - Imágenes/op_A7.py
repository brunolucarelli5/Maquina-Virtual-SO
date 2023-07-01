def op_A7(parámetros, memoria):
	dirección_origen = concatenar_hex(parámetros[1], parámetros[2])
    destino_decimal = int(dirección_origen, 16)
	dirección_origen_siguiente = hex(destino_decimal + 1)
	if destino_decimal >=1025 and destino_decimal <= 65533:
		contenido = memoria[dirección_origen] + memoria[dirección_origen_siguiente][2:]
		xp = contenido
		estado = 0
	else:
		estado = 7
    return estado
