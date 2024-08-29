from bs4 import BeautifulSoup
import requests

url = "https://www.fangraphs.com/leaders/splits-leaderboards?splitArr=44,8,1&splitArrPitch=&position=B&autoPt=false&splitTeams=false&statType=player&statgroup=2&startDate=2023-03-01&endDate=2023-11-01&players=&filter=AB%7Cgt%7C1&groupBy=season&wxTemperature=&wxPressure=&wxAirDensity=&wxElevation=&wxWindSpeed=&sort=22,1&pageitems=2000000000&pg=0"

response = requests.get(url)
# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")

results = soup.find_all("tr", class_ = "")