from operator import itemgetter


new_list = []
with open("leaderboard.txt") as f:
    for string in f:
        new_list.append(string[1:-4].split(","))


for n in range(len(new_list)):
    new_list[n][1] = int(new_list[n][1])


second_list = []
with open("ids.txt") as f:
    for string in f:
        second_list.append(string[1:-1].split("\t"))


for n in range(len(new_list)-2):
    new_list[n][0] = second_list[n][1]


for n in range(len(new_list)-2):
    try:
        if int(new_list[n][1]) > 1480 and int(new_list[n][1]) < 1520:
            new_list.pop(n)
    except:
        pass

for n in range(len(new_list)-2):
    try:
        if int(new_list[n][1]) > 1480 and int(new_list[n][1]) < 1520:
            new_list.pop(n)
    except:
        pass

for n in range(len(new_list)-2):
    try:
        if int(new_list[n][1]) > 1480 and int(new_list[n][1]) < 1520:
            new_list.pop(n)
    except:
        pass

new_list = sorted(new_list, key=itemgetter(1))
new_list = new_list[::-1]

print("\n--------------------------------------------------------")
print("Name".ljust(15),"MMR".ljust(8),"Total".ljust(8),"Wins".ljust(8),"Losses".ljust(8))
print("--------------------------------------------------------\n")
for n in range(len(new_list)):
    try:
        temp = (str(int(new_list[n][2])+int(new_list[n][3])))
    except:
        temp = 0
    print(str(new_list[n][0]).ljust(15),str(new_list[n][1]).ljust(8),str(temp).ljust(8),str(new_list[n][2]).ljust(8),str(new_list[n][3]).ljust(8))

print()
input()

