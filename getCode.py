def getCode (answerString):
    #this scrapes the answer string for the code snippet

    import xml.etree.ElementTree as ET
    answerString = "<wrapper>" + answerString + "</wrapper>"
    allCode = ""
    xmlFile = ET.fromstring(answerString)
    for code in xmlFile.iter('code'):
        allCode = allCode + code.text
    return allCode

xmlString = "<add><p>You can use the <code>+</code> operator to combine them:</p><pre><code>listone = [1,2,3]\nlisttwo = [4,5,6]\n\nmergedlist = listone + listtwo\n</code></pre>\n\n<p>Output:</p>\n\n<pre><code>&gt;&gt;&gt; mergedlist\n[1,2,3,4,5,6]\n</code></pre>\n</add>"
test = getCode(xmlString)
print(test)
