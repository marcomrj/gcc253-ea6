# Para uma abordagem aproximada ou heurística para resolver o problema de partição, uma técnica comum é a heurística do "greedy" (guloso).
# Essa abordagem não garante uma solução perfeita, mas pode produzir uma boa partição em um tempo razoável, especialmente quando o conjunto de números é grande.

# A ideia básica da heurística gulosa é ordenar os números em ordem decrescente e, em seguida, iterar sobre eles, adicionando cada número ao subconjunto que atualmente tem a menor soma.
# Aqui está como você pode implementar isso em Python:

def particao_gulosa(nums):
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return [], []  # Retornar listas vazias se a soma total é ímpar
    
    nums.sort(reverse=True)
    conjunto1, conjunto2 = [], []
    soma1, soma2 = 0, 0
    
    for num in nums:
        if soma1 <= soma2:
            conjunto1.append(num)
            soma1 += num
        else:
            conjunto2.append(num)
            soma2 += num
    return conjunto1, conjunto2



# No código acima:
# - A lista de números é primeiramente ordenada em ordem decrescente.
# - Em seguida, para cada número, decidimos em qual subconjunto inseri-lo com base na soma atual dos subconjuntos.
# - O objetivo é equilibrar as somas dos dois subconjuntos.

# Esta heurística é rápida e simples, mas a partição que ela gera pode não ser perfeitamente equilibrada.
# Ela tende a funcionar bem quando os números têm magnitudes semelhantes ou quando a diferença entre os maiores números não é extremamente alta.
# Para conjuntos de dados onde a distribuição dos valores é muito variada, esta abordagem pode não resultar em partições com somas próximas.
