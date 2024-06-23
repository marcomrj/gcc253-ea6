# Trabalho de Complexidade de Projetos Algoritmicos


## Problema da Partição (PP)
   Dado um conjunto de números inteiros, o objetivo é dividir os números em dois grupos disjuntos de tal forma que a soma dos números em cada grupo seja a mesma. Portanto, a entrada é um arranjo e a saída é composta de dois arranjos, que representam as duas partições.
  
  ---

## O que deve ser feito?
###  Implementação de algoritmos para o problema 

#### Quais algoritmos?

Dois algoritmos para o problema sorteado, sendo o primeiro um algoritmo exato de força bruta ou backtracking e o segundo um algoritmo aproximado ou uma heurística.
#### Qual linguagem de programação?
Implemente usando sua linguagem de preferência, desde que as bibliotecas padrão das linguagens sejam utilizadas e não seja necessário o download de uma grande quantidade de dependências para funcionar. Certifique-se de que o trabalho pode ser facilmente reproduzido. É responsabilidade do grupo garantir isso, entenda bem qual ambiente ele será testado e trabalhe de acordo (veja abaixo).

#### Como deve ser a entrada e a saída dos algoritmos? 
Seu trabalho deve usar a entrada e saída padrão, da mesma forma do Beecrowd (scanf, cout, cin, etc.). Dessa forma, os testes do programa serão arquivos de entrada redirecionados à entrada padrão em um formato definido pelo grupo; e a saída será produzida na saída padrão.

#### Para qual ambiente?
 Os testes serão executados em Linux/UNIX. Portanto, garanta que seu código compila e roda corretamente nesse sistema operacional. A melhor forma de garantir que seu trabalho rode em Linux é escrever e testar o código nele. Você pode também usar o subsistema do Windows para Linux (WSL)1 , que é uma forma rápida com menos instalações. Você também pode fazer o download de uma variante de Linux como o Ubuntu2 e instalá-lo em seu computador ou diretamente ou por meio de uma máquina virtual como o VirtualBox 3 . Há vários tutoriais sobre como instalar Linux disponíveis na Internet.
  
#### Como o trabalho será compilado e executado?
Usando um Makefile. Esse arquivo é obrigatório e usado para compilar/preparar ($ make), executar com alguma entrada default de teste ($ make run) ou executar com alguma entrada específica contida em um arquivo in.txt ($ make run input=in.txt). Uma referência introdutória sobre como usar makefiles para compilação pode ser encontrada no rodapé4 .

#### Como deve ser o código?
Seu código deve ser bem escrito: 
(1) dê nomes a variáveis, funções e estruturas que façam sentido semântico;
(2) divida a implementação em módulos que tenham um significado bem definido;
(3) acrescente comentários sempre que julgar apropriado;
(4) não é necessário parafrasear o código, mas é interessante acrescentar descrições de alto nível que ajudem outras pessoas a entender como sua implementação funciona;
(5) evite utilizar variáveis globais;
(6) mantenha as funções concisas: seres humanos não são muito bons em manter uma grande quantidade de informação na memória ao mesmo tempo. Funções muito grandes, portanto, são mais difíceis de entender;
(7) lembre-se de indentar o código: escolha uma forma de indentar (tabulações ou espaços) e mantenha-se fiel a ela, misturar duas formas de indentação pode fazer com que o código fique ilegível quando você abri-lo em um editor de texto diferente do que foi utilizado originalmente;
(8) evite linhas de código muito longas. Uma convenção comum adotada em vários projetos é não passar de 80 caracteres de largura.

---

### Apresentação presencial do trabalho para a turma

O trabalho, juntamente com os algoritmos implementados, devem ser apresentados à turma em dia de aula previamente combinados. A apresentação deve ter uma duração estrita de, no máximo, 20 minutos (incluindo preparação de slides). Cada estudante deve ser responsável pela apresentação de uma parte do trabalho, sendo elas:
1. **Definição e explicação do problema, com exemplos:** Explicação do objetivo do problema usando figuras e exemplos.
2. **Algoritmo exato para o problema, de força bruta ou backtracking:** Pseudocódigo de um algoritmo exato para o problema, incluindo a descrição de seu funcionamento.
3. **Algoritmo aproximado ou heurística para o problema:** Pseudocódigo de um algoritmo aproximado ou heurística para o problema, incluindo a intuição por trás da estratégia não exata e exemplos, se necessário.
4. **Demonstração da execução de cada algoritmo:** Mostre a execução dos dois algoritmos para um único caso de teste pequeno, passível de inspeção visual. Aqui deve ser explicada a entrada e a saída produzida, juntamente com o significado dos formatos utilizados.
5. **Análise experimental dos algoritmos:** Vocês devem gerar pelo menos 10 instâncias de entrada para o problema, de tamanho crescente. O ideal é gerar a entrada aleatoriamente, mas se vocês encontrarem algum conjunto de entrada próprias para o problema, podem ser utilizadas desde que devidamente referenciadas. Em seguida, vocês devem executar (no mesmo ambiente) os algoritmos para as entradas escolhidas, sempre registrando (1) tempo de execução e (2) qualidade da solução. Vocês devem mostrar na apresentação os gráficos e/ou tabelas com os resultados obtidos em média, isto é, depois de várias execuções de uma mesma entrada. Na apresentação, além de mostrar os resultados, discuta o que eles significam no contexto da disciplina (Assintoticamente acurados? Resultados inesperados?). Se você tiver dúvida de como realizar um estudo experimental, pergunte que eu dou algumas sugestões.

**Atenção:** No caso de um grupo com menos de 5 integrantes, a divisão das partes faltantes ficam a critério do grupo, desde que respeitada a condição de que cada integrante deve apresentar pelo menos uma parte.

---

### Como deve ser entregue
A apresentação é exigida a todos os integrantes do grupo para contabilização da nota. Além disso, o trabalho deve ser entregue no Campus Virtual da disciplina na forma de um único arquivo zipado (formato .zip) contendo implementação, makefile, arquivos de teste e apresentação, organizados em um diretório chamado “problemas-classicos”:
```
problemas-classicos/ 
|- apresentacao.pdf 					# slides utilizados na apresentação 
|- src/ 								# arquivos fonte 
|- testes/ 								# arquivos de teste gerados/usados 
|- makefile 							# define como usar o software 
|- integrantes.txt 						# Nome e matrícula de cada
```
Você deve compactar esse diretório e seu conteúdo em um arquivo único chamado problemasclassicos-.zip. Arquivos em outros formatos (RAR, por exemplo) que não .zip não serão aceitos. Por exemplo, para o grupo do problema do caixeiro viajante (com sigla PCV, veja acima): problemas-classicos-PCV.zip.

---

### Avalição
Este trabalho será avaliado de acordo com os seguintes critérios:
- (grupo) Seguiu a especificação do trabalho, incluindo as entregas, formatos dos arquivos, nome dos arquivos, linguagem de programação, entrada e saída, makefile, etc. 
- (grupo) Qualidade da apresentação: participação dos integrantes, domínio do assunto e das soluções apresentados, clareza nas explicações, etc. 
- (grupo) Qualidade da implementação: código indentado, bem comentado, variáveis legíveis, código modularizado, correto, alocação dinâmica correta, etc. 
- (individual) Domínio do tema e qualidade das explicações. 
- (individual) Participou da apresentação (requisito forte).

---

### Observações gerais
- Leia esta especificação com cuidado; 
- Essa especificação não é isenta de erros e ambiguidades. Portanto, se tiverem problemas para entender o que está escrito aqui: pergunte! 
- Comece o trabalho o quanto antes; 
- Apenas um arquivo deve ser entregue, compactado e no formato .zip; 
- Seu trabalho deve ser compatível com ambiente Linux; 
- Infelizmmente, nosso tempo para apresentação será estrito – em 20 minutos outro grupo entra independente de onde a apresentação estiver. Portanto, treine a apresentação e verifique o tempo juntamente com o grupo, para não haver prejuízo. Dica: utilize como base a marca de um slide de conteúdo para cada minuto de apresentação, se você possui muito mais slides do que isso ou se não tiverem treinado a apresentação, as chances de que o tempo se esgote são altas.