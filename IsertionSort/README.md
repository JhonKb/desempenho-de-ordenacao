# Insertion Sort

## Definição

A classificação de inserção é um algoritmo de classificação que coloca um elemento não classificado em seu lugar adequado em cada iteração.

A classificação de inserção funciona da mesma forma que classificamos cartas em nossa mão em um jogo de cartas.

Supomos que o primeiro cartão já está classificado, então, selecionamos um cartão não classificado. Se o cartão não classificado for maior do que o cartão em mãos, ele é colocado à direita, caso contrário, à esquerda. Da mesma forma, outras cartas não ordenadas são retiradas e colocadas em seu lugar certo.

Uma abordagem semelhante é usada por classificação de inserção.

## Funcionalidade

Suponha que precisamos classificar a seguinte matriz.

1. Presume-se que o primeiro elemento na matriz seja classificado. Pegue o segundo elemento e armazene-o separadamente no .

    Compare com o primeiro elemento. Se o primeiro elemento for maior que , então é colocado na frente do primeiro elemento.

2. Agora, os dois primeiros elementos são classificados.

    Pegue o terceiro elemento e compare-o com os elementos à esquerda dele. Coloque-o logo atrás do elemento menor que ele. Se não houver nenhum elemento menor do que ele, coloque-o no início da matriz.

3. Da mesma forma, coloque cada elemento não classificado em sua posição correta.

## Exemplo

Disponivel em [Exemplo](InsertionSort.py)
