N, M = map(int, input().split())
diceList = []
wordList = []

totalWordList = wordList[:]
totalWordList = wordList[:]

for i in range(M):
    wordList.append(input())

for i in range(N):
    diceList.append(input())

print(wordList, diceList)

mainCount = 0

tempWordList = wordList[:]
for word in tempWordList:
    tempDice = diceList[:]
    for x in word:
        for dice in tempDice:
            if x in dice:
                print(x)
                tempDice.remove(dice)
                break
            else:
                print(word)
                tempWordList.remove(word)
                continue
                # break
            print(tempWordList)

# for word in wordList:
#     tempDice = diceList[:]
#     for x in word:
#         for dice in tempDice:
#             if x in dice:
#                 tempDice.remove(dice)
#                 print(x)
#
#                 break
#         print(tempDice)
