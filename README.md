# Desempenho de Ordenação

Tarefa apresentada em sala de aula na disciplina de Estruturas de Dados


## 📊 Objetivo

A presente tarefa tem como objetivo coletar informações relacionados ao desempenho de diferentes estruturas de dados em sua veloricade de ordenção

##

## 📃 Descrição da Tarefa

- Gere um conjunto de pelo menos 10.000 números aleárotios.

- Implementem os seguintes algoritimos de ordenação **Bubble Sort**, **Selection Sort**, **Insertion Sort**, **Merge Sort** e **Quick Sort**.

- Meça o tempo que cada algoritmo leva para ordenar o conjunto de números gerados.

- Registre e compare os tempos de execução de cada algoritmo.

- Apresente os resultados em um gráfico de tabela para facilitar a comparação.

##

## 👨‍💻 Algoritmos

A tabela a seguir apresenta um breve resumo sobre a funcionalidade de cada tipo de algoritmo, bem como seus exemplos:

| Nome | Apresentação |
|-|-|
| Bubble Sort | [Resumo](BubbleSort/README.md) |
| Selection Sort | [Resumo](SelectionSort/README.md) |
| Insertion Sort | [Resumo](IsertionSort/README.md) |
| Merge Sort | [Resumo](MergeSort/README.md) |
| Quick Sort | [Resumo](QuickSort/README.md) |

##

## 📊 Análise

### Estudo de Caso

- Para a realização desta tarefa, foram feitas 2 seções com 5 execuções dos algoritmos em cada uma.

- Cada seção, foi nregistrada em tabelas com as médias de cada seção.

- Foram sorteados 10000 números em cada algoritmo aleatóriamente

- Para facilitar o entendimento e a precisão dos dados, foram sortedos 1000 números entre 0 e 10000, que organizados formam um sequência exata de 0 a 9999.

- Foi utilizado um algoritmo auxiliar para obter as médias presente em [CalculadoraMédia](CalculadoraMedia.py).

### Resultados: 

- Seção 1

| Algoritmo | Execução 1(s) | Execução 2(s) | Execução 3(s) | Execução 4(s) | Execução 5(s) | Média(s) |
|-|-|
| Buddle Sort | 4.976010322570801 | 4.9122841358184814 | 4.936694383621216 | 5.6624791622161865 | 4.946794748306274 | 5.086852550506592 |
| Selection Sort | 1.9577834606170654 | 1.9512298107147217 | 1.9575278759002686 | 1.9927895069122314 | 1.9448223114013672 | 1.9608305931091308 |
| Insertion Sort | 2.2441866397857666 | 2.2329180240631104 | 2.2641830444335938 | 2.2493889331817627 | 2.236565113067627 | 2.245448350906372 |
| Merge Sort | 0.016640901565551758 | 0.03101181983947754 | 0.0182340145111084 | 0.030367136001586914 | 0.017923355102539062 | 0.022835445404052735 |
| Quick Sort | 0.0167391300201416 | 0.005443572998046875 | 0.014688491821289062 | 0.004565000534057617 | 0.003596782684326172 | 0.009006595611572266 |

- Seção 2

| Algoritmo | Execução 1 | Execução 2 | Execução 3 | Execução 4 | Execução 5 | Média |
|-|-|
| Buddle Sort | 4.925031900405884 | 4.930409669876099 | 4.934424877166748 | 4.878313302993774 | 4.903400659561157 | 4.914316082000733 |
| Selection Sort | 1.948457956314087 | 2.1178834438323975 | 1.9580798149108887 | 1.9432828426361084 | 1.9650206565856934 | 1.986544942855835 |
| Insertion Sort | 2.268470048904419 | 2.2388463020324707 | 2.2429919242858887 | 2.2980642318725586 | 2.249119758605957 | 2.259498453140259 |
| Merge Sort | 0.021200180053710938 | 0.015271902084350586 | 0.019159317016601562 | 0.031064510345458984 | 0.020815372467041016 | 0.021502256393432617 |
| Quick Sort | 0.016607999801635742 | 0.01335906982421875 | 0.018128156661987305 | 0.013111352920532227 | 0.016808509826660156 | 0.015603017807006837 |

- Gráfico:

![Gráfico de Desempenho](grafico.html)

## 🆗 Conclusão

Comm base nos dados apresentados foram obtidas as seguintes conclusões:

- Buddle Sort, apesar de ser o algoritmo mais simples, se mostrou o mais infeciente , tendo uma média 5x maior em comparação aos outros algoritmos analisados.

- Selection Sort e Insertion Sort, apesar de tambem serem algoritmos simples, apresentaram um melhor desempenho em comparação ao Buddle Sort, mostrando um certo meio termo entre velocidade e complexidade.

- Merge Sort e Quick Sort por outro lado, foram os que apresentaram um desempenho muito superior, sendo quase 10x maior que os outros algoritmos analisados. Em contra partida, ambos possuem um maior nivel de complexidade em sua estrutura.

Portanto, é importanto analisar tambem a aplicação para cada tipo. Em caso de um volume menor de dados, opções como Isertion, Selction ou Buddle Sorte se mostram mais viaveis devido a sua facilidade de construção. Enquanto, para um grande volume de dados, Merge e Quick Sorte são mais indicados.  

##

## 🔍 Referências

- DevMedia -  [Algoritmos de ordenação - análise e comparação ](https://www.devmedia.com.br/algoritmos-de-ordenacao-analise-e-comparacao/28261)

- Programiz - [Lern DSA & Algorithms](https://www.programiz.com/dsa)

##