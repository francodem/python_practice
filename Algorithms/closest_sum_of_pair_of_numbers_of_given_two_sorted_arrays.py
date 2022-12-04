def orderArraysSize(arrayA, arrayB):
    """
    This function returns both arrays
    by elements size in ascending order
    """
    if arrayA[0] > arrayB[0]:
        biggest = arrayA
        smallest = arrayB
    elif arrayA[0] < arrayB[0]:
        biggest = arrayB
        smallest = arrayA
    return smallest, biggest


def findPairNumbers(arrayA, arrayB, x):
    """
    This function returns the pair of each one integers
    content in a two sorted arrays which sum of both is
    clostest to a given 'x' integer number
    """
    arrayA, arrayB = orderArraysSize(arrayA, arrayB)
    i = 0
    j = len(arrayB) - 1
    lastDifference = abs((arrayA[i] + arrayB[j]) - x)
    while i < len(arrayA) and j >= 0:
        if (
            abs(arrayA[i] + arrayB[j] - x) < lastDifference
            and arrayA[i] + arrayB[j] < x
        ):
            lastDifference = abs((arrayA[i] + arrayB[j]) - x)
            arrayAIndex = i
            arrayBIndex = j
        elif arrayA[i] + arrayB[j] > x:
            j -= 1
        elif arrayA[i] + arrayB[j] < x:
            i += 1
        else:
            print("OK")
            arrayAIndex = i
            arrayBIndex = j
            break
    return f"{arrayA[arrayAIndex]} and {arrayB[arrayBIndex]}"


if __name__ == "__main__":
    arrayA = [10, 20, 30, 40, 100]
    arrayB = [1, 4, 5, 7]
    x = 106
    print(findPairNumbers(arrayA, arrayB, x))
