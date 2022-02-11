def decabin(n, num, i):
    if n:
        decabin(n//2, num, i-1)
        num[i] = n % 2
        return num


def binary(nbits, tot, generalnums):
    temp = []
    for j in range(tot):
        for i in range(nbits):
            temp.append(0)
        decabin(j, temp, nbits-1)
        generalnums.append(temp.copy())
        temp = []


def grouping(nbits, goodnums1, grupos):
    count = 0
    temp = []
    for i in range(nbits+1):
        for j in range(len(goodnums1)):
            for k in range(nbits):
                if int(goodnums1[j][k]) == 1:
                    count += 1
            if int(count) == i:
                temp.append(goodnums1[j])
            count = 0
        grupos.append(temp.copy())
        temp = []


def answer(nbits, goodnums2, groups, respuestas, r):
    temp = []
    ngroup = []
    tempg = []
    check = 0
    casig = 0
    for i in range(nbits):
        temp.append(0)
    for i in range(r-1):
        for j in range(len(groups[i])):
            for k in range(len(groups[i+1])):
                for w in range(nbits):
                    if groups[i][j][w] != groups[i+1][k][w]:
                        temp[w] = 2
                        check += 1
                    else:
                        temp[w] = groups[i][j][w]
                if int(check) == 1:
                    repd = 0
                    for x in range(len(tempg)):
                        if tempg[x] == temp:
                            repd += 1
                            break
                    if int(repd) == 0:
                        tempg.append(temp.copy())
                        casig += 1
                check = 0
        ngroup.append(tempg.copy())
    r -= 1
    if casig > 0:
        answer(nbits, goodnums2, ngroup, respuestas, r)
    r += 1
    for i in range(r):
        for j in range(len(groups[i])):
            checkf = 0
            for k in range(len(goodnums2)):
                check = 0
                for w in range(nbits):
                    if groups[i][j][w] == goodnums2[k][w] or groups[i][j][w] == 2:
                        check += 1
                    else:
                        break
                if int(check) == nbits:
                    checkf += 1
                    for w in range(nbits):
                        goodnums2[k][w] = -1
            if checkf:
                respuestas.append(groups[i][j].copy())


def select(nbits, goodnums3, respuestas, temporales):
    for i in range(len(temporales)):
        checkf = 0
        for j in range(len(goodnums3)):
            check = 0
            for k in range(nbits):
                if temporales[i][k] == goodnums3[j][k] or temporales[i][k] == 2:
                    check += 1
                else:
                    break
            if int(check) == nbits:
                checkf += 1
                for k in range(nbits):
                    goodnums3[j][k] = -1
        if checkf:
            respuestas.append(temporales[i].copy())


def simplify(nbits, goodnums3, respuestas, temporales1):
    temporales2 = []
    w = 0
    while 1:
        flag = 0
        for i in range(len(goodnums3)):
            checkf = 0
            for j in range(len(temporales1)):
                check = 0
                for k in range(nbits):
                    if temporales1[j][k] == goodnums3[i][k] or temporales1[j][k] == 2:
                        check += 1
                if int(check) == nbits:
                    checkf += 1
                    w = j
            if int(checkf) == 1:
                temporales2.append(temporales1[w].copy())
                for k in range(nbits):
                    temporales1[w][k] = -1
                flag += 1
        if int(flag) == 0:
            break
    select(nbits, goodnums3, respuestas, temporales2)


def impresion(nbits, respuestas):
    check = 0
    final = ''
    for i in range(len(respuestas)):
        letter = 65
        if check:
            final = final +" + "
        for j in range(nbits):
            if respuestas[i][j] == 1 or respuestas[i][j] == 0:
                final = final + chr(letter)
            if respuestas[i][j] == 0:
                final = final + chr(39)
            letter += 1
        check += 1
    return final


def execute(nbits,nums,generalnums):
    goodnums1 = []
    goodnums2 = []
    goodnums3 = []
    for i in range(len(nums)):
        temp1 = []
        temp2 = []
        temp3 = []
        for j in generalnums[i]:
            temp1.append(j)
            temp2.append(j)
            temp3.append(j)
        if int(nums[i]):
            goodnums1.append(temp1)
        if int(nums[i]) == 1:
            goodnums2.append(temp2)
            goodnums3.append(temp3)
    groups = []
    temporales = []
    respuestas = []
    grouping(nbits, goodnums1, groups)
    answer(nbits, goodnums2, groups, temporales, nbits + 1)
    simplify(nbits, goodnums3, respuestas, temporales)
    final = impresion(nbits, respuestas)
    goodnums1.clear()
    goodnums2.clear()
    goodnums3.clear()
    respuestas.clear()
    temporales.clear()
    groups.clear()
    return final


def tam(nbits, generalnums):
    total = 2 ** nbits
    binary(nbits, total, generalnums)
    return total
