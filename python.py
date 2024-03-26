def bubble_sort(array, len_array):
    flag = True

    while flag:
        flag = False
        for i in range(len_array - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                flag = True

    return array

lis = [3, 1, 31425, 2, -1488, 1939, -float('inf')]

print(bubble_sort(lis, len(lis)))
