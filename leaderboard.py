try:
    from pymongo import MongoClient
except:
    raise RuntimeError("You do not have the right modules installed")
try:
    client = MongoClient()
    db = client["draftgames-db"]
except:
    raise RuntimeError("Could not load Database!")
    
#base_player = {
#   "NAME": "filler", 
#   "player_ID": "1234", 
#   "ELO":1500, 
#   "HEROS": {"KREEPY":0, "DOC":0, "SARGE":0}, #Needs completing
#   "GAMES": {"WINS": 0, "LOSES": 0, "LEFT": 0},
#   "CLAN": "",
#}

def get_all():
    return db.users.find_all({}).sort("ELO", pymongo.ASCENDING)
    
def display():
    players = get_all()
    print("\n--------------------------------------------------------")
    print("Name".ljust(15), "MMR".ljust(8), "Total".ljust(8), "Wins".ljust(8), "Losses".ljust(8))
    print("--------------------------------------------------------\n")
    for player in players:
        print(str(player["NAME"]).ljust(15), 
              str(player["MMR"]).ljust(8), 
              str(sum([value for x in player["GAMES"].values])).ljust(8), 
              str(player["GAMES"]["WINS"]).ljust(8), 
              str(nplayer["GAMES"]["LOSES"]).ljust(8))

    print()
    input()

