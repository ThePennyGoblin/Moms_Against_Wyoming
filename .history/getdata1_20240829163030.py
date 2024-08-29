import requests
import pandas as pd
from bs4 import BeautifulSoup

# Step 1: Fetch the webpage content
url = "https://www.fangraphs.com/leaders/major-league?pos=all&stats=bat&lg=all&qual=0&type=8&month=0&ind=1&rost=&age=&filter=&players=0&startdate=&enddate=&season1=2015&season=2024&pageitems=2000000000&team=0%2Cto"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Step 2: Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Step 3: Locate the table
    table = soup.find("table", {"class": "rgMasterTable"})  # Adjust the class if necessary

    # Extract the headers
    headers = [header.text.strip() for header in table.find_all("th")]
    
    # Extract the rows
    rows = []
    for row in table.find_all("tr")[1:]:  # Skip the header row
        cells = row.find_all("td")
        row_data = [cell.text.strip() for cell in cells]
        rows.append(row_data)
    
    # Step 4: Convert the extracted data to a DataFrame
    df = pd.DataFrame(rows, columns=headers)
    
    # Display the DataFrame
    print(df)
else:
    print(f"Failed to retrieve the webpage: {response.status_code}")
