from urllib.request import urlopen
from bs4 import BeautifulSoup
import webbrowser as browser

html = urlopen("https://www.studierendenwerk-hamburg.de/studierendenwerk/de/essen/speiseplaene/").read()
mainSite = BeautifulSoup(html, 'html.parser')
BASEURL = "https://speiseplan.studierendenwerk-hamburg.de"
linksToMensas = []
linksToMeals = []

for link in mainSite.find_all('a'):
	address = link.get('href')
	if "cafeteria" in address:
		linksToMensas.append(address)

#browser.open(linksToMensas[0])

for site in linksToMensas:
	html1 = urlopen(site)
	singlePage = BeautifulSoup(html1, 'html.parser')
	for link in singlePage.find_all('a'):
		address = link.get('href')
		if "/de/"  in address and "/0/"  in address and not "/pdf/" in address:
			linksToMeals.append(address)
'''
				with open('output.txt', 'a') as f:
					print(BASEURL + address, file = f) 
'''
site = linksToMeals[len(linksToMeals)-3]
site = BASEURL + site
html1 = urlopen(site)
singlePage = BeautifulSoup(html1, 'html.parser')
with open('oneMealPlan.txt', 'w') as f:
		print(singlePage.prettify(), file = f)
		print("\n", file = f)



