# Función que cuenta cuántas veces aparece una letra en una palabra
def contar_apariciones(palabra, letra):
    contador = palabra.count(letra)
    print(f"La letra '{letra}' aparece {contador} vez/veces en la palabra '{palabra}'.")

# Ejemplo de uso
contar_apariciones("programacion", "o")  # Resultado: 2