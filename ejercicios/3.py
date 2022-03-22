"""

Imprimir los cuadrados de los primeros 60 numeros

"""

# Ejercicio 3
# FOR
for i in range(0, 61): #Tambien puedo usar "range(61)""
    y=i**2
    print(y)
    i+=1

# WHILE
i=0

while i <= 60:
    y=i**2
    print(f"{i} al cuadrado es igual a:{y}")
    i+=1
