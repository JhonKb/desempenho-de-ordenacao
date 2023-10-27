# Quick Sort

## Definição

Quicksort é um algoritmo de classificação baseado na abordagem de dividir e conquistar onde

1. Uma matriz é dividida em submatrizes selecionando um elemento dinâmico (elemento selecionado da matriz).

1. Ao dividir a matriz, o elemento de pivô deve ser posicionado de forma que elementos menores que o pivô sejam mantidos no lado esquerdo e elementos maiores que o pivô estejam no lado direito do pivô.
1. As submatrizes esquerda e direita também são divididas usando a mesma abordagem. Esse processo continua até que cada submatriz contenha um único elemento.
1. Neste ponto, os elementos já estão classificados. Finalmente, os elementos são combinados para formar uma matriz classificada.

## Funcionalidade

1. Selecione o elemento Pivot

Existem diferentes variações de quicksort onde o elemento de pivô é selecionado de diferentes posições. Aqui, selecionaremos o elemento mais à direita da matriz como o elemento pivot.

1. Reorganizar o array

Agora, os elementos da matriz são reorganizados para que os elementos menores que o pivô sejam colocados à esquerda e os elementos maiores que o pivô sejam colocados à direita.

Veja como reorganizamos a matriz:

- Um ponteiro é fixado no elemento pivot. O elemento de pivô é comparado com os elementos que começam a partir do primeiro índice.
- Se o elemento for maior que o elemento pivot, um segundo ponteiro será definido para esse elemento.
- Agora, o pivô é comparado com outros elementos. Se um elemento menor que o elemento pivot for alcançado, o elemento menor será trocado pelo elemento maior encontrado anteriormente.
- Novamente, o processo é repetido para definir o próximo elemento maior como o segundo ponteiro. E troque-o por outro elemento menor.
- O processo continua até que o segundo último elemento seja alcançado.
- Finalmente, o elemento de pivô é trocado pelo segundo ponteiro.

1. Os elementos de pivô são novamente escolhidos para as subpartes esquerda e direita separadamente. E o passo 2 é repetido.

As submatrizes são divididas até que cada submatriz seja formada por um único elemento. Neste ponto, a matriz já está classificada.

## Exemplo

Disponível em [Exemplo](QuickSort.py)





