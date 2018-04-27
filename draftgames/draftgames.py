from discord.ext import commands
from .utils.chat_formatting import pagify
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
    "HEROS": {"KREEPY":0, "DOC":0, "SARGE":0}, #Needs completing (just some extra stats on the side
    "GAMES": {"WINS": 0, "LOSES": 0, "LEFT": 0, "TOTAL":0,},
    "CLAN": "",
}

class bnl_mmr:
	def __init__(self,bot):
		self.bot=bot

	@commands.command(pass_context=True)
	@checks.mod_or_permissions(manage_channels=True, manage_roles=True)
	async def match(self,ctx):
		"""Updates the MMR"""
		"""Gets the players we are intested in"""
    	for x in range(10):
         	if x>5:
         	    player_name = await get_input(ctx, "For Team A, Enter player {0} name! ".format(x))
        	else:
         	    player_name = await get_input(ctx, "For Team 1, Enter player {0} name! ".format(x))
                
         	player = db.users.find_one({"NAME":player_name})
         	if player is None:
               	await self.bot.say("Warning! No player called that, restarting...")
                return

            if "y" in player_name = await get_input(ctx, "Did the player leave early? ").lower():
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
				if score is not None:
					int(score)
				else:
					return
			except:
				await self.bot.say("That is not a number! ")		
		
		for player in player:
			self.find_k(player["GAMES"]["WINS"])
			self.calc_new_elo(player["ELO"])
	
		
    
	def calc_new_elo(self, player_elo):
    	"""Calculates the new elo of the player"""
    	return player_elo + self.k * (score - (1 / (1 + 10 ** ((self.team_2_elo - self.eam_A_elo) / 400))))

	def find_k(self,wins):
    	"""Finds the value of k?"""
    	if wins < 10:
       		self.k =(round((-28.8 * self.games["WINS"]) + 320))
    	else:
       		self.k = 32


	def update(self):
    	score = None
    	while score is None:
     	   score = get_score()
        
   		for num, player in enumerate(players):
        	if player["player_id"] == "-1":
	    		continue
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

	@commands.command(pass_context=True)
	async def display(self,ctx):
    	players = get_all()
    	msg = "--------------------------------------------------------\n"
    	msg += "Name".ljust(15), "MMR".ljust(8), "Total".ljust(8), "Wins".ljust(8), "Losses".ljust(8)
    	msg += "--------------------------------------------------------\n"
    	for player in players:
        	msg += str(player["NAME"]).ljust(15) 
              	+ str(player["ELO"]).ljust(8) 
              	+ str(sum([value for x in player["GAMES"].values])).ljust(8)
              	+ str(player["GAMES"]["WINS"]).ljust(8) 
              	+ str(nplayer["GAMES"]["LOSES"]).ljust(8)
				+ "\n"

		for page in pagify(msg, [" "], shorten_by=16):
			await self.bot.say(page.lstrip(" "))
	
	@commands.command(pass_context=True)
	@checks.admin_or_permissions(manage_roles=True)
	async def add_player(self, ctx, name:str, player_id:str, elo:int=1500, clan:str=""):
		if player_id <= -1:
			await self.bot.say("Not a valid ID")
			return

    	db.users.insert_one(
        	{"NAME":name,
         	"player_ID": player_id,
         	"ELO": elo,
         	"HEROS": {"KREEPY":0, "DOC":0, "SARGE":0}, #Needs completing
         	"GAMES": {"WINS": 0, "LOSES": 0, "LEFT": 0},
         	"CLAN": clan,
        	})
		self.bot.say("Player added!")
         
                
def add_win(player):
    db.users.update_one(
        {'_id': player['_id']},
        {'$inc': {"GAMES.WINS":1, "GAMES.TOTAL":1}},
        upsert=True
    )
    
def add_loss(player):
    db.users.update(
        {'_id': player['_id']},
        {'$inc': {"GAMES.WINS":-1, "GAMES.TOTAL":1}},
        upsert=True
    )
    
def add_left(player):
    db.users.update(
        {'_id': player['_id']},
        {'$inc': {"GAMES.LEFT":1}},
        upsert=True
    )

def get_all():
    return db.users.find_all({}).sort("ELO", pymongo.ASCENDING)
    
async def get_input(ctx, msg:str, time_out:int=120):
	await self.bot.send_message(ctx.message.channel, msg)
	return await self.bot.wait_for_message(author=ctx.message.author, timeouy=120, channel=ctx.message.channel)

def setup(bot):
	this_cog = BNLMMR(bot)
