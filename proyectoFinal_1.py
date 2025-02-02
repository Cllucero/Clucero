def getNotas():
    #carga la 3 notas de usuario
    notas=[]
    for i in range(3):
        aux=float(input(f"Ingrese la nota {i+1} correspondiente"))
        notas.append(aux)
        i+1
        #print(notas)
    return notas     

def getPromedio(notas):
    #funcion para calcular promedio
    return float(sum(notas)/len(notas))
    
def getEstado(notas):
    # para determinar la situación academica de estudiante, aprueba con más o igual de 7
    estadoP=False
    promedio=notas
    if promedio>=7:
        print(f"usted está aprobado con promedio {promedio} ")
        estado=True
    else:
        print(f"Su promedio de {promedio} no fue suficiente, está desaprobado")
print("Prueba_1: Calcular el Estado academico")
getEstado(getPromedio(getNotas()))