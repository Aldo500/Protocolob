pasos = []
subpasos = []
list(enumerate(pasos))
def menu():
    print("""---------Creador de protocolos-------------------
1.-Agregar paso a protocolo
2.-Borrar paso de protocolo
3.-Ver protocolo
0.-Salir
""")
def agreg():
    posi= int(input("Posición: "))
    paso = input("Escribe la instrucción que quieras agregar al protocolo: ")
    pasos.insert(posi,paso)
    print("------Protocolo------")
    for index, value in enumerate (pasos, start=1):
       print("{}.- {}".format(index, value))
def elim():
    pasoe = input("Escribe la instrucción que quieras eliminar: ")
    inde=int((pasos.index(pasoe)))
    pasos.pop(inde)
    print("-----Protocolo-----")
    for index, value in enumerate (pasos, start=1):
        print("{}.- {}".format(index, value))
def ver():
    print("-----Protocolo-----")
    for index, value in enumerate (pasos, start=1):
        print("{}.- {}".format(index, value))
    
    
while(True):  
    menu()
    resp = int (input("Escribe la opción que deseas utilizar: "))
    if resp == 1:
        agreg()
    elif resp == 2:
        elim()
    elif resp == 3:
        ver()
    elif resp == 0:
        print("Hasta luego")
        break
    
    
    
        
        
