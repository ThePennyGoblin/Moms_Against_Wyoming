import requests
from bs4 import BeautifulSoup

pd.display.

url = "https://www.fangraphs.com/roster-resource/injury-report?groupby=team"
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

# Example code to extract data (adjust the selectors based on the actual HTML structure)
injury_data = []
table = soup.find('table')  # Find the table element

# Iterate over rows in the table
for row in table.find_all('tr')[1:]:  # Skip header row
    columns = row.find_all('td')
    if len(columns) > 1:
        player_name = columns[0].text.strip()
        injury_description = columns[1].text.strip()
        injury_data.append((player_name, injury_description))

# Print extracted data
for player, injury in injury_data:
    print(f"Player: {player}, Injury: {injury}")
