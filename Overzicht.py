import os
from dotenv import load_dotenv
load_dotenv()
import csv
from supabase import create_client, Client # type: ignore

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(url, key)
def get_all_pronos():
    All_Player_Data = []
    players, count = supabase.table("Players").select("*").execute()
    for player in players[1]:
        playerData = []
        playerData.append(player["name"])
        final = f"{player['T1']} - {player['T2']}"
        playerData.append(final)
        playerData.append(player["Topscorer"])
        playerData.append(str(player["total_score"]).replace(".", ","))
        pronomatches, count = supabase.table("pronomatches").select("*").eq("player", player["id"]).order("match", desc=False).execute()
        for pronomatch in pronomatches[1]:
            score = f'{pronomatch["T1_score"]} - {pronomatch["T2_score"]}'
            playerData.append(score)
        All_Player_Data.append(playerData)
    with open('Overzicht.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        headers = ["Name", "Final", "Topscorer", "Total Score"]
        matches, count = supabase.table("matches").select("*").order("id",desc=False).execute()
        for match in matches[1]:
            headers.append(f"{match['T1']} - {match['T2']}")
        writer.writerow(headers)
        for player in All_Player_Data:
            writer.writerow(player)

get_all_pronos()