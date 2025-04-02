def TwoNTabs(n):
    timesToTab = 0
    timesToTab = 2 * n
    return timesToTab

def TwoNPlus1Tabs(n):
    timesToTab = 0
    timesToTab = 2 * n + 1
    return timesToTab

def TwoNMinus1Tabs(n):
    timesToTab = 0
    timesToTab = 2 * n - 1
    return timesToTab

for lp in range(1, 5 + 1, 1):
    output = TwoNMinus1Tabs(lp)
    print(output)
