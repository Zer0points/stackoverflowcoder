from searchGoogle import searchGoogle
from getAnswer import getAnswer
from getCode import getCode

def generateStupidCode (questionsList):
    perfectCode = []
    for elem in questionsList:
        try:
            ID = searchGoogle(elem)
            answerText = getAnswer(ID)
            code = getCode(answerText)
            perfectCode.append(code)
        except ValueError:
            perfectCode.append("You're fucked.")

    return perfectCode