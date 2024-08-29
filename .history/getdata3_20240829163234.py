from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from bs4 import BeautifulSoup

# Step 1: Set up Selenium WebDriver (adjust the path to your WebDriver)
driver = webdriver.Chrome(executable_path='path_to_chromedriver')

# Step 2: Load the webpage
url = "https://www.fangraphs.com/leaders/major-league?pos=all&stats=bat&lg=all&qual=0&type=8&month=0&ind=1&rost=&age=&filter=&players=0&startdate=&enddate=&season1=2015&season=2024&pageitems=2000000000&team=0%2Cto"
driver.get(url)

# Step 3: Wait for the table to load (you may need to adjust this if the table takes time to load)
driver.implicitly_wait(10)  # Waits up to 10 seconds

# Step 4: Parse the page with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Step 5: Locate the table and extract data
table = soup.find("table", {"class": "rgMasterTable"})
headers = [header.text.strip() for header in table.find_all("th")]
rows = []
for row in table.find_all("tr")[1:]:
    cells = row.find_all("td")
    row_data = [cell.text.strip() for cell in cells]
    rows.append(row_data)

# Step 6: Convert to DataFrame
df = pd.DataFrame(rows, columns=headers)

# Display the DataFrame
print(df)

# Close the browser
driver.quit()
