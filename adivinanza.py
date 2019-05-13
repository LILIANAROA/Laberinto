#juego de adivinar el numero,todos juntos,
#adivinar un numero generado aleatoriomente,
#ir introduciendo por teclado el dato a adivinar 
from randomb import randint
generado=randint(0,10)
#print(generado) #trampa
condicion:True
intento=10
while condicion:
    if intento>0:
    numero=input("Dame un numero del o al 10: ")
    if generado==int(numero):
       print("ganaste una anvurgesa que Lore paga")
       condicion=Flase 
    else:
       print("El perdedor compra pizza a Lore")
       print("te quedad",intento"intentos")

    else:
        condicion=False
        print("perdiste")

