with open("input.txt", "r") as file:
    data = file.read().split("\n")

def initalise(data):
    num_matches = []
    num_cards = []

    for line in data:
        if line:
            num_cards.append(1) # at least 1 of each scratchcard
            
            card = line.split(":")[1].split("|") # remove unnecessary sections of the string
            winning_num = card[0].split(" ")
            given_num = card[1].split(" ")

            winning_num = [i for i in winning_num if i!=""] # remove empty strings from the list
            given_num = [i for i in given_num if i!=""]

            overlapping_num = [i for i in winning_num + given_num if i in winning_num and i in given_num]
            overlapping_num = list(dict.fromkeys(overlapping_num)) # remove duplicates
            
            num_matches.append(len(overlapping_num))
    
    return num_matches, num_cards

matches, cards = initalise(data)

for i in range(len(cards)):
    num_matches = matches[i]
    for j in range(i + 1, i + num_matches + 1):
        cards[j] += cards[i]

print(sum(cards))
