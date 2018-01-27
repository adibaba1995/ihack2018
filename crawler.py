import requests
from bs4 import BeautifulSoup

def checkSignUp(url):
	r = requests.get(url)
	c = r.content

	content = BeautifulSoup(c,"html.parser")

	forms = content.find_all('form')
	for form in forms:
		emails = form.find_all('input', {"type":"email"})

		if emails is not None and len(emails) != 0:
			return True

def getWeight(url):
	hasSignUp = False

	url = 'http://www.ojusapsit.com/'

	if checkSignUp(url):
		hasSignUp = True
	else:
		r = requests.get('http://www.icasteconference.com/')
		c = r.content

		content = BeautifulSoup(c,"html.parser")

		links = content.find_all('a', href=True)
		for link in links:
			if link['href'].startswith("http"):
				if checkSignUp(url):
					hasSignUp = True
					break

	if hasSignUp:
		return 0.25
	else:
		return 0