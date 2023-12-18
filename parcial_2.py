#Peralta Perez Luka, LU: 1170204 
def menu():
    texto = []
    while True:
        opciones = ["\n1- Leer archivo", "2- Oponentes", "3- Perdidos Cap. Messi", "4- Cant. Ganados", "5- Exporta perdidos","0- Salir"]
        for op in opciones:
            print(op)
        try:
            usuario = int(input("Ingrese una opción: "))
        except:
            print("Ingrese una opción válida")
            continue
        if usuario not in range(len(opciones)):
            print("Ingrese una opción válida")
            continue
        elif usuario == 0:
            print("Saliendo...")
            break
        elif usuario == 1:
            texto,encabezado = leer_archivo()
        elif usuario == 2:
            if texto:
                oponentes(texto, encabezado)
            else:
                print('No hay datos')
        elif usuario == 3:
            if texto:
                perdidos_messi(texto,encabezado)
            else:
                print("No hay datos")
        elif usuario == 4:
            if texto:
                ganados(texto, encabezado)
            else:
                print('No hay datos')
        elif usuario == 5:
            if texto:
                exportar_perdidos(texto, encabezado)
            else:
                print("No hay datos")
                
                
def leer_archivo():
    texto = []
    encabezado = []
    try:
        with open("barcelona-la-liga-2020.csv", "rt", encoding="utf-8-sig") as archivo:
            texto = [linea.rstrip().split(";") for linea in archivo]
            encabezado = [texto.pop(0)]
    except Exception as e:
        print(f"Archivo no encontrado...{e}")
        return texto
    else:
        print("\nArchivo Encontrado")
        return texto, encabezado

def oponentes(texto, encabezado):
    if texto:
        oponentes = {valor: elemento for valor, elemento in enumerate(sorted(set([linea[3] for linea in texto[1:]])), start = 1)}
        print(oponentes)
        while True:
            try:
                usuario = int(input("Ingrese una opción: "))
                if usuario not in oponentes:
                    print("Valor fuera de rango")
                    continue
                else:
                    for linea in texto:
                        if linea[3] == oponentes.get(usuario):
                            print("|".join(linea))
            except Exception as e:
                print(e)
                return oponentes(texto, encabezado)
                
def perdidos_messi(texto,encabezado):
    for linea in texto[1:]:
        if linea[2].upper() == "P" and linea[4].upper() == "LIONEL MESSI":
            print("|". join(linea))
    
    
    
def ganados(texto, encabezado):
    partidos_ganados = [linea[2] for linea in texto if linea[2].upper() == 'G']
    ganados = partidos_ganados.count('G')
    print(f'\nlos partidos ganados totales son: {ganados}')

def exportar_perdidos(texto, encabezado):
    partidos = [';'.join(linea) + '\n' for linea in texto if linea[2] == 'P']
    enc = [';'.join(linea) + '\n' for linea in encabezado]
    try:
        with open('partidos_perdidooss.csv', 'wt', encoding = 'utf-8-sig') as arch:
            for j in enc:
                arch.write(j)
                for linea in partidos:
                    arch.write(linea)
    except Exception as e:
        print(e)
    else:
        print('Se creo correctamente')
 
    
                   
menu()