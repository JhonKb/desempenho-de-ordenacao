import random
import time

def selectionSort(array, size):
   
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            if array[i] < array[min_idx]:
                min_idx = i
         
        (array[step], array[min_idx]) = (array[min_idx], array[step])

lista = random.sample(range(0,10000), 10000)

tempo_inicial = time.time()

selectionSort(lista, len(lista))

tempo_final = time.time()

tempo_decorrido = tempo_final - tempo_inicial

print(tempo_decorrido)
    