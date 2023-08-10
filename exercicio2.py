def is_anagram(str1, str2):
    # Remover espaços e transformar em letras minúsculas
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Verificar se as strings têm o mesmo número de caracteres
    if len(str1) != len(str2):
        return False

    # Converter as strings em listas de caracteres
    list1 = list(str1)
    list2 = list(str2)

    # Verificar se as listas são iguais quando ordenadas
    return sorted(list1) == sorted(list2)

# Exemplos de uso
print(is_anagram("Amor", "Roma"))  # retornar True
print(is_anagram("Pedra", "Padre"))  #  retornar True
print(is_anagram("Perda", "Pedra"))  #  retornar True
print(is_anagram("Hello", "World"))  #  retornar False











