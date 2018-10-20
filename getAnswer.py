import requests

def getAnswer(questionID):
    #This function uses the Stack Overflow API to return the answer for a specific question ID.
    answerId = 25491297
    url = "https://api.stackexchange.com/2.2/answers/%s?order=desc&sort=activity&site=stackoverflow&filter=withbody" % (answerId)

    r = requests.get(url)

    print(r)

    answer = "1"
    return answer

result = getAnswer(123)
print(result)