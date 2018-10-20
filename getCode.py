import xml.etree.ElementTree as ET

def getCode (answerString):
    #this scrapes the answer string for the code snippet
    answerString = "<wrapper>" + answerString + "</wrapper>" #string needs to be wrapped for ElementTree library
    allCode = ""
    xmlFile = ET.fromstring(answerString)
    for code in xmlFile.iter('code'):
        allCode = allCode + code.text
    return allCode
