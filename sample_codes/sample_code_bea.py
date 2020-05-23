from algorithms.sort import *

algos = [bitonic_sort, bogo_sort, bubble_sort, bucket_sort, cocktail_shaker_sort, comb_sort, counting_sort, cycle_sort, \
         gnome_sort, max_heap_sort, insertion_sort, merge_sort, pancake_sort, quick_sort, radix_sort, selection_sort, \
         shell_sort]


def create_prompt():
    out = ""
    for i in range(len(algos)):
        out += str(i + 1) + " - " + format_name(algos[i]) + '\n'
    return out


def format_name(s):
    return s.__name__.replace('_', " ").capitalize()


def sort(alg, arr):
    return algos[alg - 1](arr)


if __name__ == "__main__":
    prompt = create_prompt() + "Please choose which sorting algorithm you want to use: "
    alg = int(input(prompt))
    arr = [int(x) for x in input('Please input the array of integers, divided by spaces: ').split()]
    print('-' * 10)
    print('Input: ' + ", ".join([str(x) for x in arr]))
    print('Chosen algorithm: ' + format_name(algos[alg - 1]))
    print('Sorted output: ' + ", ".join([str(x) for x in sort(alg, arr)]))
