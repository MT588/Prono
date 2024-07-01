from dotenv import load_dotenv
load_dotenv()
import os
from supabase import create_client, Client # type: ignore

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(url, key)

def add_player(name):
    try:
        supabase.table("Players").insert({"name": name}).execute()
    except:
        print("Player already exists")

def get_player_id(name):
    response, count = supabase.table("Players").select("*").eq("name", name).execute()
    return response[1][0]["id"]

def add_prono(playerid, matchid, T1_score, T2_score):
    try:
        reponse, count = supabase.table("pronomatches").select("*").eq("player", playerid).eq("match", matchid).execute()
        if count == None:
            return
        supabase.table("pronomatches").insert({"player": playerid, "match": matchid, "T1_score": T1_score, "T2_score": T2_score}).execute()
        print("Prono added for player", playerid, "match", matchid, "T1_score", T1_score, "T2_score", T2_score)
    except:
        print("Prono already exists")

def add_all_pronos(playerid, Scores):
    for score in Scores:
        add_prono(playerid, score[0], score[1], score[2])

Scorepatrik = [
    [1, 1, 1],
    [2, 3, 1],
    [3, 1, 0],
    [4, 3, 0],
    [5, 2, 1], 
    [6, 2, 0], 
    [7, 2, 2], 
    [8, 1, 1]
]
ScoreLieve = [
    [1, 1, 1],
    [2, 2, 1],
    [3, 1, 0],
    [4, 3, 0],
    [5, 2, 0],
    [6, 2, 0],
    [7, 1, 1],
    [8, 2, 2]
]
ScoreVincent = [
    [1, 1, 1],
    [2, 2, 1],
    [3, 1, 0],
    [4, 2, 0],
    [5, 1, 0],
    [6, 2, 0],
    [7, 0, 1],
    [8, 1, 1]
]

add_all_pronos(2, Scorepatrik)
add_all_pronos(3, ScoreLieve)
add_all_pronos(4, ScoreVincent)