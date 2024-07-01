from dotenv import load_dotenv
load_dotenv()
import os
from supabase import create_client, Client # type: ignore

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(url, key)

def get_score(T1_ps, T2_ps, T1_as, T2_as):
    score = 0
    if T1_ps == T1_as:
        score += 1
    if T2_ps == T2_as:
        score += 1
    if (T1_ps - T2_ps)>0 and (T1_as - T2_as)>0:
        score += 2
    if (T1_ps - T2_ps)<0 and (T1_as - T2_as)<0:
        score += 2
    if (T1_ps - T2_ps)==0 and (T1_as - T2_as)==0:
        score += 2
    score *= 1.5
    return score


def update_score():
    matches, count = supabase.table("matches").select("*").not_.is_('T1s',None).execute()
    for match in matches[1]:
        pronomatches, count = supabase.table("pronomatches").select("*").eq("match", match["id"]).execute()
        for pronomatch in pronomatches[1]:
            score = get_score(pronomatch["T1_score"], pronomatch["T2_score"],match["T1s"], match["T2s"])
            supabase.table("pronomatches").update({"score": score}).eq("id", pronomatch["id"]).execute()

def calculate_score():
    Players, count = supabase.table("Players").select("*").execute()
    for player in Players[1]:
        pronomatches, count = supabase.table("pronomatches").select("*").eq("player", player["id"]).not_.is_('score',None).execute()
        score = 0.0
        for pronomatch in pronomatches[1]:
            score += pronomatch["score"]
        supabase.table("Players").update({"total_score": score}).eq("id", player["id"]).execute()

update_score()
calculate_score()