def array_length(array):
    if array == []:
        return 0

    return 1 + array_length(array[1:])

print(array_length([1, 2, 3, 4, 5]))
