

def checkCommonElements(arrayA, arrayB, arrayC):
    i = 0 
    j = 0
    k = 0
    while i < len(arrayA) and j < len(arrayB) and k < len(arrayC):
        if arrayA[i] == arrayB[j] and arrayA[i] == arrayC[k]:
            print(f'{arrayA[i]}')
            i += 1
            j += 1
            k += 1
        elif arrayA[i] < arrayB[j]:
            i += 1
        elif arrayB[j] < arrayC[k]:
            j += 1
        else:
            k += 1


a = [7, 7, 8, 9, 10, 11]
b = [5, 6, 7, 8, 11]
c = [8, 9, 10, 11]
checkCommonElements(a, b, c)  # This will print 8 and 11