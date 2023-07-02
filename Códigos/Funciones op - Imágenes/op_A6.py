def op_A6(parámetros, memoria):
	dirección_destino = int(concatenar_hex(parámetros[1], parámetros[2]), 16)
    dirección_destino_siguiente = int(hex(destino_decimal + 1), 16)
	destino_decimal = int(dirección_destino, 16)
	if dirección_destino >=1025 and dirección_destino <= 65533:
		x = xp[2:4]
		p = xp[4:]
		memoria[dirección_destino] = x
		memoria[dirección_destino_siguiente] = p
		xp = hex(dirección_destino_siguiente)
		return xp
	else:
		print(" /!\ Error en la ejecución de A6: Dirección inválida /!\ ")