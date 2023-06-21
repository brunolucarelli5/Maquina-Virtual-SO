


<p></p><img src="https://github.com/ignamosconi/ASI/blob/master/Anexo/Im%C3%A1genes/Marca%20de%20agua%20SIMPLE%20-%20UTN%20FRVM.png" align-items="center" width="700" height="200">
<h2> TRABAJO PRÁCTICO - MÁQUINA VIRTUAL <br> SISTEMAS OPERATIVOS - ING EN SISTEMAS</br></h2>

<p> El presente trabajo se desarrolla en el marco de la materia Sistemas Operativos, dictada en la Universidad Tecnológica Nacional Facultad Regional Villa María; situada en Av. Universidad 450. </p>                                                        <h3> Características de la VM </h3>

La máquina virtual opera en BigEndian, dispone de un espacio de direcciones de 0 a 65535 y sus registros son de 16 bits.

### Mapeo de memoria

- De 0 a 99 - Es un espacio reservado
- De 100 a 1024 - Se carga el programa a ejecutar
- El resto de la memoria puede utilizarse libremente

### Registros

Dos registros de 16 bits

XP - Registro de propósito general

IP - Apunta la siguiente instrucción

## SET DE INSTRUCCIONES

### Operación MOV

- Opcode A0: Mueve una constante a una posición de memoria. Recibe dos parámetros, primero la dirección de memoria y luego el valor.

- Opcode A1: Mueve el contenido del registro IP a una posición de memoria. Recibe como parámetro la posición de memoria inicial. Tome en cuenta que los registros son de 16 bits, con lo cual almacenara los primeros 8 en
la dirección recibida como parámetro y los restantes en la posición de memoria siguiente.

- Opcode A2: Mueve el contenido de una posición de memoria al registro IP. Recibe como parámetro la posición de memoria inicial. Tome en cuenta que los registros son de 16 bits, con lo cual obtendrá los primeros 8 en la dirección recibida como parámetro y los restantes en la posición de memoria siguiente.

- Opcode A3: Mueve valores entre posiciones
de memoria. Recibe dos parámetros, el primero es la posición de memoria de origen, y el segundo es la posición de memoria de destino.

<b> Integrantes: </b> Lucarelli, Bruno; Mosconi, Ignacio; Monti, Agustín; Terreno, Valentino.



