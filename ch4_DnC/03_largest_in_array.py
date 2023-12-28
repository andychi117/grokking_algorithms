def find_largest(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = find_largest(list[1:])
    return list[0] if list[0] > sub_max else sub_max


print(find_largest([1, 3, 7, 20, 45]))
