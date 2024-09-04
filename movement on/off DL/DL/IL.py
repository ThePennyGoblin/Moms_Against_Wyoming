import requests
from bs4 import BeautifulSoup
import pandas as pd

# Base URL
base_url = 'https://www.prosportstransactions.com/baseball/Search/SearchResults.php?Player=&Team=&BeginDate=2000-02-01&EndDate=2024-09-03&DLChkBx=yes&submit=Search'

# List to hold all data
all_data = []

# Start page counter
page_number = 0

while True:
    # Construct the URL with pagination
    url = f'{base_url}&start={page_number * 25}'
    
    # Send a request to the website
    response = requests.get(url)
    
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Locate the table and extract data
    table = soup.find('table', {'class': 'datatable'})
    
    # Check if table exists (there might be no more data after the last page)
    if not table:
        break
    
    # Iterate through the rows of the table
    for row in table.find_all('tr')[1:]:  # Skip the header row
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        all_data.append(cols)
    
    # Increment the page number
    page_number += 1
    
    # Optional: Stop after a certain number of pages to avoid long runtimes during testing
    # if page_number > 5:
    #     break

# Convert the data to a pandas DataFrame
df = pd.DataFrame(all_data, columns=['Date', 'Team', 'Acquired', 'Relinquished', 'Notes'])

# Save the data to a CSV file
df.to_csv('baseball_transactions_all_pages.csv', index=False)

# Display the DataFrame (Optional)
print(df)


