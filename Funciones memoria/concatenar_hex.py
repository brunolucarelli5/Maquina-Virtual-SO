def concatenar_hex(más_significativo, menos_significativo):
    a = más_significativo[2:len(más_significativo)]
    b = menos_significativo[2:len(menos_significativo)]

    if len(a) != 2:
        a = "0" + a
    if len(b) != 2:
        b = "0" + b

    concatenado = "0x" + (a+b)

    return concatenado

a = "0x0"
b = "0xC0"

print(concatenar_hex(a,b))