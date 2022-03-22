"""

Pedir al usuario que ingrese la nota de 10 alumnos,
y decirle cuantos aprobaron y cuales perdieron

"""
contador = 1
alumnos_aprobados = 0
alumnos_reprobados = 0

cantidad_alumnos = int(input("Ingrese la cantidad de alumnos a los que le registrara la nota: "))

while contador <= cantidad_alumnos:

    nota=float(input(f"Ingresa la nota del alumno {contador}: "))
    contador+=1

    if nota >= 3:
        alumnos_aprobados+=1
    else:
        alumnos_reprobados+=1  

    


  
       
print(f"\nLa cantidad de alumnos aprobados es de: {str(alumnos_aprobados)}")
print(f"La cantidad de alumnos reprobados es de: {str(alumnos_reprobados)}")