"""
# Definir lista

peliculas = ['Batman', 'Superman', 'Acuaman']
cantantes = list(('Yatra','Cepeda','Sin banderas'))
years=list(range(2001,2022))
variada=["ejemplo", 54, True, "ejemplo2.0"]

print(peliculas)
print(cantantes)
print(years)
print(variada)

# Indices
#cantantes[0]="Camilo Sesto" #Modifique el primer item de mi lista "cantantes"

print(peliculas[2])
print(cantantes[-1])
print(cantantes[0:2])
print(peliculas[0:]) #Imprime todos los elementos

#Añadir elementos

cantantes.append("Freddy Mercury")

print(cantantes)

#Recorre lista

print("\nRecorrer lista")

for cantantes in cantantes:
    print(f"{cantantes.index(cantantes)}. {cantantes}")



contador = 1
cantidad_adiciones=int(input("Ingresa la cantidad de peliculas que deseas ingresar: "))

while contador <= cantidad_adiciones:

    nueva_pelicula = input("Ingresa el nombre de la pelicula: ")
    peliculas.append(nueva_pelicula)

    contador+=1

print(peliculas)
"""
#Listas multidimensionales (varias dimensiones)

print("-----------------------------------------")
print("LISTA DE CONTACTOS")
print("-----------------------------------------")
contactos = [
    [
        'Cesar',
        'flozcesar@gmail.com'
    ],
    [
        'Juan Pablo',
        'juanpisf55@gmail.com'
    ],
    [
        'Gloria',
        'gcepa2326@gmail.com'
    ],
    [
        'Yter',
        'yter.florezg@gmail.com'
    ]
]

#print(contactos[0][1])
for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento)== 0:
            print(f"Nombre: {elemento}")

        else:
            print(f"Email: {elemento}")
    print("\n")
