"""

Pedirle al usuario 2 numeros y realizar las
4 operaciones basicas con ellos e imprimirlos

"""
# Ejercicio 4

first_num = float(input("Ingrese el primer numero: "))
second_num = float(input("Ingrese el ultimo numero: " ))

suma = first_num + second_num
resta = first_num - second_num
multiplicacion = first_num * second_num
division = first_num / second_num

print(f"El resultado de la suma es: " + str(suma))
print(f"El resultado de la resta es: " + str(resta))
print(f"El resultado de la multiplicacion es: " + str(multiplicacion))
print(f"Division: " + str(division))
