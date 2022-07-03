def solution(inputArray):
    productList = []
    for i in range(len(inputArray) - 1):
        productList.append(inputArray[i] * inputArray[i + 1])
    return max(productList)


def betterSolution(inputArray):
    return max([inputArray[i] * inputArray[i+1] for i in range(len(inputArray)-1)])
