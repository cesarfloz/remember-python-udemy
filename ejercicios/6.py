"""

Mostrar todas las tablas de multiplicar del 1 al 10

"""

# Ejercicio 6
tabla=1

print("TABLAS DE MULTIPLICAR\n")

for tabla in  range(1,11):

    print(f"Tabla del {tabla}\n")

    for contador in range(1,11):
        
        resultado = tabla*contador
        print(f"{tabla} x {contador} = {resultado}")

        if contador ==10:
            print("")

        contador+=1

tabla+=1        
#QUE HERMOSO, PURO CODIGO INNATO (puede ser mas limpio)