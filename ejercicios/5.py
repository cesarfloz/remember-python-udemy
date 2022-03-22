"""

Un programa que muestre todos los numeros entre
dos numeros que me de el usuario

"""

# Ejercicio 5

first_num = int(input("Ingrese un numero entero: "))
second_num = int(input("Ingrese otro numero entero, pero mayor al anterior: "))

while first_num <= second_num:
    print(first_num)
    first_num+=1
