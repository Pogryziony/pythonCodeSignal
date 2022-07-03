def solution(statues):
    missing = 0
    for i in range(max(statues)):
        if i not in statues and i > min(statues):
            missing = missing + 1
    return missing


def betterSolution(statues):
    return max(statues) - min(statues) - len(statues) + 1
