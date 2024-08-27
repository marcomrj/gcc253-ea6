import random

def gerar_vetores_aleatorios(num_vetores, comp_maximo=20, num_maximo=50):
    vetores = []
    for _ in range(num_vetores):
        comprimento = random.randint(4, comp_maximo)
        vetor = [random.randint(0, num_maximo) for _ in range(comprimento)]
        vetores.append(vetor)
    return vetores

def salvar_vetores_em_arquivo(vetores, caminho_arquivo):
    vetores.sort(key=len)
    with open(caminho_arquivo, 'w') as arquivo:
        for vetor in vetores:
            linha = ' '.join(map(str, vetor))
            arquivo.write(linha + '\n')

num_vetores = 10
comp_maximo = 20
num_maximo = 50

vetores_aleatorios = gerar_vetores_aleatorios(num_vetores, comp_maximo, num_maximo)

caminho_arquivo = '../testes/entrada.txt'

salvar_vetores_em_arquivo(vetores_aleatorios, caminho_arquivo)

print("Vetores aleatórios foram gerados e ordenados pelo tamanho.")
