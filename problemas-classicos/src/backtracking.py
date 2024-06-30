def pode_particionar(nums):
    total_sum = sum(nums)
    # Se a soma total não for par, não é possível dividir em dois subconjuntos com a mesma soma
    if total_sum % 2 != 0:
        return False, [], []
    target = total_sum // 2
    n = len(nums)

    # Função auxiliar para realizar o backtracking
    def backtrack(index, soma_atual, conjunto, used_indices):
        # Se a soma atual for igual ao alvo, encontramos uma partição
        if soma_atual == target:
            return True, conjunto, used_indices
        # Se exceder o índice ou a soma atual exceder o alvo, não há solução por esse caminho
        if index >= n or soma_atual > target:
            return False, [], []
        # Tenta incluir o número atual no subconjunto
        found, result, indices = backtrack(index + 1,
                                           soma_atual + nums[index],
                                           conjunto + [nums[index]],
                                           used_indices + [index])
        if found:
            return True, result, indices
        # Tenta não incluir o número atual no subconjunto
        return backtrack(index + 1, soma_atual, conjunto, used_indices)

    # Iniciar o backtracking a partir do índice 0 e soma 0
    sucesso, conjunto1, used_indices = backtrack(0, 0, [], [])
    if sucesso:
        conjunto2 = [nums[i] for i in range(n) if i not in used_indices]
        return True, conjunto1, conjunto2
    else:
        return False, [], []


# Exemplo de uso
with open("../testes/partition_input_test.txt", "r") as file:
    print("Testando o algoritmo de backtracking para "
          "o problema de partição de conjunto...")
    for line in file:
        print("--------------------")
        print("Conjunto original:", line)
        nums = list(map(int, line.split()))
        sucesso, conjunto1, conjunto2 = pode_particionar(nums)
        if sucesso:
            print("Partição válida:")
            print("Conjunto 1:", conjunto1, "Soma:", sum(conjunto1))
            print("Conjunto 2:", conjunto2, "Soma:", sum(conjunto2))
        else:
            print("Partição inválida. Não é possível dividir "
                  "o conjunto em dois subconjuntos com a mesma soma."
                )
        
