from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
#import webbrowser as browser

BASEURL = "https://speiseplan.studierendenwerk-hamburg.de"
linksToMensas = []
linksToMeals = []
mensaId = 0

html = urlopen("https://www.studierendenwerk-hamburg.de/studierendenwerk/de/essen/speiseplaene/").read()
mainSite = BeautifulSoup(html, 'html.parser')

for link in mainSite.find_all('a'):
	address = link.get('href')
	if "cafeteria" in address:
		linksToMensas.append(address)

#browser.open(linksToMensas[0])

for site in linksToMensas:
	html1 = urlopen(site)
	singlePage = BeautifulSoup(html1, 'html.parser')
	for link in singlePage.find_all('a'):
		if "Diese Woche" in link.get_text():
			linksToMeals.append(link.get('href'))

for site in linksToMeals:
	site = BASEURL + site
	html1 = urlopen(site)
	singlePage = BeautifulSoup(html1, 'html.parser')
	data = {}
	data['id'] = mensaId
	for title in singlePage.find_all('h1'):
		data['name'] = title.get_text()

	json_data = json.dumps(data)

	with open('json/json' + str(mensaId) + '.txt', 'w') as f:
			print(json_data, file = f)
	mensaId += 1
