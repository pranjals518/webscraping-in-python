url = "https://www.worldometers.info/gdp/nepal-gdp/"
import requests
html = requests.get(url).content
from bs4 import BeautifulSoup
tree = BeautifulSoup(html,'html.parser')
tbody =tree.find('tbody')
table_rows = tbody.find_all('tr')
whole_data = []
whole_data = []
for tr in table_rows:
    yearly_data = []
    td = tr.find_all('td')
    
    for item in td:
        yearly_data.append(item.text.strip())