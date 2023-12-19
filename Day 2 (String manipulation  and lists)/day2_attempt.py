import re

data_list = open("input.txt").read().split("\n")
data_list = list(filter(None, data_list))
    
def is_invalid(num, color, thresholds={"red": 12, "green": 13, "blue": 14}):
    return num > thresholds.get(color, 0)

totala = 0
for game in data_list:
    game = re.split("\W",game)
    game = [x for x in game if x!=""]
    
    valid = True
    for i in range(2,len(game)):
        if game[i].isnumeric():
            if is_invalid(int(game[i]), game[i+1]):
                valid = False
    if valid:
        totala += int(game[1])

print(totala)

totalb = 0
for game in data_list:
    game = re.split("\W",game)
    game = [x for x in game if x!=""]
    
    max_r = 0
    max_g = 0
    max_b = 0

    for i in range(2,len(game)):
        if game[i] == "red":
            if int(game[i-1]) > max_r:
                max_r = int(game[i-1])
        if game[i] == "green":
            if int(game[i-1]) > max_g:
                max_g = int(game[i-1])
        if game[i] == "blue":
            if int(game[i-1]) > max_b:
                max_b = int(game[i-1])
    
    power = max_r * max_g * max_b
    totalb += power

print(totalb)