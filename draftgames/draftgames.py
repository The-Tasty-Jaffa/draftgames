from discord.ext import commands
from .utils.chat_formatting import pagify, box
from .utils import checks

try:
    import pymongo
    from pymongo import MongoClient
except:
    raise RuntimeError("You do not have the right modules installed")
try:
    client = MongoClient()
    db = client["draftgames-db"]
except:
    raise RuntimeError("Could not load Database!")
    
base_player = {
    "NAME": "filler", 
    "player_ID": "-1", 
    "ELO":1500,
    "GAMES": {"WINS": 0, "LOSSES": 0, "LEFT": 0, "TOTAL":0,},
    "CLAN": "",
}

class draftgames:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @checks.mod_or_permissions(manage_channels=True, manage_roles=True)
    async def match(self, ctx):
        """Updates the MMR"""
        for x in range(10):
            if x>5:
                player_name = await self.get_input(ctx, "For Team A, Enter player {0} name! ".format(x))
            else:
                player_name = await self.get_input(ctx, "For Team 1, Enter player {0} name! ".format(x))
            
            player = db.users.find_one({"NAME":player_name.content})
            if player is None:
                await self.bot.say("Warning! No player called that, restarting...")
                return
            
            responce = await self.get_input(ctx, "Did the player leave early? ").lower()
            if responce is not None and "y" in responce:
                add_loss(player)
                add_left(player)
                player = base_player 
        	    
            players.append({x:player})
                    
            if x>5: team_A_elo += player["ELO"] 
            else: team_1_elo += player["ELO"]
    
        #get average
        self.team_A_elo /= 5
        self.team_1_elo /= 5
                
        valid = False
        attempts = 0
        while not valid:
            score = await get_input(ctx, "Who won? __**(1 if Team 1 won 0 otherwise)?**__ ")
            attempts += 1
            try:
                if score is not None: int(score)
                else: return
            except:
                await self.bot.say("That is not a number! ")		
                
            if attempts >= 4:
                await self.bot.say("Too many attempts... restarting")
                return

            #update PLayers
            self.update(players, score)
            
    def update(self, players, score):
        for num, player in enumerate(players):
            if player["player_id"] == "-1":
                continue
            if num>5:
                #team A
                if score == 1:
                    change_elo(player, team = teamA, opp_team = team1, win=0)
                    add_loss(player)
                else:
                    change_elo(player, team = teamA, opp_team = team1, win=1)
                    add_win(player)
                        
            else:
                #team 1
                if score == 1:
                    change_elo(player, team = team1, opp_team = teamA, win=1)
                    add_win(player)

                else:
                    change_elo(player, team = team1, opp_team = teamA, win=0)
                    add_loss(player)
                            
    @commands.command(pass_context=True)
    async def display(self, ctx):
        """Displays the leaderboard"""
        msg = "-| Clan |      Name       |   MMR   | Total | Wins  | Losses | Left \n"
        for player in db.users.find().sort("ELO", pymongo.ASCENDING):
            msg += "+" + "| {0:<4} | {1:<15} | {2:<7} | {3:<5} | {4:<5} | {5:<6} | {6:<5}\n".format(
                     player["CLAN"], 
                     player["NAME"],
                     player["ELO"],
                     player["GAMES"]["TOTAL"],
                     player["GAMES"]["WINS"],
                     player["GAMES"]["LOSSES"],
                     player["GAMES"]["LEFT"]
                     )
                
        for page in pagify(msg, [" "], shorten_by=16):
            await self.bot.say(box(page.lstrip(" "), lang="diff"))
                
    @commands.command(pass_context=True)
    @checks.admin_or_permissions(manage_roles=True)
    async def add_player(self, ctx, name:str, player_id:int, elo:int=1500, wins:int=0, losses:int=0, clan:str=""):
        """Adds a player to the Data base"""
        if  player_id <= -1:
            await self.bot.say("Not a valid ID")
            return
            
        db.users.insert_one(
                    {"NAME":name,
                        "player_ID": player_id,
                        "ELO": elo,
                        "GAMES": {"WINS": wins, "LOSSES": losses, "LEFT": 0, "TOTAL":wins+losses},
                        "CLAN": clan,
                        })
                    
        await self.bot.say("Player added!")
         
    async def get_input(self, ctx, msg:str, time_out:int=120):
        await self.bot.send_message(ctx.message.channel, msg)
        return await self.bot.wait_for_message(author=ctx.message.author, timeout=time_out, channel=ctx.message.channel)

    @commands.command(pass_context=True)
    async def creatematch(self):
	"""Creates a match"""
	pass

              
def add_win(player):
    db.users.update_one(
        {'_id': player['_id']},
        {'$inc': {"GAMES.WINS":1, "GAMES.TOTAL":1}},
        upsert=True
    )
    
def add_loss(player):
    db.users.update(
        {'_id': player['_id']},
        {'$inc': {"GAMES.LOSSES":1, "GAMES.TOTAL":1}},
        upsert=True
    )
    
def add_left(player):
    db.users.update(
        {'_id': player['_id']},
        {'$inc': {"GAMES.LEFT":1}},
        upsert=True
    )

def change_elo(player, team, opp_team, win):
    """Updates Players elo"""
    db.users.update(
            {'_id': player['_id']},
            {'$inc': {"ELO": 32 * (win - (1/(1+10 ** ((team - opp_team) /400))))}},
                )

def setup(bot):
	this_cog = draftgames(bot)
	bot.add_cog(this_cog)
