import re

def analisar_texto(texto):
    # Número de palavras
    palavras = texto.split()
    num_palavras = len(palavras)

    # Número de caracteres
    num_caracteres = len(texto)

    # Número de frases
    frases = re.split(r'[.!?]', texto)
    num_frases = len([frase for frase in frases if frase.strip()])

    return {
        'num_palavras': num_palavras,
        'num_caracteres': num_caracteres,
        'num_frases': num_frases
    }

# Exemplo de uso
texto = "Este é um exemplo de texto. Ele tem várias frases e palavras."
estatísticas = analisar_texto(texto)

print("Estatísticas do texto:")
print(f"  Número de palavras: {estatísticas['num_palavras']}")
print(f"  Número de caracteres: {estatísticas['num_caracteres']}")
print(f"  Número de frases: {estatísticas['num_frases']}")