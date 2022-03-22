
#Funciones con parametros

def personal_data (name, age, country):
    print(f"Your name is: {name}, age: {age}, and you are from {country}")

name=str(input("What's your name?: "))
age=int(input("What's your years old?: "))
country=str(input("Where are you from?: "))

personal_data(name, age, country)

# Funciones con parametros opcionales

def getEmpleado(name,id=None):#None es el valor por defecto de "id", por lo que no es un parametro onligatorio
    print("Empleado")
    print(f"name: {name}")
    print(f"id: {id}")

getEmpleado("Cesar")


def suma(num1, num2):
    resultado = num1+num2

    return resultado 

def resta(num1, num2):
    resultado = num1-num2

    return resultado

def multiplicacion(num1, num2):
    resultado = num1*num2

    return resultado

def division(num1, num2):
    resultado = num1/num2

    return resultado

print("-----------------------------------------------------------------------------------------------------------")
print("CALCULADORA de dos numeros")
print("-----------------------------------------------------------------------------------------------------------")
print("Ingresa la operacion que deseas realizar: ")
print("1. Suma ")
print("2. Resta ")
print("3. Multiplicacion ")
print("4. Division ")
operacion=int(input(""))

if operacion <1 or operacion >4:
    print("Esa opcion no existe")
    
else:
    primer_numero=float(input("Ingresa el primer numero: "))
    segundo_numero=float(input("Ingresa el segundo numero: "))

    if operacion == 1:
     print(suma(primer_numero, segundo_numero))

    elif operacion == 2:
      print(resta(primer_numero, segundo_numero))

    elif operacion == 3:
        print(multiplicacion(primer_numero, segundo_numero))

    elif operacion == 4:
     print(division(primer_numero, segundo_numero))

#PUEDE SER MAS LIMPIO


#Funciones dentro de funciones

def getNombre(nombre):

    imprimir=f"Tu nombre es {nombre}"

    return imprimir

def getApellido (apellido):

    imprimir=f"Tu apellido es {apellido}"

    return imprimir

def todo (nombre, apellido):

    imprimir=f"{getNombre(nombre)}, {getApellido(apellido)}"

    return imprimir



print(todo(nombre="Cewr", apellido="Florez"))

#Funcion Lambda (definida en una linea)

tellme_year = lambda year:f"El año es {year}"
print(tellme_year(2022))

