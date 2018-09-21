def parseLogText(aLogText):
    aLogLineArray = keepFreeText(aLogText, " : ")
    return compareLogLinesWithin(aLogLineArray, ":")


def keepFreeText(aLogText, aToken):
    aLogArray = splitTextIntoByToken(aLogText, "\n")
    aLogLineArray = []
    for logLine in aLogArray:
        aLogLineArray.append(removeTagsFromLineAfterToken(logLine, aToken))
    return aLogLineArray


def compareLogLinesWithin(aLogLineArray, aToken):
    structuredLine = ""
    aStructuredLogLineList = []
    for line in aLogLineArray:
        similarLines = list(filter(lambda a: sameLength(line, a, aToken), aLogLineArray))
        similarLines.remove(line)
        structuredLine = getStructuredLine(line, similarLines, aToken)
        aStructuredLogLineList.append(structuredLine)
    return makeSet(aStructuredLogLineList)


def getStructuredLine(aLine, aListOfLines, aToken):
    structuredLine = aLine
    for similar in aListOfLines:
        answer = structurizedSimilarLines(aLine, similar, 2, aToken)
        if structuredLine.count("*") < answer.count("*"):
            structuredLine = answer
    return structuredLine


def structurizedSimilarLines(aLogLine, anotherLogLine, maxParamValues, aToken):
    if bothHaveTheToken(aLogLine, anotherLogLine, aToken):
        return structurizedLogLineConsideringToken(aLogLine, anotherLogLine, maxParamValues, aToken)
    if not(hasToken(aLogLine, aToken)) & (not(hasToken(anotherLogLine, aToken))):
        return structurizedLogLines(aLogLine, anotherLogLine, maxParamValues)


def structurizedLogLineConsideringToken(aLogLine, anotherLogLine, maxParamValues, aToken):
    firstLogLine = splitTextIntoByToken(aLogLine, aToken)
    secondLogLine = splitTextIntoByToken(anotherLogLine, aToken)

    structuredLine = structurizedLogLines(firstLogLine[0], secondLogLine[0], maxParamValues)
    structuredLineArray = [structuredLine]
    structuredLineArray.append("")
    structuredLineArray[1] = firstLogLine[1]
    if firstLogLine[1] != secondLogLine[1]:
        structuredLineArray[1] = " *"
    return aToken.join(structuredLineArray)


def structurizedLogLines(aLogLine, anotherLogLine, maxParamValues):
    logLineList = splitTextIntoByToken(aLogLine, " ")
    anotherLogLineList = splitTextIntoByToken(anotherLogLine, " ")
    structuredLine = structurizedLineList(logLineList, anotherLogLineList)
    if structuredLine.count("*") > maxParamValues:
        return aLogLine
    return structuredLine


def structurizedLineList(aLineList, anotherLineList):
    structuredLineList = []
    for index in range(len(aLineList)):
        aWord = aLineList[index]
        anotherWord = anotherLineList[index]
        structuredLineList.append(structurizedIfEqualWords(aWord, anotherWord))
    return " ".join(structuredLineList)


def structurizedIfEqualWords(aWord, anotherWord):
    if aWord != anotherWord:
        return "*"
    return aWord


def bothHaveTheToken(aLogLine, anotherLogLine, aToken):
    return hasToken(aLogLine, aToken) & hasToken(anotherLogLine, aToken)


def hasToken(aLogLine, aToken):
    return (aLogLine.count(aToken) > 0)


def sameLength(aLogLine, anotherLogLine, aToken):
    if (bothHaveTheToken(aLogLine, anotherLogLine, aToken)):
        aLine = splitTextIntoByToken(aLogLine, aToken)
        aLine = splitTextIntoByToken(aLine[0], " ")
        anotherLine = splitTextIntoByToken(anotherLogLine, aToken)
        anotherLine = splitTextIntoByToken(anotherLine[0], " ")
        return len(aLine) == len(anotherLine)
    if not(hasToken(aLogLine, aToken)) & (not(hasToken(anotherLogLine, aToken))):
        logLineList = splitTextIntoByToken(aLogLine, " ")
        anotherLogLineList = splitTextIntoByToken(anotherLogLine, " ")
        return len(logLineList) == len(anotherLogLineList)
    return False


def removeTagsFromLineAfterToken(aLogLine, aToken):
    log = splitTextIntoByToken(aLogLine, aToken)
    lastIndex = len(log) - 1
    return "".join(log[lastIndex])


def splitTextIntoByToken(aText, aToken):
    return aText.split(aToken)


def makeSet(aList):
    set = []
    for index in range(len(aList)):
        if set.count(aList[index]) == 0:
            set.append(aList[index])
    return set


def appendWith(aList, anotherList):
    for elem in anotherList:
        aList.append(elem)
    return aList
