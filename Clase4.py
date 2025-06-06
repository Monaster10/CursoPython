# Paso 1: Crear una lista que se llame mascotas y tenga los siguientes tres elementos: perro, gato, conejo.
mascotas = ["perro", "gato", "conejo"]

# Paso 2: Decir qué devuelve mascotas[2]
# Esto imprime el tercer elemento de la lista, ya que los índices comienzan en 0
print("Paso 2: El elemento en mascotas[2] es:", mascotas[2])  # Devuelve: conejo

# Paso 3: Escribir una función que imprima por pantalla los elementos que tiene la lista de mascotas
def imprimir_mascotas():
    print("Paso 3: Lista de mascotas:")
    for mascota in mascotas:
        print(mascota)

# Llamamos a la función para mostrar los elementos actuales
imprimir_mascotas()

# Paso 4: Crear una variable que se llame animal y asignarle un nuevo animal
animal = "loro"
print("Paso 4: Nuevo animal asignado a la variable 'animal':", animal)

# Paso 5: ¿De qué tipo es la variable animal?
print("Paso 5: El tipo de la variable 'animal' es:", type(animal))  # str

# Paso 6: Escribir una función que reciba un animal y lo agregue a la lista de mascotas
def agregar_mascota(nuevo_animal):
    mascotas.append(nuevo_animal)
    print(f"Paso 6: '{nuevo_animal}' fue agregado a la lista de mascotas.")

# Usamos la función para agregar el animal
agregar_mascota(animal)

# Volvemos a imprimir la lista actualizada
imprimir_mascotas()

# Paso 7: A partir de la siguiente lista decir qué mostrará el ciclo for
lista = [2, 3, 4, 8, 6, 7]
print("Paso 7: Valores que se imprimen en el ciclo for:")
for i in range(1, 3):
    print(lista[i])  # Imprime: 3 y 4