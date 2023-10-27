import random
import time

def bubbleSort(array):

  for i in range(len(array)):

    for j in range(0, len(array) - i - 1):

      if array[j] > array[j + 1]:

        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp

lista = random.sample(range(0,10000), 10000)

tempo_inicial = time.time()

bubbleSort(lista)

tempo_final = time.time()

tempo_decorrido = tempo_final - tempo_inicial

print(tempo_decorrido)