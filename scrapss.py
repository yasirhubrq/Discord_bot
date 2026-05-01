import requests
import random
import json
from bs4 import BeautifulSoup
import os
import geocoder

#this function is used to get a random meme from the imgflip api
def get_meme():
    url = "https://api.imgflip.com/get_memes/"
    response = requests.get(url)
    data = json.dumps(response.json())
    if response.status_code == 200:
        memes = json.loads(data)['data']['memes']
        meme = random.choice(memes)
        return meme['url']
    else:
        print("Failed to retrieve memes. Status code:", response.status_code)

#this function is used to scrape the game details from the website and save it in a json file
def game_details():
    game_url = "https://www.gametracker.com/server_info/pakproness.ddns.net:28960/"

    response = requests.get(game_url)
    
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    # 1. Target the specific table
    table = soup.find('div', id='HTML_online_players')

    players = []

    if table:
        # 2. Iterate through rows, skipping the header
        for row in table.find_all('tr')[1:]:
            cols = row.find_all('td')
            
            if len(cols) >= 4:
                # 3. Clean and extract
                rank  = cols[0].get_text(strip=True)
                name  = cols[1].get_text(strip=True)
                score = cols[2].get_text(strip=True)
                time  = cols[3].get_text(strip=True)
                
                # Fixed indentation here
                players.append({
                    "Rank": rank,
                    "Name": name,
                    "Score": score,
                    "Time": time
                })

    # 4. Save to file (Fixed keys to match the dictionary above)
    
    with open('game_details.json', 'w') as f:  
        json.dump(players, f, indent=4)

#this function is used to read the game details from the json file and return it as a string
def player_det():
    game_details()  # Ensure we have the latest data
    with open('game_details.json', 'r') as f:
        data = json.load(f)
    player_info = ""
    for player in data:
        player_info += f"Rank: {player['Rank']}\t, Name: {player['Name']}\t, Score: {player['Score']}\t, Time: {player['Time']}\n"
    return player_info
#this function is used to get the location of an IP address using the geocoder library
def ip_locate(a):
    g = geocoder.ip(a)
    return f"city: {g.city}, state: {g.state}, country: {g.country}"

    
