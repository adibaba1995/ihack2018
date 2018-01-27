import requests
from bs4 import BeautifulSoup

signup_weightage = 0.25

total_weightage = 0

r = requests.get('https://caster.io/users/sign_in')
c = r.content

content = BeautifulSoup(c,"html.parser")

forms = content.find_all('form')
for form in forms:
	emails = form.find_all('input', {"type":"email"})

	if emails is not None and len(emails) != 0:
		total_weightage = total_weightage + signup_weightage
		break

print(total_weightage)