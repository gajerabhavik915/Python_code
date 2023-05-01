a1 = int(input('How many row would you like to show?'))

# method 1
def generate(numRows):
    final_l = [[1]]

    for i in range(numRows - 1):
        req_l = [0] + final_l[-1] + [0]
        apd_l = []
        for j in range(len(req_l) - 1):
            apd_l.append(req_l[j] + req_l[j + 1])
        final_l.append(apd_l)
    return final_l


print(generate(a1))

# method 2

def generate(numRows):
    final_l = [[1]]

    for i in range(numRows - 1):
        req_l = [0] + final_l[-1] + [0]
        apd_l = []
        for j in range(len(final_l[-1]) + 1):   # here made changes with list
            apd_l.append(req_l[j] + req_l[j + 1])
        final_l.append(apd_l)
    return final_l


print(generate(a1))