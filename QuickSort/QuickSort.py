import random
import time

def partition(array, low, high):

  pivot = array[high]

  i = low - 1

  for j in range(low, high):
    if array[j] <= pivot:

      i = i + 1

      (array[i], array[j]) = (array[j], array[i])

  (array[i + 1], array[high]) = (array[high], array[i + 1])

  return i + 1

def quickSort(array, low, high):
  if low < high:

    pi = partition(array, low, high)

    quickSort(array, low, pi - 1)

    quickSort(array, pi + 1, high)

lista = random.sample(range(0,10000), 10000)

tempo_inicial = time.time()

quickSort(lista,0,len(lista)-1)

tempo_final = time.time()

tempo_decorrido = tempo_final - tempo_inicial

print(tempo_decorrido)