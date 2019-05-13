#creamos un archivo nuevo
#guardar en la carpeta del repositorio
#con la extension
#uso de numeros aleatorios

#importamos la liberia randint
from random import randint
aleatorio=randint(0,20) #creamos una variable 
#y generamos un numero aleatorio entre 0 y 20
print(aleatorio) #imprimimos el numero generando
#ejercicio
#escribir una funcion sorteo() que reciba 
#una lista de participantes aleatoriamente, y 
#retornar esa persona elegida 
# desafio: no volver a retornar una persona
#  ya sorteada

from random import randint
participantes=["Jorge","Maria","Ana","Beatriz"]
def sorteo(lista_participantes):
    cant=len(lista_participantes)
    aleatorio=randint(0,cant)
    ganador=participantes[aleatorio]
    return ganador

sorteo(participantes)


