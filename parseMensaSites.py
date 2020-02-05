from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
from datetime import datetime

#import webbrowser as browser

BASEURL = "https://speiseplan.studierendenwerk-hamburg.de"
linksToMensas = []
linksToMeals = []
mensaId = 0
now = datetime.now()
current_time = now.strftime("%d.%m.%Y %H:%M:%S")
finalData = [{"time" : current_time, "data" : {}}]


html = urlopen("https://www.studierendenwerk-hamburg.de/studierendenwerk/de/essen/speiseplaene/").read()
mainSite = BeautifulSoup(html, 'html.parser')

for link in mainSite.find_all('a'):
	address = link.get('href')
	if "cafeteria" in address:
		linksToMensas.append(address)

#browser.open(linksToMensas[0])

for site in linksToMensas:
	html = urlopen(site)
	singlePage = BeautifulSoup(html, 'html.parser')
	for link in singlePage.find_all('a'):
		if "Diese Woche" in link.get_text():
			linksToMeals.append(link.get('href'))

for site in linksToMeals:
	site = BASEURL + site
	html = urlopen(site)
	singlePage = BeautifulSoup(html, 'html.parser')
	data = {}
	data['id'] = mensaId
	for title in singlePage.find_all('h1'):
		data['name'] = title.get_text()
	for dish in singlePage.find_all('p'):
		classTag = dish.get('class')
		if classTag != None and 'dish' in classTag:
			print(dish)

	json_data = json.dumps(data)
	finalData[0]['data'][mensaId] = json_data
	mensaId += 1


with open('dataJSON.txt', 'w') as f:
		print(finalData, file = f)

