from lxml import etree
import requests
from bs4 import BeautifulSoup as bs


def getContent(link: str) -> str:
    webPage = requests.get(link)
    return str(bs(webPage.content, "html.parser"))

content: str = getContent("https://en.wikipedia.org/wiki/List_of_international_airports_by_country")
html: etree.ElementBase = etree.HTML(content)

RELATIVE_ROOT = '//*[@id="mw-content-text"]/div[1]'
# allNodes: list[etree.ElementBase] = html.xpath(RELATIVE_ROOT+"/*")
allNodes = html.xpath(RELATIVE_ROOT+"/*")
length: int = len(allNodes)

rows = []
for i in range(0, length):
    currentRow = []
    node: etree.ElementBase = allNodes[i]
    if node.tag == 'table' and 'wikitable' in node.get('class'):
        for j in range(1, len(node.xpath("./tbody/tr"))):
            currentRegion = node.xpath("./preceding-sibling::h2[1]/span[@class='mw-headline']")[0].text
            # if/else for sub regions having their name within <a> tag and None for no sub regions in Oceania
            currentSubRegion = None if currentRegion == 'Oceania' \
                else (node.xpath("./preceding-sibling::h3[1]/span[@class='mw-headline']")[0].text \
                if node.xpath("./preceding-sibling::h3[1]/span[@class='mw-headline']")[0].text is not None \
                else node.xpath("./preceding-sibling::h3[1]/span[@class='mw-headline']/a")[0].text)
            # if/else for Oceania countries' having their name within <h3>
            currentCountry = node.xpath("./preceding-sibling::h3[1]/span[@class='mw-headline']")[0].text if currentRegion == 'Oceania' \
                else node.xpath("./preceding-sibling::h4[1]/span[@class='mw-headline']")[0].text
            # try/except for the cities having multiple airports
            try:
                currentCity = node.xpath(f"./tbody/tr[{j+1}]/td/a")[0].text
                currentAirport = node.xpath(f"./tbody/tr[{j+1}]/td[2]/a")[0].text
                currentIATA = node.xpath(f"./tbody/tr[{j+1}]/td[3]")[0].text.strip('\n')
            except IndexError:
                currentCity = node.xpath(f"./tbody/tr[{j+1}]//preceding::*[@rowspan][1]/a")[0].text
                currentAirport = node.xpath(f"./tbody/tr[{j+1}]/td[1]/a")[0].text
                currentIATA = node.xpath(f"./tbody/tr[{j+1}]/td[2]")[0].text.strip('\n')
            currentRow = [currentRegion, currentSubRegion, currentCountry, currentCity, currentAirport, currentIATA]
            rows.append(currentRow)

for i in rows:
    print(i)