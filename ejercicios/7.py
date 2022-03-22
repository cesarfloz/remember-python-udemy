"""
Mostrar todos los numeros pares entre 2 digitos
dados por el usuario

"""
first_num = int(input("Ingrese un numero entero: "))
second_num = int(input("Ingrese otro numero entero, pero mayor al anterior: "))

for i in range(first_num, second_num+1):
    if i%2==0:
        print(f"{i} es un numero par en el rango ingresado")
i+=1
      