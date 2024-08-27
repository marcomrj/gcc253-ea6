import timeit
import matplotlib.pyplot as plt

# Importando os módulos guloso e backtracking
from guloso import particao_gulosa
from backtracking import pode_particionar

def executar_testes_e_salvar_resultados():
    with open("../testes/entrada.txt", "r") as file:
        resultados = []
        comprimentos_vetores = []
        for line in file:
            nums = list(map(int, line.split()))
            comprimentos_vetores.append(len(nums))
            tempos_guloso = []
            tempos_backtracking = []
            
            for _ in range(5):
                tempo_guloso = timeit.timeit(lambda: particao_gulosa(nums), number=1)
                tempo_backtracking = timeit.timeit(lambda: pode_particionar(nums), number=1)
                tempos_guloso.append(tempo_guloso)
                tempos_backtracking.append(tempo_backtracking)
            
            media_guloso = sum(tempos_guloso) / len(tempos_guloso)
            media_backtracking = sum(tempos_backtracking) / len(tempos_backtracking)
            
            conjunto1_guloso, conjunto2_guloso = particao_gulosa(nums)
            validade_guloso = "Sim" if sum(conjunto1_guloso) == sum(conjunto2_guloso) else "Não"
            _, conjunto1_backtracking, conjunto2_backtracking = pode_particionar(nums)
            validade_backtracking = "Sim" if sum(conjunto1_backtracking) == sum(conjunto2_backtracking) else "Não"

            resultados.append((media_guloso, media_backtracking, tempos_guloso, tempos_backtracking, validade_guloso, validade_backtracking, conjunto1_guloso, conjunto2_guloso, conjunto1_backtracking, conjunto2_backtracking))

        with open("resultados_tempos.txt", "w") as out_file:
            for idx, (media_g, media_b, tempos_g, tempos_b, val_g, val_b, conj1_g, conj2_g, conj1_b, conj2_b) in enumerate(resultados):
                out_file.write(f"Vetor {idx+1} - Tamanho {comprimentos_vetores[idx]}:\n")
                out_file.write(f"Tempos Guloso: {tempos_g} - Média: {media_g} - Válido: {val_g}\n")
                out_file.write(f"Partições: {conj1_g} e {conj2_g}\n") if val_g == "Sim" else ""
                out_file.write(f"Tempos Backtracking: {tempos_b} - Média: {media_b} - Válido: {val_b}\n")
                out_file.write(f"Partições: {conj1_b} e {conj2_b}\n") if val_b == "Sim" else ""
                out_file.write("----------\n")

        indices = range(len(comprimentos_vetores))
        medias_gulosos = [res[0] for res in resultados]
        medias_backtracking = [res[1] for res in resultados]

        plt.figure(figsize=(15, 7))
        plt.bar([x - 0.2 for x in indices], medias_gulosos, width=0.4, label='Guloso', color='blue')
        plt.bar([x + 0.2 for x in indices], medias_backtracking, width=0.4, label='Backtracking', color='red')
        plt.xticks(indices, comprimentos_vetores)
        plt.xlabel('Tamanho do Vetor')
        plt.ylabel('Tempo Médio de Execução (s)')
        plt.title('Comparação de Tempo Médio: Guloso vs. Backtracking')
        plt.legend()
        plt.savefig('comparacao_tempos.png')
        plt.show()

executar_testes_e_salvar_resultados()
