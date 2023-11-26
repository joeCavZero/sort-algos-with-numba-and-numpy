import numpy as np
from numba import njit

#============== BUBBLE_SORT ==============
@njit
def bubble_sort(array : np.ndarray ) -> None:
    size  :int  = array.size
    troca :bool = True
    
    while troca:
        troca = False
        for i in np.arange(size - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                troca = True
    pass

#============== INSERTION_SORT ==============
@njit
def insertion_sort(array  : np.ndarray ):
    size :int = array.size

    for i in np.arange( 1, size ):
        key = array[i]
        j = i-1
        while j >= 0 and key < array[j] :
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

    pass

#============== SELECTION_SORT ==============
@njit
def selection_sort(array : np.ndarray ):
    size :int = array.size

    for i in np.arange( size ):
        menor_pos :int = i
        for j in np.arange(i + 1, size):
            if array[j] < array[menor_pos]:
                menor_pos = j
        array[i], array[menor_pos] = array[menor_pos] , array[i]

    pass

#============== MERGE_SORT ==============
def merge_sort(array : np.ndarray):
    if array.size > 1:
        mid = array.size // 2
        left_half = array[:mid].copy()  # Usar copy() para criar uma cópia
        right_half = array[mid:].copy()  # Usar copy() para criar uma cópia

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < left_half.size and j < right_half.size:
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1

        while i < left_half.size:
            array[k] = left_half[i]
            i += 1
            k += 1

        while j < right_half.size :
            array[k] = right_half[j]
            j += 1
            k += 1
    pass

#============== QUICK_SORT ==============
# sem jit é mais rapido que uma versão compativel com o jit kkkkkkk
def quick_sort(array: np.ndarray) -> None:
    if array.size <= 1:
        return

    pivot = array[array.size // 2]
    left = array[array < pivot]
    middle = array[array == pivot]
    right = array[array > pivot]

    quick_sort(left)
    quick_sort(right)

    array[:] = np.concatenate((left, middle, right))

#============== HEAP_SORT ==============
def heap_sort(array: np.ndarray) -> None:
    @njit
    def heapify(arr, n, i):
        largest = i
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        if left_child < n and arr[left_child] > arr[largest]:
            largest = left_child

        if right_child < n and arr[right_child] > arr[largest]:
            largest = right_child

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    @njit
    def build_heap(arr):
        n = arr.size
        start_index = (n // 2) - 1

        for i in range(start_index, -1, -1):
            heapify(arr, n, i)

    @njit
    def sort_heap(arr):
        n = arr.size

        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            heapify(arr, i, 0)

    build_heap(array)
    sort_heap(array)

    pass



caminho_arquivo = "/content/ED/nomes.txt"
dados = np.loadtxt( caminho_arquivo, dtype=str , usecols=[0] )
dados = dados.ravel(  )

print(dados.size)
quick_sort(dados)
print(dados)

