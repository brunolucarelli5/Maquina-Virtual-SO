def op_F1(memoria,xp,ip):
    # Si no existe, se crea el archivo
    archivo = open("memory_dump.txt", "w+")

    archivo.write("------------------------REGISTROS-------------------\n")
    archivo.write("xp, " + str(xp) + "\n")
    archivo.write("ip, " + str(ip) + "\n")

    archivo.write("------------------------MEMORIA---------------------\n")
    archivo.write("DIR,VAL"+"\n")

    for i in range(65535):
        archivo.write(str(hex(i))+","+str(memoria[i])+"\n")

    archivo.close()