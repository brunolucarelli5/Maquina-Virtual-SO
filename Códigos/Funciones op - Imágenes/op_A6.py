def op_A5(parámetros, memoria):
	dirección_destino = concatenar_hex(parámetros[1], parámetros[2])
    destino_decimal = int(dirección_destino, 16)
    dirección_destino_siguiente = hex(destino_decimal + 1)
	destino_decimal = int(dirección_destino, 16)
	if destino_decimal >=1025 and destino_decimal <= 65533:
		x = xp[2:4]
		p = xp[4:]
		memoria[dirección_destino] = x
		dirección[dirección_destino_siguiente] = p
		estado = 0
	else:
		estado = 6
    return estado
