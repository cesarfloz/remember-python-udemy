# definir una clase

from turtle import color
from typing_extensions import Self


class Carro:

    #Atributos
    color = "negro"
    marca = "Tesla"
    modelo = "Model 3"
    velocidad = 260 
    puertas = 3

    #Metodos
    def setColor(self, color):
        self.color=color 

    def getColor(self):
        return self.color

    def acelerar(self):
        self.velocidad +=1
        
    def frenar(self):
        self.velocidad -=1

    def getVelocidad(self):
        return self.velocidad

#Crear objeto / Instanciar clase
carro = Carro()
print (carro.color)

print ("Velocidad actual: ", carro.velocidad)

carro.acelerar()
print("Velocidad actiual= ", carro.velocidad)

carro.frenar()
print("Velocidad actual: ", carro.velocidad)
###########################################################################################
carro.color="amarillo"
print("El nuevo color es: ", carro.getColor())
############################################################################################

carro2=Carro()
carro.color="Verde"
print("El color de este nuevo carro es: ", carro.getColor())