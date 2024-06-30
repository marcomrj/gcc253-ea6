# Para uma abordagem aproximada ou heurística para resolver o problema de partição, uma técnica comum é a heurística do "greedy" (guloso).
# Essa abordagem não garante uma solução perfeita, mas pode produzir uma boa partição em um tempo razoável, especialmente quando o conjunto de números é grande.

# A ideia básica da heurística gulosa é ordenar os números em ordem decrescente e, em seguida, iterar sobre eles, adicionando cada número ao subconjunto que atualmente tem a menor soma.
# Aqui está como você pode implementar isso em Python:

def particao_gulosa(nums):
    # Ordena os números em ordem decrescente
    nums.sort(reverse=True)

    # Inicializa dois subconjuntos
    conjunto1 = []
    conjunto2 = []

    # Soma inicial dos subconjuntos
    soma1, soma2 = 0, 0

    # Distribui os números entre os dois subconjuntos
    for num in nums:
        if soma1 <= soma2:
            conjunto1.append(num)
            soma1 += num
        else:
            conjunto2.append(num)
            soma2 += num

    return conjunto1, conjunto2


with open("../testes/partition_input_test.txt", "r") as arq:
    for linha in arq:
        nums = list(map(int, linha.split()))
        conjunto1, conjunto2 = particao_gulosa(nums)
        print("Conjunto original:", nums)
        if sum(conjunto1) == sum(conjunto2):
            print("Partição válida:")
        else:
            print("Partição inválida:")
        print("Conjunto 1:", conjunto1, "Soma:", sum(conjunto1))
        print("Conjunto 2:", conjunto2, "Soma:", sum(conjunto2))
        print("--------------------")

# No código acima:
# - A lista de números é primeiramente ordenada em ordem decrescente.
# - Em seguida, para cada número, decidimos em qual subconjunto inseri-lo com base na soma atual dos subconjuntos.
# - O objetivo é equilibrar as somas dos dois subconjuntos.

# Esta heurística é rápida e simples, mas a partição que ela gera pode não ser perfeitamente equilibrada.
# Ela tende a funcionar bem quando os números têm magnitudes semelhantes ou quando a diferença entre os maiores números não é extremamente alta.
# Para conjuntos de dados onde a distribuição dos valores é muito variada, esta abordagem pode não resultar em partições com somas próximas.
