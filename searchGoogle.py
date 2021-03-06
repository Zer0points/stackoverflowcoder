from googlesearch import search
BASE_URL = "https://stackoverflow.com/questions/"
def searchGoogle (aQuestion):
    # This function wll search Google and take the top Stack Overflow result and return the questionID (in the url)
	questionID = -1
	for url in search(aQuestion + " stack overflow", stop=5):
		if BASE_URL not in url:
			continue
		questionID = url.lstrip(BASE_URL).split("/")[0]
		if not questionID.isdigit():
			continue
		print(url)
		print(questionID)
		break

	if questionID == -1:
		raise ValueError("Could not find any questions")
	return questionID