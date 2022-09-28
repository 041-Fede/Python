"""Pedir al usuario que ingrese dos números por teclado e imprimir """

NroPrimario = int(input("INFORME numero: "))
NroSecundario = int(input("INFORME numero siguiente: "))

def Operaciones(NroPrimario, NroSecundario):

    print("La suma de ambos:", NroPrimario + NroSecundario)

    if(NroPrimario > NroSecundario):
        print("La resta de ambos: ", NroPrimario - NroSecundario)
    else:
        print("La resta de ambos: ", NroSecundario - NroPrimario)

    print("La multiplicacion de ambos", NroPrimario * NroSecundario)
    
    if(NroSecundario != 0):
        print("La division entera de ambos: ", int(NroPrimario / NroSecundario))
        print("La division decimal de ambos", NroPrimario / NroSecundario)
    else:
        print("ERROR")

Operaciones(NroPrimario,NroSecundario)






