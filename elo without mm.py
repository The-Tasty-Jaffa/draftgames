#[id, elo, wins, losses]


def elo(player, a, b, score, k):
    return player + k * (score - (1 / (1 + 10 ** ((b - a) / 400))))


def find_k(wins):
    if wins < 10:
        return(round((-28.8 * wins) + 320))
    else:
        return(32)


team_1_1_id = input("Team 1, player 1 ID: ")
team_1_1_id = "".join(["#",team_1_1_id])
with open("leaderboard.txt") as f:
    for (num_1_1, line) in enumerate(f):
        if team_1_1_id in line:
            num_1_1_new = num_1_1
            text_1_1 = line.split(",")
            team_1_1 = int((line.split(","))[1])
            wins_1_1 = int((line.split(","))[2])
            losses_1_1 = int((line.split(","))[3])

team_1_2_id = input("Team 1, player 2 ID: ")
team_1_2_id = "".join(["#",team_1_2_id])
with open("leaderboard.txt") as f:
    for (num_1_2, line) in enumerate(f):
        if team_1_2_id in line:
            num_1_2_new = num_1_2
            text_1_2 = line.split(",")
            team_1_2 = int((line.split(","))[1])
            wins_1_2 = int((line.split(","))[2])
            losses_1_2 = int((line.split(","))[3])

team_1_3_id = input("Team 1, player 3 ID: ")
team_1_3_id = "".join(["#",team_1_3_id])
with open("leaderboard.txt") as f:
    for (num_1_3, line) in enumerate(f):
        if team_1_3_id in line:
            num_1_3_new = num_1_3
            text_1_3 = line.split(",")
            team_1_3 = int((line.split(","))[1])
            wins_1_3 = int((line.split(","))[2])
            losses_1_3 = int((line.split(","))[3])

team_1_4_id = input("Team 1, player 4 ID: ")
team_1_4_id = "".join(["#",team_1_4_id])
with open("leaderboard.txt") as f:
    for (num_1_4, line) in enumerate(f):
        if team_1_4_id in line:
            num_1_4_new = num_1_4
            text_1_4 = line.split(",")
            team_1_4 = int((line.split(","))[1])
            wins_1_4 = int((line.split(","))[2])
            losses_1_4 = int((line.split(","))[3])

team_1_5_id = input("Team 1, player 5 ID: ")
team_1_5_id = "".join(["#",team_1_5_id])
with open("leaderboard.txt") as f:
    for (num_1_5, line) in enumerate(f):
        if team_1_5_id in line:
            num_1_5_new = num_1_5
            text_1_5 = line.split(",")
            team_1_5 = int((line.split(","))[1])
            wins_1_5 = int((line.split(","))[2])
            losses_1_5 = int((line.split(","))[3])

team_a_1_id = input("Team A, player 1 ID: ")
team_a_1_id = "".join(["#",team_a_1_id])
with open("leaderboard.txt") as f:
    for (num_a_1, line) in enumerate(f):
        if team_a_1_id in line:
            num_a_1_new = num_a_1
            text_a_1 = line.split(",")
            team_a_1 = int((line.split(","))[1])
            wins_a_1 = int((line.split(","))[2])
            losses_a_1 = int((line.split(","))[3])

team_a_2_id = input("Team A, player 2 ID: ")
team_a_2_id = "".join(["#",team_a_2_id])
with open("leaderboard.txt") as f:
    for (num_a_2, line) in enumerate(f):
        if team_a_2_id in line:
            num_a_2_new = num_a_2
            text_a_2 = line.split(",")
            team_a_2 = int((line.split(","))[1])
            wins_a_2 = int((line.split(","))[2])
            losses_a_2 = int((line.split(","))[3])

team_a_3_id = input("Team A, player 3 ID: ")
team_a_3_id = "".join(["#",team_a_3_id])
with open("leaderboard.txt") as f:
    for (num_a_3, line) in enumerate(f):
        if team_a_3_id in line:
            num_a_3_new = num_a_3
            text_a_3 = line.split(",")
            team_a_3 = int((line.split(","))[1])
            wins_a_3 = int((line.split(","))[2])
            losses_a_3 = int((line.split(","))[3])

team_a_4_id = input("Team A, player 4 ID: ")
team_a_4_id = "".join(["#",team_a_4_id])
with open("leaderboard.txt") as f:
    for (num_a_4, line) in enumerate(f):
        if team_a_4_id in line:
            num_a_4_new = num_a_4
            text_a_4 = line.split(",")
            team_a_4 = int((line.split(","))[1])
            wins_a_4 = int((line.split(","))[2])
            losses_a_4 = int((line.split(","))[3])

team_a_5_id = input("Team A, player 5 ID: ")
team_a_5_id = "".join(["#",team_a_5_id])
with open("leaderboard.txt") as f:
    for (num_a_5, line) in enumerate(f):
        if team_a_5_id in line:
            num_a_5_new = num_a_5
            text_a_5 = line.split(",")
            team_a_5 = int((line.split(","))[1])
            wins_a_5 = int((line.split(","))[2])
            losses_a_5 = int((line.split(","))[3])


score = int(input("Result (1 if team 1 won, 0 if they lost): "))


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
print("\n".join(lines))
open("leaderboard_new.txt","w").write("\n".join(lines))
