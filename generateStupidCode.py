from searchGoogle import searchGoogle
from getAnswer import getAnswer
from getCode import getCode

def generateStupidCode (questionsList):
    perfectCode = []
    for question in questionsList:
        try:
            id = searchGoogle(question)
            answerText = getAnswer(id)
            code = getCode(answerText)
            perfectCode.append(code)
        except ValueError:
            perfectCode.append("You're fucked.")

    return perfectCode