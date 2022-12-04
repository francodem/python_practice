def findThePairNumbers(arr, x):
    i = 0
    j = len(arr) - 1
    lastPairSum = 0
    lastDifference = abs(arr[0] + arr[-1] - x)
    while j > i:
        difference = abs(arr[i] + arr[j] - x)
        lastPairSum = arr[i] + arr[j]
        if difference < lastDifference:
            pairFirstIndex = i
            pairSecondIndex = j
            lastDifference = difference
        if lastPairSum > x:
            j -= 1
        elif lastPairSum < x:
            i += 1
        else:
            return arr[i], arr[j]
    return arr[pairFirstIndex], arr[pairSecondIndex]


arr = [3, 4, 5, 9, 12, 28, 45, 56, 102]
x = 114
print(findThePairNumbers(arr, x))