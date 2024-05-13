from random import randint
from timeit import repeat

def time_algorithm(algorithm, array):
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm} ({array})"

    times = repeat(setup = setup_code, stmt =stmt, repeat =3, number = 10)

    sorted_array, num_swaps = eval(stmt)

    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}. Number of swaps: {num_swaps}")


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

ARRAY_LENGTH = 1000

if __name__ == "__main__":
    array = [randint(0,1000) for i in range(ARRAY_LENGTH)]
    time_algorithm(algorithm = "bubble_sort", array = array)