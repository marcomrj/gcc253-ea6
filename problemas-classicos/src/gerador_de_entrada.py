import random

def gerar_vetores_aleatorios(num_vetores, num_maximo=50):
    vetores = []
    comprimento = 4 # Assim como solicitado durante a apresentação, a geração do comprimento não é mais aleatória
    for _ in range(num_vetores):
        comprimento += 2
        vetor = [random.randint(0, num_maximo) for _ in range(comprimento)]
        vetores.append(vetor)
    return vetores

def salvar_vetores_em_arquivo(vetores, caminho_arquivo):
    vetores.sort(key=len)
    with open(caminho_arquivo, 'w') as arquivo:
        for vetor in vetores:
            linha = ' '.join(map(str, vetor))
            arquivo.write(linha + '\n')

num_vetores = 10    # Valor que define a quantidade de vetores a serem analisados
num_maximo = 50     # Valor que define os números máximos que podem ser gerados aleatoriamente

vetores_aleatorios = gerar_vetores_aleatorios(num_vetores, num_maximo)

caminho_arquivo = '../testes/entrada.txt'

salvar_vetores_em_arquivo(vetores_aleatorios, caminho_arquivo)

print("Vetores aleatórios foram gerados e ordenados pelo tamanho.")
