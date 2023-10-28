# Merge Sort

## Definição

Merge Sort é um dos algoritmos de classificação mais populares que se baseia no princípio do Algoritmo de Dividir e Conquistar.

Aqui, um problema é dividido em vários subproblemas. Cada sub-problema é resolvido individualmente. Finalmente, os sub-problemas são combinados para formar a solução final.

## Funcionalidade

1. Dividir para conquistar

    Usando a técnica Dividir para Conquistar, dividimos um problema em subproblemas. Quando a solução para cada subproblema está pronta, nós "combinamos" os resultados dos subproblemas para resolver o problema principal.

    A função MergeSort divide repetidamente a matriz em duas metades até chegarmos a um estágio em que tentamos executar MergeSort em uma submatriz de tamanho 1

    Depois disso, a função de mesclagem entra em ação e combina as matrizes classificadas em matrizes maiores até que toda a matriz seja mesclada.

1. Etapa de mesclagem:
    
    A etapa de mesclagem é a solução para o problema simples de mesclar duas listas classificadas (matrizes) para criar uma grande lista classificada (matriz).

    O algoritmo mantém três ponteiros, um para cada uma das duas matrizes e um para manter o índice atual da matriz classificada final.

## Exemplo

Disponível em [Exemplo](MergeSort.py)