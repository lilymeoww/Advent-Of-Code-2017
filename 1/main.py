from AOCutils import *
import math

puzzleInput = list(int(character) for character in list(importAsStrippedArray("input.txt")[0]))
# puzzleInput = [1,2,1,2]


partOneCount = 0
for posIndex in range(len(puzzleInput)):
    try:
        if puzzleInput[posIndex] == puzzleInput[posIndex+1]:
            partOneCount += puzzleInput[posIndex]
    except:
        if puzzleInput[-1] == puzzleInput[0]:
            partOneCount += puzzleInput[-1]
    posIndex += 1


partTwoCount = 0
for posIndex in range(len(puzzleInput)):
    print((posIndex + len(puzzleInput) / 2) % len(puzzleInput))
    if puzzleInput[posIndex] == puzzleInput[int((posIndex + len(puzzleInput) / 2) % len(puzzleInput))]:
        partTwoCount += puzzleInput[posIndex]
    posIndex += 1

print(f"Part one: {partOneCount}")
print(f"Part two: {partTwoCount}")

