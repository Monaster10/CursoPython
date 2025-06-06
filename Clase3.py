tupla = ("Génesis 1:1", "Éxodo 20:13", "Salmo 23:1")

lista = ("Génesis 1:1", "Éxodo 20:13", "Salmo 23:1")

def agregar_pasaje(pasaje):
    lista_pasajes = []
    lista_pasajes.append(pasaje)
    print("Pasajes en la lista:", lista_pasajes)

# Ejemplo de uso:
agregar_pasaje("Juan 3:16")

pasajes_biblia = [
    "Génesis 1:1 - En el principio creó Dios los cielos y la tierra.",
    "Éxodo 20:13 - No matarás.",
    "Salmo 23:1 - El Señor es mi pastor; nada me faltará.",
    "Juan 3:16 - Porque de tal manera amó Dios al mundo, que ha dado a su Hijo unigénito, para que todo aquel que en él cree no se pierda, mas tenga vida eterna.",
    "Filipenses 4:13 - Todo lo puedo en Cristo que me fortalece."
]

def mostrar_estructura(datos):
    for item in datos:
        print(item)

# Lista y tupla con pasajes bíblicos
tupla = ("Génesis 1:1 - En el principio creó Dios los cielos y la tierra.",
         "Éxodo 20:13 - No matarás.",
         "Salmo 23:1 - El Señor es mi pastor; nada me faltará.")

lista = ["Juan 3:16 - Porque de tal manera amó Dios al mundo, que ha dado a su Hijo unigénito, para que todo aquel que en él cree no se pierda, mas tenga vida eterna.",
         "Filipenses 4:13 - Todo lo puedo en Cristo que me fortalece.",
         "Mateo 28:19 - Por tanto, id y haced discípulos a todas las naciones..."]

# Llamamos a la función para mostrar la tupla
print("Mostrando los pasajes de la tupla:")
mostrar_estructura(tupla)

# Llamamos a la función para mostrar la lista
print("\nMostrando los pasajes de la lista:")
mostrar_estructura(lista)

def cuadrado(x):
    resultado = x * x
    return resultado

print(cuadrado(2))
# Aquí defines la función cuadrado(x) que calcula el cuadrado de x.

# Luego, llamas a la función dentro de print(), lo que significa que el resultado de la función se imprimirá directamente en la consola.

# Cuando ejecutas cuadrado(2), la salida es 4, y eso es lo que se imprimirá.

def cuadrado(x):
    resultado = x * x
    return resultado

cuadrado(2)

# Aquí defines la misma función cuadrado(x).

# Sin embargo, en este caso no usas print() para mostrar el resultado de la función.

# Llamas a la función cuadrado(2), pero no hay ninguna acción posterior para imprimir o almacenar el valor devuelto. Es decir, la función se ejecuta, pero su resultado se "pierde" porque no haces nada con él (no lo imprimes ni lo asignas a una variable).