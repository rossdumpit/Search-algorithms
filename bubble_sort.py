def bubble_sort(array):
    n = len(array)
    swaps = 0
    for i in range(n):
        already_sorted = True

        for j in range(n - i -1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swaps += 1
                already_sorted = False
        if already_sorted:
            break
    return array, swaps