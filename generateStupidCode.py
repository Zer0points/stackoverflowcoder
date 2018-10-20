from searchGoogle import searchGoogle
from getAnswer import getAnswer
from getCode import getCode

def generateStupidCode (questionsList):
    perfectCode = []
    for question in questionsList:
        try:
            id = searchGoogle(question)
            print(id)
            answerText = getAnswer(id)
            code = getCode(answerText)
            perfectCode.append(code)
        except ValueError as er:
            print(str(er))
            perfectCode.append("You're fucked.")

    return perfectCode

def test_general_questions():
    questions = ["how to invert an image stack overflow"]
    stupidCode = generateStupidCode(questions)
    print(stupidCode[0])

test_general_questions()