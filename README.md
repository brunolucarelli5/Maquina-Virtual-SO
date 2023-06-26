


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

- Opcode 0xA0: Mueve una constante a una posición de memoria. Recibe dos parámetros, primero la dirección de memoria y luego el valor.

- Opcode 0xA1: Mueve el contenido del registro IP a una posición de memoria. Recibe como parámetro la posición de memoria inicial. Tome en cuenta que los registros son de 16 bits, con lo cual almacenara los primeros 8 en
la dirección recibida como parámetro y los restantes en la posición de memoria siguiente.

- Opcode 0xA2: Mueve el contenido de una posición de memoria al registro IP. Recibe como parámetro la posición de memoria inicial. Tome en cuenta que los registros son de 16 bits, con lo cual obtendrá los primeros 8 en la dirección recibida como parámetro y los restantes en la posición de memoria siguiente.

- Opcode 0xA3: Mueve valores entre posiciones
de memoria. Recibe dos parámetros, el primero es la posición de memoria de origen, y el segundo es la posición de memoria de destino.

 - Opcode 0xA4: Mueve el valor desde una posición de memoria, a la posición de memoria que contiene XP. Es decir, si XP contiene D1FA el valor se moverá a esa dirección de memoria. Recibe sólo un parámetro, la posición de memoria de origen, ya que el destino se encuentra en XP.

- Opcode 0xA5: Mueve el valor desde la posición de memoria que contiene XP, a otra posición de memoria. Es decir, si XP contiene el D1FA el valor se moverá desde esa dirección de memoria a otra que se recibe como parámetro. Recibe sólo un parámetro, la posición de memoria de destino, ya que el origen se encuentra en XP.

- Opcode 0xA6: Mueve el contenido de XP a una posición de memoria. En este caso si se mueve el contenido de XP, es decir, si XP contiene D1FA, D1 se movera a la posición de memoria recibida como parámetro y FA a la posición siguiente. Recibe sólo un parámetro, que es la posición de memoria de destino.

- Opcode 0xA7: Mueve el contenido de una posición de memoria a XP. Sólo recibe como parámetro la posición de memoria de origen. Tomar en cuenta nuevamente que XP es de 16 bits, por lo tanto se utilizaran la posición de memoria como parámetro y la siguiente para rellenar XP.

### Operación JMP

- Opcode 0xB0: Salto condicional. Recibe dos parámetros, el primero es la dirección a saltar, si la posición de memoria apuntada por el segundo parametro contiene 0. Es decir, si el segundo parametro es D1F4 y en esa posición de memoria contiene un 0, se salta a la dirección que ofrece el primer parámetro, de lo contrario se continua con la ejecución en la instrucción que sigue.

- Opcode 0xB1: Salto obligado. Recibe como parámetro la dirección de salto, y salta siempre.

### Operaciones lógicas

Todas las operaciones lógicas reciben 2 parámetros (excepto NOT), donde son las direcciones de memoria a operar, el resultado se almacena siempre en la posición de memoria que se recibe como segundo parámetro.

- Opcode 0xC0: Operación lógica NOT, es la única que recibe sólo 1 parámetro que es la posición de memoria a operar.

- Opcode 0xC1: AND entre las posiciones de memoria recibidas como parámetro.

- Opcode 0xC2: OR entre las posiciones de memoria recibidas como parámetro.

- Opcode 0xC3: XOR entre las posiciones de memoria recibidas como parámetro.

### Operaciones Aritméticas

Todas las operaciones aritméticas, al igual que las lógicas, reciben 2 parámetros, donde son las direcciones de memoria a operar, el resultado se almacena siempre en la posición de memoria que se recibe como segundo parámetro.

- Opcode 0xD0: ADD, suma el contenido de las posiciones de memoria recibidos como parámetros.

- Opcode 0xD1: SUB, suma el contenido de las posiciones de memoria recibidos como parámetros. El primer parámetro es el minuendo y el segundo el sustraendo.

- Opcode 0xD1: MOD, calcula el módulo del contenido de las posiciones de memoria recibidos. El primer parámetro es el divisor y el segundo el dividendo.

### Operaciones de sistema

- Opcode 0xF0: Dump de memoria, es decir, almacena todo el contenido de memoria (las 65536 posiciones) en un archivo que se llama mem.dump

- Opcode 0xF1: HALT, finaliza la ejecución del programa, todos los programas terminan con esta instrucción.
  
<b> Integrantes: </b> Lucarelli, Bruno; Mosconi, Ignacio; Monti, Agustín; Terreno, Valentino.



