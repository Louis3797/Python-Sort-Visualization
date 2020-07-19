import time

def bubble_sort(data, drawData, timeTick):
    for _ in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                drawData(data, ['#C9F4F4' if x == j or x == j+1 else 'red' for x in range(len(data))] )
                time.sleep(timeTick)
    drawData(data, ['#C9F4F4' for x in range(len(data))])

def partition(data, head, tail, drawData, timeTick):
    border = head
    pivot = data[tail]

    drawData(data, getColorArray(len(data), head, tail, border, border))
    time.sleep(timeTick)

    for j in range(head, tail):
        if data[j] < pivot:
            drawData(data, getColorArray(len(data), head, tail, border, j, True))
            time.sleep(timeTick)

            data[border], data[j] = data[j], data[border]
            border += 1

        drawData(data, getColorArray(len(data), head, tail, border, j))
        time.sleep(timeTick)

    drawData(data, getColorArray(len(data), head, tail, border, tail, True))
    time.sleep(timeTick)

    data[border], data[tail] = data[tail], data[border]

    return border

def quick_sort(data, head, tail, drawData, timeTick):
    if head < tail:
        partitionIndex = partition(data, head, tail, drawData, timeTick)

        #Left partition
        quick_sort(data, head, partitionIndex-1, drawData, timeTick)

        #Roght partition
        quick_sort(data, partitionIndex+1, tail, drawData, timeTick)

def getColorArray(dataLen, head, tail, border, currIndex, isSwapping = False):
    colorArray = []
    for i in range(dataLen):
        if i >= head and i <= tail:
            colorArray.append('gray')
        else:
            colorArray.append('#C9F4F4')
        if i == tail:
            colorArray[i] = 'blue'
        elif i == border:
            colorArray[i] = 'red'
        elif i == currIndex:
            colorArray[i] = 'yellow'

        if isSwapping:
            if i == border or i == currIndex:
                colorArray[i] = 'green'

    return colorArray


def merge_sort(data, drawData, timeTick):
    merge_sort_alg(data, 0, len(data) - 1, drawData, timeTick)


def merge_sort_alg(data, left, right, drawData, timeTick):
    if left < right:
        middle = (left + right) // 2
        merge_sort_alg(data, left, middle, drawData, timeTick)
        merge_sort_alg(data, middle + 1, right, drawData, timeTick)
        merge(data, left, middle, right, drawData, timeTick)


def merge(data, left, middle, right, drawData, timeTick):
    drawData(data, GetColorArray(len(data), left, middle, right))
    time.sleep(timeTick)

    leftPart = data[left:middle + 1]
    rightPart = data[middle + 1: right + 1]

    leftIdx = rightIdx = 0

    for dataIdx in range(left, right + 1):
        if leftIdx < len(leftPart) and rightIdx < len(rightPart):
            if leftPart[leftIdx] <= rightPart[rightIdx]:
                data[dataIdx] = leftPart[leftIdx]
                leftIdx += 1
            else:
                data[dataIdx] = rightPart[rightIdx]
                rightIdx += 1

        elif leftIdx < len(leftPart):
            data[dataIdx] = leftPart[leftIdx]
            leftIdx += 1
        else:
            data[dataIdx] = rightPart[rightIdx]
            rightIdx += 1

    drawData(data, ["#C9F4F4" if x >= left and x <= right else "grey" for x in range(len(data))])
    time.sleep(timeTick)


def GetColorArray(leght, left, middle, right):
    colorArray = []

    for i in range(leght):
        if i >= left and i <= right:
            if i >= left and i <= middle:
                colorArray.append("blue")
            else:
                colorArray.append("red")
        else:
            colorArray.append("grey")

    return colorArray

