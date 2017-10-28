V = " abcdefghijklmnopqrstuvwxyz"
VList = list(V)
VLtoN = {}
VNtoL = {}
for index in range(len(VList)):
    VLtoN[VList[index]] = index
    VNtoL[index] = VList[index]

def encrypt(s):
    vS = []
    for x in s:
        vS.append(VLtoN[x])
    # print(vS)

    uS = []
    uSS = []
    addd = 0
    for x in vS:
        uSS.append(x)

        addd += x

        uS.append(addd)
    # print(uSS)
    # print(uS)
    for x in range(len(uS)):
        uS[x] = uS[x] % 27

    cipher = ""

    for x in uS:
        cipher += VNtoL[x]

    print(cipher)

def removeMod(dNum):
    # f = 13
    l = [dNum[0]]

    for x in range(1, len(dNum)):
        l.append(l[-1] + (dNum[x] - l[-1]) % 27)
    # return (13 + (x-f)%27)
    return l

def decrypt(s):
    dNum = []

    for x in s:
        dNum.append(VLtoN[x])
    # print(dNum)
    dNum = removeMod(dNum)
    newDNum = []
    for x in range(len(dNum)-1, 0, -1):
        newDNum.append(dNum[x]-dNum[x-1])
        # print(x)
    newDNum.append(dNum[0])
    finDnum = []
    for x in range(len(newDNum)-1,-1,-1):
        finDnum.append(newDNum[x])

    # print(finDnum)
    finS = ""
    for x in finDnum:
        finS += VNtoL[x]
    print(finS)


# encrypt("my pie")
# decrypt("mkk in")



t = int(input())
for x in range(t):
    s = input()
    if s[0] == 'e':
        encrypt(s[2:])
    else:
        decrypt(s[2:])
# encrypt(s)

# for x in cipher
