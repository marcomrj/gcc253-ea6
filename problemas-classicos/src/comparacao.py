import timeit
import matplotlib.pyplot as plt
import pandas as pd

# Importando os módulos guloso e backtracking
from guloso import particao_gulosa
from backtracking import pode_particionar

def executar_testes_e_salvar_resultados():
    with open("../testes/entrada.txt", "r") as file:
        resultados = []
        comprimentos_vetores = []
        identificadores_vetores = []
        
        for idx, line in enumerate(file, start=1):
            nums = list(map(int, line.split()))
            comprimentos_vetores.append(len(nums))
            identificadores_vetores.append(f'Vetor {idx}')
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

            resultados.append({
                'media_guloso': media_guloso,
                'media_backtracking': media_backtracking,
                'qualidade_guloso': abs(sum(conjunto1_guloso) - sum(conjunto2_guloso)),
                'qualidade_backtracking': abs(sum(conjunto1_backtracking) - sum(conjunto2_backtracking)),
                'validade_guloso': validade_guloso,
                'validade_backtracking': validade_backtracking
            })

        # Convertendo resultados para DataFrame
        df_resultados = pd.DataFrame(resultados)
        df_resultados['comprimento_vetor'] = comprimentos_vetores
        df_resultados.insert(0, 'identificador_vetor', identificadores_vetores)

        # Salvar o DataFrame em CSV
        df_resultados.to_csv('resultados/resultados_comparacao.csv', index=False)

        # Gráficos
        fig, axs = plt.subplots(2, 1, figsize=(10, 10))

        # Gráfico de tempo de execução
        axs[0].plot(df_resultados['comprimento_vetor'], df_resultados['media_backtracking'],
                    label='Backtracking (Exato)', marker='o')
        axs[0].plot(df_resultados['comprimento_vetor'], df_resultados['media_guloso'], label='Heurística Gulosa',
                    marker='o')
        axs[0].set_title('Tempo de Execução Médio')
        axs[0].set_xlabel('Tamanho do Conjunto')
        axs[0].set_ylabel('Tempo de Execução (s)')
        axs[0].set_yscale('log')  # Escala logarítmica para visualizar melhor
        axs[0].legend()
        axs[0].grid(True)

        # Gráfico de qualidade da solução
        axs[1].plot(df_resultados['comprimento_vetor'], df_resultados['qualidade_backtracking'],
                    label='Backtracking (Exato)', marker='o')
        axs[1].plot(df_resultados['comprimento_vetor'], df_resultados['qualidade_guloso'], label='Heurística Gulosa',
                    marker='o')
        axs[1].set_title('Qualidade da Solução (Diferença de Somas)')
        axs[1].set_xlabel('Tamanho do Conjunto')
        axs[1].set_ylabel('Diferença de Somas')
        axs[1].legend()
        axs[1].grid(True)

        plt.tight_layout()

        # Salvar gráficos como imagem
        plt.savefig('resultados/comparacao_tempos_qualidade.png')

executar_testes_e_salvar_resultados()
