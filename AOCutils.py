def importAsStrippedArray(inputTextFile):
    outputArray = []
    with open(inputTextFile, "r+") as inputText:
        for line in inputText:
            outputArray.append(line.strip())

    return outputArray