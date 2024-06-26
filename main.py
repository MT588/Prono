from dotenv import load_dotenv
load_dotenv()
import os
from supabase import create_client, Client # type: ignore

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(url, key)

response, count = supabase.table("matches").select("*").execute()
print(response)

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
    return score

def update_score(matchid,playerid,T1_score,T2_score):
    response2, count = supabase.table("pronomatches").select("*").eq("match", matchid).eq("player", playerid).execute()
    playerProno = response2[1][0]
    score = get_score(playerProno["T1_score"],playerProno["T2_score"],T1_score,T2_score)
    supabase.table("pronomatches").update({"score": score}).eq("match", matchid).eq("player", playerid).execute()
    print("Score updated for match",matchid,"player",playerid,"score",score)

    

update_score(1,1,2,0)
update_score(2,1,1,1)