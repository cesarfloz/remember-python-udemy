'''
# FOR

for variable in elemento_iterable (lista, rango...)
    Bloque de instrucciones
'''
# Example 

resultado = 0
contador = 0

for contador in range(0, 10):
    print (contador)
    resultado += contador
    #resultado = resultado + contador

print(f"voy en el : {resultado}")

''' 
HOMEWORK
Hacer las tablas de  multiplicar con bucle for 
'''

'''
# WHILE

while condicion:
    bloque de instruciones
    actualizacion del contador
'''

# Example 

contador = 1

while contador >= 100:
    print(f"Voy en el numero : {contador}")
    contador +=1
