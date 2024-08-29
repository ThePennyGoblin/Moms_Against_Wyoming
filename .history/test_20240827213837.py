import requests
from bs4 import BeautifulSoup

url = "https://www.fangraphs.com/roster-resource/injury-report?groupby=team"
response = requests.get(url)
html_content = response.text
