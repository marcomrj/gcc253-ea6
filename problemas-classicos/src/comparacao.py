import timeit
import matplotlib.pyplot as plt

# Importando os módulos guloso e backtracking
from guloso import particao_gulosa
from backtracking import pode_particionar

def executar_testes_e_salvar_resultados():
    with open("../testes/entrada.txt", "r") as file:
        resultados = []
        comprimentos_vetores = []  # Lista para armazenar o comprimento de cada vetor
        for line in file:
            nums = list(map(int, line.split()))
            comprimentos_vetores.append(len(nums))  # Armazenar o comprimento do vetor atual
            tempos_guloso = []
            tempos_backtracking = []
            
            # Executando cada algoritmo 5 vezes
            for _ in range(5):
                tempo_guloso = timeit.timeit(lambda: particao_gulosa(nums), number=1)
                tempo_backtracking = timeit.timeit(lambda: pode_particionar(nums), number=1)
                tempos_guloso.append(tempo_guloso)
                tempos_backtracking.append(tempo_backtracking)
            
            # Calculando os tempos médios
            media_guloso = sum(tempos_guloso) / len(tempos_guloso)
            media_backtracking = sum(tempos_backtracking) / len(tempos_backtracking)
            
            # Armazenando os resultados
            resultados.append((media_guloso, media_backtracking, tempos_guloso, tempos_backtracking))

        # Salvando os resultados em um arquivo de texto
        with open("resultados_tempos.txt", "w") as out_file:
            for media_g, media_b, tempos_g, tempos_b in resultados:
                out_file.write(f"Tempos Guloso: {tempos_g} - Média: {media_g}\n")
                out_file.write(f"Tempos Backtracking: {tempos_b} - Média: {media_b}\n")
                out_file.write("----------\n")

        # Gerando o gráfico
        indices = range(len(comprimentos_vetores))
        medias_gulosos = [res[0] for res in resultados]
        medias_backtracking = [res[1] for res in resultados]

        plt.figure(figsize=(15, 7))
        plt.bar([x - 0.2 for x in indices], medias_gulosos, width=0.4, label='Guloso', color='blue')
        plt.bar([x + 0.2 for x in indices], medias_backtracking, width=0.4, label='Backtracking', color='red')
        plt.xticks(indices, comprimentos_vetores)  # Adicionando tamanhos de vetor como rótulos do eixo x
        plt.xlabel('Tamanho do Vetor')
        plt.ylabel('Tempo Médio de Execução (s)')
        plt.title('Comparação de Tempo Médio: Guloso vs. Backtracking')
        plt.legend()
        plt.savefig('comparacao_tempos.png')
        plt.show()

# Chamada da função que executa os testes e gera os resultados
executar_testes_e_salvar_resultados()
