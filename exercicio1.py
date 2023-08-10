def conta_palavras_unicas(frase):
    # Divide a frase em palavras, ignora caracteres especiais e converte para minúsculas
    palavras = [palavra.strip(".,!?").lower() for palavra in frase.split()]
    # Usa um conjunto para remover palavras duplicadas e retorna o tamanho 
    return len(set(palavras))

# Exemplo de uso
frase = "Esta é uma frase de exemplo. Esta frase contém palavras repetidas, mas queremos contar apenas as palavras únicas."
quantidade_palavras_unicas = conta_palavras_unicas(frase)
print("Quantidade de palavras únicas na frase:", quantidade_palavras_unicas)












