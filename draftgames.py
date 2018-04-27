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
        
def calc_new_elo(self, player_elo, team_1_elo, team_A_elo, score, k):
    """Calculates the new elo of the player"""
    return player_elo + k * (score - (1 / (1 + 10 ** ((team_2_elo - team_A_elo) / 400))))

def find_k():
    """Finds the value of k?"""
    if self.games["WINS"] < 10:
       return(round((-28.8 * self.games["WINS"]) + 320))
    else:
       return(32)

def get_players():
    """Gets the players we are intested in"""
    for x in range(10):
        while not valid:
            valid = True
            if x>5:
                player_name = input("For Team A, Enter player {0} name! ".format(x))
            else:
                player_name = input("For Team 1, Enter player {0} name! ".format(x))
            player = db.users.find_one({"NAME":player_name})
            if player is None:
                print("Warning! No user found with that name")
                valid = False
                
        players.append({x:player})
        
        if x>5: team_A_elo += player["ELO"] 
        else: team_1_elo += player["ELO"]
    
    #get avrage
    team_A_elo /= 5
    team_1_elo /= 5
    k = find_k(players[0]["GAMES"]["WINS"])
        
def get_score():
    """Gets the match score, returns None on fail"""
    try:
        return int(input("Result (1 if team 1 won, 0 if they lost): "))
    except:
        print("Invalid input")
        return None

def update():
    score = None
    while score is None:
        score = get_score()
        
    for num, player in enumerate(players):
        if num>5:
            #team A
            if score == 1:
               add_loss(player)
            else:
                add_win(player)
        else:
            #team 1
            if score == 1:
                add_win(player)
            else:
                add_loss(player)

def add_player(name:str, player_id:str, elo:int=1500, clan:str=""):
    db.users.insert_one(
        {"NAME":name,
         "player_ID": player_id,
         "ELO": elo,
         "HEROS": {"KREEPY":0, "DOC":0, "SARGE":0}, #Needs completing
         "GAMES": {"WINS": 0, "LOSES": 0, "LEFT": 0},
         "CLAN": clan,
        })
         
                
def add_win(player):
    db.users.update_one(
        {'_id': player['_id']},
        {'$inc': {"GAMES.WINS":1}},
        upsert=True
    )
    
def add_loss(player):
    db.users.update(
        {'_id': player['_id']},
        {'$inc': {"GAMES.WINS":-1}},
        upsert=True
    )
                
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
    
