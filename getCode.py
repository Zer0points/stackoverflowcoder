from bs4 import BeautifulSoup as bs

def getCode (answerString):
    #this scrapes the answer string for the code snippet
    allCode = ""
    xmlFile = bs(answerString, 'html.parser')

    for code in xmlFile.find_all('code'):
        allCode = allCode + code.string
    if not allCode:
        raise ValueError("No code.")

    return allCode

