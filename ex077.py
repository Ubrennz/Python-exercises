palavras = (
    "python", "codigo", "desenvolvimento", "tupla", "aleatorio",
    "computador", "tecnologia", "programacao", "dados", "estrutura",
    "algoritmo", "funcao", "script", "variavel", "sistema"
)

vogais = ('a', 'e', 'i', 'o', 'u')

palavra_mostrada = False

for palavra in palavras:
    for vogal in vogais:
        if vogal in palavra and palavra_mostrada == False:
            print(f'Na palavra {palavra.upper()} temos', end=' ')
            palavra_mostrada = True
        if vogal in palavra:
            print(vogal, end=' ')

    print()
    palavra_mostrada = False
