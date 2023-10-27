soma = 0.0

# insira os valores pelos valores
array = [0.009006595611572266, 0.015603017807006837]

for i in range(len(array)):

    soma += array[i-1]

media = soma/len(array)

print(media)
