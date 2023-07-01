def op_A4(parámetros, memoria):
	dirección_origen = concatenar_hex(parámetros[1], parámetros[2])
	origen_decimal = int(dirección_origen, 16)
	if dirección_origen >=1025 and dirección_origen <= 65534:
		contenido = memoria[dirección_origen]
		dirección_destino = xp
		memoria[dirección_destino] = contenido
		estado = 0 
	else:
		estado = 4
    return estado