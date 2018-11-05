def minMoves(avg):
    # Write your code here
    avgOrig = avg
    avgOrig2 = avg
    avgSort = avgOrig.sort()
    avgRev = sorted(avgOrig2,reverse=True)
    if avgOrig == avgSort or avgOrig == avgRev:
        return 0
    upSwap = 0
    downSwap = 0
    # Use bubble sort algorithm as defined in question above
    upSwap = bubbleUp(avg)
    downSwap = bubbleDown(avg)
    print(upSwap)
    print(downSwap)
    if upSwap < downSwap:
        return upSwap
    else:
        return downSwap

def bubbleUp(avg):
    swaps = 0
    for i in range(len(avg)):
            for j in range(0,(len(avg)-i-1)):
                if avg[j] > avg[j+1]:
                    avg[j],avg[j+1] =avg[j+1], avg[j]
                    swaps += 1
    return swaps
def bubbleDown(avg):
    swaps = 0
    for i in range(len(avg)):
        for j in range(0,(len(avg)-i-1)):
            if avg[j] <= avg[j+1]:
                avg[j],avg[j+1] =avg[j+1], avg[j]
                swaps += 1
    return swaps
    
