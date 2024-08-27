import timeit
import matplotlib.pyplot as plt

def backtrack(index, soma_atual, conjunto, used_indices, nums, target, n):
    if soma_atual == target:
        return True, conjunto, used_indices
    if index >= n or soma_atual > target:
        return False, [], []
    encontrado, resultado, indices = backtrack(index + 1,
                                               soma_atual + nums[index],
                                               conjunto + [nums[index]],
                                               used_indices + [index],
                                               nums, target, n)
    if encontrado:
        return True, resultado, indices
    return backtrack(index + 1, soma_atual, conjunto, used_indices, nums, target, n)

def pode_particionar(nums):
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False, [], []
    target = total_sum // 2
    n = len(nums)
    return backtrack(0, 0, [], [], nums, target, n)

def ler_dados_e_medir_tempos():
    tempos = []
    conjuntos = []
    with open("../testes/entrada.txt", "r") as file:
        for line in file:
            nums = list(map(int, line.split()))
            # Usar uma função lambda para capturar 'nums' diretamente
            tempo = timeit.timeit(lambda: pode_particionar(nums), number=10) / 10
            tempos.append(tempo)
            conjuntos.append(len(nums))
            
            sucesso, conjunto1, used_indices = pode_particionar(nums)
            conjunto2 = [nums[i] for i in range(len(nums)) if i not in used_indices] if sucesso else []
            print("Conjunto original:", nums)
            if sucesso:
                print("Partição válida:")
            else:
                print("Partição inválida:")
            print("Conjunto 1:", conjunto1, "Soma:", sum(conjunto1))
            print("Conjunto 2:", conjunto2, "Soma:", sum(conjunto2))
            print("Tempo de execução: {:.5f} segundos".format(tempo))
            print("--------------------")
    return tempos, conjuntos

tempos, conjuntos = ler_dados_e_medir_tempos()

plt.figure(figsize=(10, 5))
plt.bar(range(len(tempos)), tempos, tick_label=conjuntos)
plt.xlabel('Tamanho do Vetor')
plt.ylabel('Tempo de Execução (s)')
plt.title('Tempo de Execução por Tamanho do Vetor para Backtracking')
plt.savefig('grafico_ultima_execucao/backtracking.png')
plt.show()
