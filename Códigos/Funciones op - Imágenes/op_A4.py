def op_A4(parámetros, memoria):
	dirección_origen = concatenar_hex(parámetros[1], parámetros[2])
	origen_decimal = int(dirección_origen, 16)
	if dirección_origen >=1025 and dirección_origen <= 65534:
		contenido = memoria[origen_decimal]
		dirección_destino = int(xp, 16)
		memoria[dirección_destino] = contenido
		xp = hex(dirección_destino)
		return xp
	else:
		print(" /!\ Error en la ejecución de A4: Dirección inválida /!\ ")