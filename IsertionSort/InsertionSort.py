import random
import time

def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
       
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1

        array[j + 1] = key

lista = random.sample(range(0,10000), 10000)

tempo_inicial = time.time()

insertionSort(lista)

tempo_final = time.time()

tempo_decorrido = tempo_final - tempo_inicial

print(tempo_decorrido)