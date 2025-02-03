print("Empecemos a jugar,el P1 va a elegir 5 numeros al azar , para ingresar en una bolsa, luego el otro participante P2 va intentar adivinar")
print("P1: Ingrese uno de los numeros para adivinar")
aux=input()
bolsa = []
bolsa.append(aux)
ganador=1
i=1

for i in range (4):
    aux=input("ingrese otro numero")
    bolsa.append(aux)
    
    if aux.isalpha()==True :
        bolsa.pop()
        print("ingreso un valor no validos, solo numero. sera reemplazado por un 0")
        bolsa.append("0")
    else :
        
        print(f"Usted a ingresado {len(bolsa)} numero de 5")
        
print(f"ya ingreso todos los numero para jugar, ahora deje a P2")

p2=input("P2: elige 1 numero para adivinar en 5 que el P1 elegio.. suerte")

for elemento in bolsa :
    i+1
    if elemento==p2 :
        ganador= 2


if ganador == 2 :
      print(f"El jugador P2 ha ganado, con el numero {p2} el jugado P1 coloco en la posicion {i} ")
else :
      print(f"El jugador P1 ha ganado sus numeros fueron {bolsa} y el P2 eleigio{p2}")


print("GRACIAS POR JUGAR")