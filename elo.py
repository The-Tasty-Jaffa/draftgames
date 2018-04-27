import random
import itertools


#[id, elo, wins, losses]


def elo(player, a, b, score, k):
    return player + k * (score - (1 / (1 + 10 ** ((b - a) / 400))))


def find_k(wins):
    return(round((288 / ((wins + 1))**0.7) + 32))


print("\nDraft Games Match Making\n")


team_1_1_id = input("Player 1: ")
team_1_1_id_fixed = "".join(["#",team_1_1_id])
with open("leaderboard.txt") as f:
    for (num_1_1, line) in enumerate(f):
        if team_1_1_id_fixed in line:
            team_1_1 = int((line.split(","))[1])
            
team_1_2_id = input("Player 2: ")
team_1_2_id_fixed = "".join(["#",team_1_2_id])
with open("leaderboard.txt") as f:
    for (num_1_2, line) in enumerate(f):
        if team_1_2_id_fixed in line:
            team_1_2 = int((line.split(","))[1])

team_1_3_id = input("Player 3: ")
team_1_3_id_fixed = "".join(["#",team_1_3_id])
with open("leaderboard.txt") as f:
    for (num_1_3, line) in enumerate(f):
        if team_1_3_id_fixed in line:
            team_1_3 = int((line.split(","))[1])

team_1_4_id = input("Player 4: ")
team_1_4_id_fixed = "".join(["#",team_1_4_id])
with open("leaderboard.txt") as f:
    for (num_1_4, line) in enumerate(f):
        if team_1_4_id_fixed in line:
            team_1_4 = int((line.split(","))[1])

team_1_5_id = input("Player 5: ")
team_1_5_id_fixed = "".join(["#",team_1_5_id])
with open("leaderboard.txt") as f:
    for (num_1_5, line) in enumerate(f):
        if team_1_5_id_fixed in line:
            team_1_5 = int((line.split(","))[1])

team_a_1_id = input("Player 6: ")
team_a_1_id_fixed = "".join(["#",team_a_1_id])
with open("leaderboard.txt") as f:
    for (num_a_1, line) in enumerate(f):
        if team_a_1_id_fixed in line:
            team_a_1 = int((line.split(","))[1])
            
team_a_2_id = input("Player 7: ")
team_a_2_id_fixed = "".join(["#",team_a_2_id])
with open("leaderboard.txt") as f:
    for (num_a_2, line) in enumerate(f):
        if team_a_2_id_fixed in line:
            team_a_2 = int((line.split(","))[1])

team_a_3_id = input("Player 8: ")
team_a_3_id_fixed = "".join(["#",team_a_3_id])
with open("leaderboard.txt") as f:
    for (num_a_3, line) in enumerate(f):
        if team_a_3_id_fixed in line:
            team_a_3 = int((line.split(","))[1])
            
team_a_4_id = input("Player 9: ")
team_a_4_id_fixed = "".join(["#",team_a_4_id])
with open("leaderboard.txt") as f:
    for (num_a_4, line) in enumerate(f):
        if team_a_4_id_fixed in line:
            team_a_4 = int((line.split(","))[1])

team_a_5_id = input("Player 10: ")
team_a_5_id_fixed = "".join(["#",team_a_5_id])
with open("leaderboard.txt") as f:
    for (num_a_5, line) in enumerate(f):
        if team_a_5_id_fixed in line:
            team_a_5 = int((line.split(","))[1])


a = [team_1_1_id,team_1_1]
b = [team_1_2_id,team_1_2]
c = [team_1_3_id,team_1_3]
d = [team_1_4_id,team_1_4]
e = [team_1_5_id,team_1_5]
f = [team_a_1_id,team_a_1]
g = [team_a_2_id,team_a_2]
h = [team_a_3_id,team_a_3]
i = [team_a_4_id,team_a_4]
j = [team_a_5_id,team_a_5]


both_teams = [a,b,c,d,e,f,g,h,i,j]
all_mmrs = [el[1] for el in both_teams]


team_1 = []
team_a = []


lista = []
listb = []


stuff = [a[1],b[1],c[1],d[1],e[1],f[1],g[1],h[1],i[1],j[1]]
r = int((a[1]+b[1]+c[1]+d[1]+e[1]+f[1]+g[1]+h[1]+i[1]+j[1]) / 2)


for k in range(0, len(stuff)+1):
  for subset in itertools.combinations(stuff, k):
    if len(subset) == 5:
        lista.append(subset)
        listb.append(sum(subset))


to_find = min(listb, key=lambda x:abs(x-r))


gen = [l for l,x in enumerate(listb) if x == to_find]

for l in gen:
  #can't remember what this does but it's necessary
  break


team_1_1 = both_teams[all_mmrs.index(lista[l][0])][0]
team_1_2 = both_teams[all_mmrs.index(lista[l][1])][0]
team_1_3 = both_teams[all_mmrs.index(lista[l][2])][0]
team_1_4 = both_teams[all_mmrs.index(lista[l][3])][0]
team_1_5 = both_teams[all_mmrs.index(lista[l][4])][0]


team_1_list = [team_1_1,team_1_2,team_1_3,team_1_4,team_1_5]
both_teams_list = [item[0] for item in both_teams]
team_a_list = list(set(both_teams_list)-set(team_1_list))


team_a_1 = team_a_list[0]
team_a_2 = team_a_list[1]
team_a_3 = team_a_list[2]
team_a_4 = team_a_list[3]
team_a_5 = team_a_list[4]


team_1_1_id = team_1_1
team_1_2_id = team_1_2
team_1_3_id = team_1_3
team_1_4_id = team_1_4
team_1_5_id = team_1_5
team_a_1_id = team_a_1
team_a_2_id = team_a_2
team_a_3_id = team_a_3
team_a_4_id = team_a_4
team_a_5_id = team_a_5


print("\nTeam 1:\n")
print(str(open("ids.txt").readlines()[int(team_1_1.lstrip("0"))-1]))
print(str(open("ids.txt").readlines()[int(team_1_2.lstrip("0"))-1]))
print(str(open("ids.txt").readlines()[int(team_1_3.lstrip("0"))-1]))
print(str(open("ids.txt").readlines()[int(team_1_4.lstrip("0"))-1]))
print(str(open("ids.txt").readlines()[int(team_1_5.lstrip("0"))-1]))

print("\nTeam A:\n")
print(str(open("ids.txt").readlines()[int(team_a_1.lstrip("0"))-1]))
print(str(open("ids.txt").readlines()[int(team_a_2.lstrip("0"))-1]))
print(str(open("ids.txt").readlines()[int(team_a_3.lstrip("0"))-1]))
print(str(open("ids.txt").readlines()[int(team_a_4.lstrip("0"))-1]))
print(str(open("ids.txt").readlines()[int(team_a_5.lstrip("0"))-1]))


team_1_1_id = "".join(["#",team_1_1_id])
with open("leaderboard.txt") as f:
    for (num_1_1, line) in enumerate(f):
        if team_1_1_id in line:
            num_1_1_new = num_1_1
            text_1_1 = line.split(",")
            team_1_1 = int((line.split(","))[1])
            wins_1_1 = int((line.split(","))[2])
            losses_1_1 = int((line.split(","))[3])

team_1_2_id = "".join(["#",team_1_2_id])
with open("leaderboard.txt") as f:
    for (num_1_2, line) in enumerate(f):
        if team_1_2_id in line:
            num_1_2_new = num_1_2
            text_1_2 = line.split(",")
            team_1_2 = int((line.split(","))[1])
            wins_1_2 = int((line.split(","))[2])
            losses_1_2 = int((line.split(","))[3])

team_1_3_id = "".join(["#",team_1_3_id])
with open("leaderboard.txt") as f:
    for (num_1_3, line) in enumerate(f):
        if team_1_3_id in line:
            num_1_3_new = num_1_3
            text_1_3 = line.split(",")
            team_1_3 = int((line.split(","))[1])
            wins_1_3 = int((line.split(","))[2])
            losses_1_3 = int((line.split(","))[3])

team_1_4_id = "".join(["#",team_1_4_id])
with open("leaderboard.txt") as f:
    for (num_1_4, line) in enumerate(f):
        if team_1_4_id in line:
            num_1_4_new = num_1_4
            text_1_4 = line.split(",")
            team_1_4 = int((line.split(","))[1])
            wins_1_4 = int((line.split(","))[2])
            losses_1_4 = int((line.split(","))[3])

team_1_5_id = "".join(["#",team_1_5_id])
with open("leaderboard.txt") as f:
    for (num_1_5, line) in enumerate(f):
        if team_1_5_id in line:
            num_1_5_new = num_1_5
            text_1_5 = line.split(",")
            team_1_5 = int((line.split(","))[1])
            wins_1_5 = int((line.split(","))[2])
            losses_1_5 = int((line.split(","))[3])

team_a_1_id = "".join(["#",team_a_1_id])
with open("leaderboard.txt") as f:
    for (num_a_1, line) in enumerate(f):
        if team_a_1_id in line:
            num_a_1_new = num_a_1
            text_a_1 = line.split(",")
            team_a_1 = int((line.split(","))[1])
            wins_a_1 = int((line.split(","))[2])
            losses_a_1 = int((line.split(","))[3])

team_a_2_id = "".join(["#",team_a_2_id])
with open("leaderboard.txt") as f:
    for (num_a_2, line) in enumerate(f):
        if team_a_2_id in line:
            num_a_2_new = num_a_2
            text_a_2 = line.split(",")
            team_a_2 = int((line.split(","))[1])
            wins_a_2 = int((line.split(","))[2])
            losses_a_2 = int((line.split(","))[3])

team_a_3_id = "".join(["#",team_a_3_id])
with open("leaderboard.txt") as f:
    for (num_a_3, line) in enumerate(f):
        if team_a_3_id in line:
            num_a_3_new = num_a_3
            text_a_3 = line.split(",")
            team_a_3 = int((line.split(","))[1])
            wins_a_3 = int((line.split(","))[2])
            losses_a_3 = int((line.split(","))[3])

team_a_4_id = "".join(["#",team_a_4_id])
with open("leaderboard.txt") as f:
    for (num_a_4, line) in enumerate(f):
        if team_a_4_id in line:
            num_a_4_new = num_a_4
            text_a_4 = line.split(",")
            team_a_4 = int((line.split(","))[1])
            wins_a_4 = int((line.split(","))[2])
            losses_a_4 = int((line.split(","))[3])

team_a_5_id = "".join(["#",team_a_5_id])
with open("leaderboard.txt") as f:
    for (num_a_5, line) in enumerate(f):
        if team_a_5_id in line:
            num_a_5_new = num_a_5
            text_a_5 = line.split(",")
            team_a_5 = int((line.split(","))[1])
            wins_a_5 = int((line.split(","))[2])
            losses_a_5 = int((line.split(","))[3])


score = int(input("\nResult (1 if team 1 won, 0 if they lost): "))


player = team_1_1
a = (team_1_1 + team_1_2 + team_1_3 + team_1_4 + team_1_5)/5
b = (team_a_1 + team_a_2 + team_a_3 + team_a_4 + team_a_5)/5
k = find_k(wins_1_1)
team_1_1_new = elo(player, a, b, score, k)
text_1_1[1] = round(team_1_1_new)
if score == 1:
    wins_1_1 += 1
elif score == 0:
    losses_1_1 += 1
text_1_1[2] = wins_1_1
text_1_1[3] = losses_1_1

player = team_1_2
a = (team_1_1 + team_1_2 + team_1_3 + team_1_4 + team_1_5)/5
b = (team_a_1 + team_a_2 + team_a_3 + team_a_4 + team_a_5)/5
k = find_k(wins_1_2)
team_1_2_new = elo(player, a, b, score, k)
text_1_2[1] = round(team_1_2_new)
if score == 1:
    wins_1_2 += 1
elif score == 0:
    losses_1_2 += 1
text_1_2[2] = wins_1_2
text_1_2[3] = losses_1_2

player = team_1_3
a = (team_1_1 + team_1_2 + team_1_3 + team_1_4 + team_1_5)/5
b = (team_a_1 + team_a_2 + team_a_3 + team_a_4 + team_a_5)/5
k = find_k(wins_1_3)
team_1_3_new = elo(player, a, b, score, k)
text_1_3[1] = round(team_1_3_new)
if score == 1:
    wins_1_3 += 1
elif score == 0:
    losses_1_3 += 1
text_1_3[2] = wins_1_3
text_1_3[3] = losses_1_3

player = team_1_4
a = (team_1_1 + team_1_2 + team_1_3 + team_1_4 + team_1_5)/5
b = (team_a_1 + team_a_2 + team_a_3 + team_a_4 + team_a_5)/5
k = find_k(wins_1_4)
team_1_4_new = elo(player, a, b, score, k)
text_1_4[1] = round(team_1_4_new)
if score == 1:
    wins_1_4 += 1
elif score == 0:
    losses_1_4 += 1
text_1_4[2] = wins_1_4
text_1_4[3] = losses_1_4

player = team_1_5
a = (team_1_1 + team_1_2 + team_1_3 + team_1_4 + team_1_5)/5
b = (team_a_1 + team_a_2 + team_a_3 + team_a_4 + team_a_5)/5
k = find_k(wins_1_5)
team_1_5_new = elo(player, a, b, score, k)
text_1_5[1] = round(team_1_5_new)
if score == 1:
    wins_1_5 += 1
elif score == 0:
    losses_1_5 += 1
text_1_5[2] = wins_1_5
text_1_5[3] = losses_1_5
    

if score == 1:
    score = 0
elif score == 0:
    score = 1


player = team_a_1
a = (team_1_1 + team_1_2 + team_1_3 + team_1_4 + team_1_5)/5
b = (team_a_1 + team_a_2 + team_a_3 + team_a_4 + team_a_5)/5
k = find_k(wins_a_1)
team_a_1_new = elo(player, a, b, score, k)
text_a_1[1] = round(team_a_1_new)
if score == 1:
    wins_a_1 += 1
elif score == 0:
    losses_a_1 += 1
text_a_1[2] = wins_a_1
text_a_1[3] = losses_a_1

player = team_a_2
a = (team_1_1 + team_1_2 + team_1_3 + team_1_4 + team_1_5)/5
b = (team_a_1 + team_a_2 + team_a_3 + team_a_4 + team_a_5)/5
k = find_k(wins_a_2)
team_a_2_new = elo(player, a, b, score, k)
text_a_2[1] = round(team_a_2_new)
if score == 1:
    wins_a_2 += 1
elif score == 0:
    losses_a_2 += 1
text_a_2[2] = wins_a_2
text_a_2[3] = losses_a_2

player = team_a_3
a = (team_1_1 + team_1_2 + team_1_3 + team_1_4 + team_1_5)/5
b = (team_a_1 + team_a_2 + team_a_3 + team_a_4 + team_a_5)/5
k = find_k(wins_a_3)
team_a_3_new = elo(player, a, b, score, k)
text_a_3[1] = round(team_a_3_new)
if score == 1:
    wins_a_3 += 1
elif score == 0:
    losses_a_3 += 1
text_a_3[2] = wins_a_3
text_a_3[3] = losses_a_3

player = team_a_4
a = (team_1_1 + team_1_2 + team_1_3 + team_1_4 + team_1_5)/5
b = (team_a_1 + team_a_2 + team_a_3 + team_a_4 + team_a_5)/5
k = find_k(wins_a_4)
team_a_4_new = elo(player, a, b, score, k)
text_a_4[1] = round(team_a_4_new)
if score == 1:
    wins_a_4 += 1
elif score == 0:
    losses_a_4 += 1
text_a_4[2] = wins_a_4
text_a_4[3] = losses_a_4

player = team_a_5
a = (team_1_1 + team_1_2 + team_1_3 + team_1_4 + team_1_5)/5
b = (team_a_1 + team_a_2 + team_a_3 + team_a_4 + team_a_5)/5
k = find_k(wins_a_5)
team_a_5_new = elo(player, a, b, score, k)
text_a_5[1] = round(team_a_5_new)
if score == 1:
    wins_a_5 += 1
elif score == 0:
    losses_a_5 += 1
text_a_5[2] = wins_a_5
text_a_5[3] = losses_a_5


text_1_1 = str(text_1_1)
text_1_2 = str(text_1_2)
text_1_3 = str(text_1_3)
text_1_4 = str(text_1_4)
text_1_5 = str(text_1_5)
text_a_1 = str(text_a_1)
text_a_2 = str(text_a_2)
text_a_3 = str(text_a_3)
text_a_4 = str(text_a_4)
text_a_5 = str(text_a_5)


text_1_1 = text_1_1.replace("'", "")
text_1_1 = text_1_1.replace(" ", "")
text_1_1 = text_1_1[1:-3]

text_1_2 = text_1_2.replace("'", "")
text_1_2 = text_1_2.replace(" ", "")
text_1_2 = text_1_2[1:-3]

text_1_3 = text_1_3.replace("'", "")
text_1_3 = text_1_3.replace(" ", "")
text_1_3 = text_1_3[1:-3]

text_1_4 = text_1_4.replace("'", "")
text_1_4 = text_1_4.replace(" ", "")
text_1_4 = text_1_4[1:-3]

text_1_5 = text_1_5.replace("'", "")
text_1_5 = text_1_5.replace(" ", "")
text_1_5 = text_1_5[1:-3]

text_a_1 = text_a_1.replace("'", "")
text_a_1 = text_a_1.replace(" ", "")
text_a_1 = text_a_1[1:-3]

text_a_2 = text_a_2.replace("'", "")
text_a_2 = text_a_2.replace(" ", "")
text_a_2 = text_a_2[1:-3]

text_a_3 = text_a_3.replace("'", "")
text_a_3 = text_a_3.replace(" ", "")
text_a_3 = text_a_3[1:-3]

text_a_4 = text_a_4.replace("'", "")
text_a_4 = text_a_4.replace(" ", "")
text_a_4 = text_a_4[1:-3]

text_a_5 = text_a_5.replace("'", "")
text_a_5 = text_a_5.replace(" ", "")
text_a_5 = text_a_5[1:-3]


lines = open("leaderboard.txt").read().splitlines()
lines[num_1_1_new] = text_1_1
lines[num_1_2_new] = text_1_2
lines[num_1_3_new] = text_1_3
lines[num_1_4_new] = text_1_4
lines[num_1_5_new] = text_1_5
lines[num_a_1_new] = text_a_1
lines[num_a_2_new] = text_a_2
lines[num_a_3_new] = text_a_3
lines[num_a_4_new] = text_a_4
lines[num_a_5_new] = text_a_5
print("\n")
print("\n".join(lines))
open("leaderboard_new.txt","w").write("\n".join(lines))

#© Uppishgryphon 2018 (Sam Hughes)
