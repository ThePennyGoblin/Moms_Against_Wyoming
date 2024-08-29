from bs4 import BeautifulSoup
import requests
import pandas as pd
import json
url = "https://www.fangraphs.com/leaders/major-league?pos=all&stats=bat&lg=all&qual=0&type=8&month=0&ind=1&rost=&age=&filter=&players=0&startdate=&enddate=&season1=2015&season=2024&pageitems=2000000000&team=0%2Cto"
url2 = "https://www.fangraphs.com/api/projections?type=steamer&stats=bat&pos=all&team=0&players=0&lg=all"
url3 = "https://www.fangraphs.com/api/projections?type=steamer&stats=bat&pos=all&team=0&players=0&lg=all"
# response = requests.get(url2)
# # print(response.text)
# soup = BeautifulSoup(response.text,"html.parser")

# result = soup.find_all("a")

# print(result[0])

response = requests.get(url3)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    
    # Step 2: Extract player names and their stats
    players_stats = []
    
    for player in data:
        player_info = {
            "Name": player.get("playername"),
            "Team": player.get("team", "N/A"),
            "G": player.get("g", 0),       # Games
            "AB": player.get("ab", 0),     # At Bats
            "H": player.get("h", 0),       # Hits
            "HR": player.get("hr", 0),     # Home Runs
            "R": player.get("r", 0),       # Runs
            "RBI": player.get("rbi", 0),   # Runs Batted In
            "SB": player.get("sb", 0),     # Stolen Bases
            "AVG": player.get("avg", 0.0), # Batting Average
            "OBP": player.get("obp", 0.0), # On-Base Percentage
            "SLG": player.get("slg", 0.0), # Slugging Percentage
            "wOBA": player.get("woba", 0.0), # Weighted On-Base Average
            "WAR": player.get("war", 0.0)  # Wins Above Replacement
        }
        players_stats.append(player_info)

    # Step 3: Display the data
    for player in players_stats:
        print(player)
else:
    print(f"Failed to retrieve data: {response.status_code}")