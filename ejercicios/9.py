"""
Pedir un numero indefinido al usuario, hasta 
que introduzca el 111

"""
i=2

while  i < 10:
    num = int(input("\nAdivina el numero entero, si no aciertas tendras que poner otro: "))

    if num == 18:
        break
    else:
        print("\nPISTA: Esta en un rango de 0 a 20 ")
        
 


print("\nHaz acertado felicidades")
