'''
Binary Search - For sorted arrays
* This algorithm applies the divide and conquest method
'''
import random


def binarySearch(array, start, end, obj):
    if start > end:
        return False
    middle = (start + end) // 2
    if array[middle] == obj:
        return f'{True}, index={middle}'
    elif array[middle] < obj:
        return binarySearch(array, middle + 1, end, obj)
    elif array[middle] > obj:
        return binarySearch(array, start, middle - 1, obj) 


if __name__ == '__main__':
    array = sorted([random.randint(0, 100) for i in range(20)])
    print(binarySearch(array, 0, len(array), 2))