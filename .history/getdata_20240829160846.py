from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.fangraphs.com/leaders/major-league?pos=all&stats=bat&lg=all&qual=0&type=8&month=0&ind=1&rost=&age=&filter=&players=0&startdate=&enddate=&season1=2015&season=2024&pageitems=2000000000&team=0%2Cto"
url2 = "https://www.fangraphs.com/api/projections?type=steamer&stats=bat&pos=all&team=0&players=0&lg=all"

response = requests.get(url2)
# print(response.text)
soup = BeautifulSoup(response.text,"html.parser")

result = soup.find_all("a")

print(result[1])

