from random import randint  #imports function for random integers
from timeit import repeat   #imports repeat function for timing algorithm

sorted_array = None #initialise sorted_array variable for global use

def insertion_sort(array):

    n = array
    swaps = 0   #initialises swap count
    comparison = 0  #initialises comparison count
    passes = 0
    for i in range(1, len(n)):  #loops through each element of the array starting on index 1

        value = n[i]    #assign value of i to value
        position = i   #assign index to position
        passes +=1
        while position > 0 and n[position -1] > value: #condition if position is not 0 and value of [position -1] is > value
            comparison += 1
            n[position] = n[position -1]
            position = position - 1    #decrement position
            swaps += 1 #increment swaps by 1
            n[position] = value #assign the value to index position
        comparison += 1
        if comparison == 0:
            comparison = passes -1

    return array, swaps, comparison

def descending_insertion_sort(array):   #descending insertion sort

    n = array
    swaps = 0
    comparison = 0

    for i in range(1, len(n)):

        value = n[i]
        position = i
        while position > 0 and n[position -1] < value:
            comparison += 1
            n[position] = n[position -1]
            position = position - 1
            swaps += 1
            n[position] = value
    return array, swaps, comparison

def time_algorithm(algorithm, array):   #function that takes in the algorithm and array
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""    #imports the algorithm unless it is sorted,
                                            # since that is a built in function

    stmt = f"{algorithm} ({array})"

    times = repeat(setup = setup_code, stmt =stmt, repeat =3, number = 10)  #executes the code 10times per repeat

    global sorted_array

    sorted_array, num_swaps, comparison = eval(stmt)    #evaluates the pythonic expression and stores the value into
                                                        #the variables

    print(f"AVERAGE CASE: Algorithm: {algorithm}. Minimum execution time: {min(times)}.\n"
          f"Number of swaps: {num_swaps}. Number of comparisons: {comparison}")

def best_insertion(algorithm, sorted_array):   #makes use of the already sorted array to pass into the bubble_sort
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm} ({sorted_array})"

    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)


    sorted_array, num_swaps, comparison = eval(stmt)


    print(f"BEST CASE: Algorithm: {algorithm}. Minimum execution time: {min(times)}.\n"
          f"Number of swaps: {num_swaps}. Number of comparisons: {comparison}")


def worst_insertion(algorithm, sorted_array):  #using the descending insertion sort the worst case
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm} ({sorted_array})"

    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    reversed_array, num_swaps, comparison = eval(stmt)

    print(f"WORST CASE: Algorithm: {algorithm}. Minimum execution time: {min(times)}.\n"
          f"Number of swaps: {num_swaps}. Number of comparisons: {comparison}")

ARRAY_LENGTH = 10

if __name__ == "__main__":  #calls all functions
    array = [randint(0,1000) for i in range(ARRAY_LENGTH)]
    time_algorithm(algorithm="insertion_sort", array=array)
    best_insertion(algorithm="insertion_sort", sorted_array=sorted_array)
    worst_insertion(algorithm="descending_insertion_sort", sorted_array=sorted_array)