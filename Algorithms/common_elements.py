def checkCommonElements(arrayA, arrayB, arrayC):
    # The arrray A is the most bigger array of the three
    i = 0  # Base array assigned, the most bigger
    j = 0
    k = 0
    while i < len(arrayA):
        try:
            if arrayA[i] == arrayB[j] and arrayA[i] == arrayC[k]:
                print(arrayA[i])
                i += 1
                j += 1
                k += 1

            if arrayA[i] == arrayB[j]:
                print(arrayA[i])
                i += 1
                j += 1

            if arrayA[i] == arrayC[k]:
                print(arrayA[i])
                i += 1
                k += 1

            if arrayA[i] != arrayB[j] and arrayA[i] != arrayC[k]:
                if arrayB[j]:
                    j += 1
                if arrayC[k]:
                    k += 1
            
            if j == len(arrayB):
                arrayB.append(False)
            
            if k == len(arrayC):
                arrayC.append(False)
            
            if arrayB[j] != arrayA[i] and arrayC[k] != arrayA[i]:
                i += 1
        except IndexError:
            break


a = [9, 10, 11, 12]
b = [11, 12, 15, 16]
c = [9, 9, 11, 12, 16]
# common elements will be 9, 11, 12, 16

lengths = {1: len(a), 2: len(b), 3: len(c)}  # O(1) in space
comparation = 0
for i in range(1, len(lengths) + 1):
    if lengths[i] > comparation:
        comparation = lengths[i]
        index = i

match index:
    case 1:
        checkCommonElements(a, b, c)
    case 2:
        checkCommonElements(b, a, c)
    case 3: # index = 3
        checkCommonElements(c, a, b) # arrayA, arrayB, arrayC