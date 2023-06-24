"""
NOTA: Esta función extrae los hexadecimales como CADENA, con formato "0B". Consultar si debe ser en formato "0x0b".
Este cambio implica sólo un desfasaje en la subcadena que se imprime.

NOTA 2: La función trabaja los hexadecimales como cadena para preservar el 0 a la izquierda. Consultar si puede 
trabajarse así o si hay que trabajar todo como hex.
"""

def leer_binario(nombre_archivoBin):

    #Leyendo el binario nombre_archivo
    binario = open(nombre_archivoBin,"rb")

    binario = binario.read()
    print(binario)        
        #print(binario[0:1]) - Lee el primer campo definido entre los caracteres "\" y "\"

    #Leemos uno por uno los "campos" del binario. El primero no lo leemos porque es un enter
    for i in range(1,len(binario)):
        hexadecimal = str(binario[i:i+1]).upper()   #Lo hacemos mayúscula para que sea más fácil de leer

        #Los bloques en binario tienen el formato: b'\x(valorhexa)'. De la cadena hexadecimal nos sirve el contenido
        #a partir del caracter 4 hasta el penúltimo caracter. Al ser binario, mantiene los ceros a la izquierda, por
        #lo que no tendremos que añadirlos
        print(hexadecimal[4:len(hexadecimal)-1])

leer_binario("prog1.bin")