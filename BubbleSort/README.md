# Bubble Sort

## Classificação

Bubble sort é um algoritmo de classificação que compara dois elementos adjacentes e os troca até que estejam na ordem pretendida.

Assim como o movimento das bolhas de ar na água que sobem até a superfície, cada elemento da matriz se move até o final em cada iteração. Por isso, é chamado de bubble sort.

## Funcionalidade

Suponha que estejamos tentando classificar os elementos em ordem crescente.

1. Primeira Iteração (Compare e Swap)

    1. A partir do primeiro índice, compare o primeiro e o segundo elementos.

    2. Se o primeiro elemento for maior que o segundo, eles serão trocados.

    3. Agora, compare o segundo e o terceiro elementos. Troque-os se não estiverem em ordem.

    4. O processo acima continua até o último elemento.

2. Iteração restante

O mesmo processo continua para as iterações restantes.

Após cada iteração, o maior elemento entre os elementos não classificados é colocado no final.

Em cada iteração, a comparação ocorre até o último elemento não classificado.

A matriz é classificada quando todos os elementos não classificados são colocados em suas posições corretas.

## Exemplo

Disponivel em [Exemplo](BuddleSort.py)