def contar_letra(palabra, letra):
    contador = 0
    for caracter in palabra:
        if caracter == letra:
            contador += 1
    return contador

# Ejemplo de uso:
resultado = contar_letra("noelia olea", "i")
print("La letra aparece", resultado, "veces.")