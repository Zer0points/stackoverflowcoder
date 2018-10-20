import requests

def getAnswer(questionId):
    # This function uses the Stack Overflow API to return the top rated answer in xml format for a specific question ID.
    url = "https://api.stackexchange.com/2.2/questions/%s/answers?order=desc&sort=votes&site=stackoverflow&filter=withbody" % (questionId)
    r = requests.get(url)
    data = r.json()
    
    # Exception for no answers
    if len(data['items']) == 0:
    	raise ValueError("No answers for this question")

    answer = data['items'][0]['body']    
    return answer