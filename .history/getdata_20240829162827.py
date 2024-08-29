import requests
import pandas as pd

# Step 1: Fetch data from the API
url = "https://www.fangraphs.com/api/projections?type=steamer&stats=bat&pos=all&team=0&players=0&lg=all"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    
    # Step 2: Extract player names and their stats and put them into a DataFrame
    players_stats = []
    
    for player in data:
        player_info = {
            "Name": player.get("PlayerName", "N/A"),
            "Team": player.get("Team", "N/A"),
            "G": player.get("G", 0.0),                 # Games
            "AB": player.get("AB", 0.0),               # At Bats
            "H": player.get("H", 0.0),                 # Hits
            "1B": player.get("1B", 0.0),               # Singles
            "2B": player.get("2B", 0.0),               # Doubles
            "3B": player.get("3B", 0.0),               # Triples
            "HR": player.get("HR", 0.0),               # Home Runs
            "R": player.get("R", 0.0),                 # Runs
            "RBI": player.get("RBI", 0.0),             # Runs Batted In
            "BB": player.get("BB", 0.0),               # Walks
            "SO": player.get("SO", 0.0),               # Strikeouts
            "SB": player.get("SB", 0.0),               # Stolen Bases
            "AVG": player.get("AVG", 0.0),             # Batting Average
            "OBP": player.get("OBP", 0.0),             # On-Base Percentage
            "SLG": player.get("SLG", 0.0),             # Slugging Percentage
            "OPS": player.get("OPS", 0.0),             # On-Base Plus Slugging
            "wOBA": player.get("wOBA", 0.0),           # Weighted On-Base Average
            "WAR": player.get("WAR", 0.0),             # Wins Above Replacement
            "wRC+": player.get("wRC+", 0.0),           # Weighted Runs Created Plus
            "ISO": player.get("ISO", 0.0),             # Isolated Power
            "Spd": player.get("Spd", 0.0),             # Speed Score
            "BABIP": player.get("BABIP", 0.0),         # Batting Average on Balls In Play
            "Def": player.get("Def", 0.0),             # Defensive Runs Above Average
            "Off": player.get("Off", 0.0),             # Offensive Runs Above Average
        }
        players_stats.append(player_info)

    # Step 3: Create a Pandas DataFrame
    df = pd.DataFrame(players_stats)

    # Display the DataFrame
    print(df)
    
else:
    print(f"Failed to retrieve data: {response.status_code}")
