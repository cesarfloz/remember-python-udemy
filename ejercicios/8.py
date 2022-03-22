"""
Pedir un numero, y pedir ademas cuando porcentaje
quiere que le muestre de dicho numero

"""
first_num = int(input("Ingrese un numero entero: "))
second_num = int(input("Ingrese en numero entero el porcentaje que le quierese sacar al primer numero: "))

porcentaje = second_num/100

resultado = first_num*porcentaje

print (f"el {second_num}% de {first_num} es : {resultado}")

#(puede ser mas limpio)