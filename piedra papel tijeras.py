#Juego piedra papel y tijeras escito en python 3

#encoding:UTF-8
import random #importamos la libreria random que es la que se encarga de darnos  valores aleatorios

aleatorio = random.randrange(0, 3)  # ubicamos el rango en el que queremos que escoja las opciones aleatorias 
elijePc = ""   #la maquina escoje un valor aleatorio de nuestra lista anterior    
print("1)Piedra")
print("2)Papel")
print("3)Tijera")
opcion = int(input("Que elijes: ")) #le decimos al usuario que elija una de las opciones 

if opcion == 1:    #si la opcion que escoge el usuario es 1 entonces se le asigna piedra
    elijeUsuario = "piedra"
elif opcion == 2:  #si la opcion que escoge el usuario es 2 entonces se le asigna papel
    elijeUsuario = "papel"
elif opcion == 3:  #si la opcion que escoge el usuario es 3 entonces se le asigna tijera
    elijeUsuario = "tijera"
print("Tu elijes: ", elijeUsuario) #aqui leemos la opcion que escogio el usuario y la imprimimos 

if aleatorio == 0:   #si la opcion que escoge la maquina es 0 entonces se le asigna piedra
    elijePc = "piedra"
elif aleatorio == 1:   #si la opcion que escoge la maquina es 1 entonces se le asigna papel
    elijePc = "papel"
elif aleatorio == 2:   #si la opcion que escoge la maquina es 2 entonces se le asigna tijera
    elijePc = "tijera"
print("PC elijio: ", elijePc)  #se imprime la opcion que la maquina elijio aleatoriamente
print("...")
 #aqui viene nustras condicionales
if elijePc == "piedra" and elijeUsuario == "papel": #si la maquina elige piedra y el usuario elije papel, gana el usuario 
    print("Ganaste, papel envulve piedra")  #imprime ganaste , y el motivo por que gano
elif elijePc == "papel" and elijeUsuario == "tijera": #si la maquina elige papel y el usuario elije tijera, gana el usuario 
    print("Ganaste, Tijera corta papel")   #imprime ganaste , y el motivo por que gano
elif elijePc == "tijera" and elijeUsuario == "piedra": #si la maquina elige tijera y el usuario elije piedra, gana el usuario 
    print("Ganaste, Piedra pisa tijera")   #imprime ganaste , y el motivo por que gano

#ahora  vamos con las condicionales si el usuario pierde

if elijePc == "papel" and elijeUsuario == "piedra":  #si la maquina elige papel y el usuario elije piedra, gana la maquina
    print("perdiste, papel envulve piedra")   #imprime perdiste , y el motivo por que perdio
elif elijePc == "tijera" and elijeUsuario == "papel":  #si la maquina elige tijera y el usuario elije papel, gana la maquina 
    print("perdiste, Tijera corta papel")     #imprime perdiste , y el motivo por que perdio
elif elijePc == "piedra" and elijeUsuario == "tijera": #si la maquina elige piedra y el usuario elije tijera, gana la maquina 
    print("perdiste, Piedra pisa tijera")    #imprime perdiste , y el motivo por que perdio
elif elijePc == elijeUsuario:  #si la maquina elige la misma opcion que el usuario ingresa entonces se produce un empate 
    print("empate")   #imprimimos el mensaje de empate
