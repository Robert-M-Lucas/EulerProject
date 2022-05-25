

with open("poker.txt", "r") as f:
    data = f.read()

lines = data.split("\n")

letter_numbers = ["T", "J", "Q", "K", "A"]
cards = []
for i in lines:
    new_line = []
    for j in i.split(" "):
        try:
            num = letter_numbers.index(j[0]) + 10
        except ValueError:
            num = int(j[0])
        new_line.append([int(num), j[1]])
    cards.append(new_line)
print(len(cards))


p1_wins = 0

for hand in cards:
    hands = [hand[:5], hand[5:]]

    highest_cards = [[], []]
    for p in range(2):
        nums = [c for c in hands[p]]
        highest_cards[p] = sorted(nums, reverse=True)

    one_pair = [0, 0]
    two_pair = [0, 0]
    three_kind = [0, 0]
    four_kind = [0, 0]
    for p in range(2):
        hand_dict = {}
        for c in hands[p]:
            if c[0] in hand_dict:
                hand_dict[c[0]] += 1
            else:
                hand_dict[c[0]] = 1

        one_pair_bool = False
        for i in hand_dict.keys():
            if hand_dict[i] == 2:
                if i > one_pair[p] and not one_pair_bool:
                    one_pair[p] = i
                if one_pair_bool:
                    if one_pair[p] > two_pair[p]:
                        two_pair[p] = one_pair[p]
                        one_pair[p] = i
                    if i > two_pair[p]:
                        one_pair[p] = two_pair[p]
                        two_pair[p] = i
                one_pair_bool = True
            elif hand_dict[i] == 3:
                if i > three_kind[p]:
                    three_kind[p] = i
            elif hand_dict[i] == 4:
                if i > four_kind[p]:
                    four_kind[p] = i

    flush = [False, False]
    for p in range(2):
        if hands[p][0][1] == hands[p][1][1] == hands[p][2][1] == hands[p][3][1] == hands[p][4][1]:
            flush[p] = True

    straight = [-1, -1]

    for p in range(2):
        min_c = 20
        max_c = 0
        for c in hands[p]:
            if c[0] < min_c:
                min_c = c[0]
            if c[0] > max_c:
                max_c = c[0]
        if max_c - min_c == 5:
            straight[p] = max_c

    # Only p1 got straight flush
    if straight[0] != -1 and flush[0] and not flush[1]:
        p1_wins += 1
        continue
    # Only p2 got straight flush
    elif straight[1] != -1 and flush[1] and not flush[0]:
        continue
    # p1 got better four kind
    elif four_kind[0] > four_kind[1]:
        p1_wins += 1
        continue
    # opposite
    elif four_kind[1] > four_kind[0]:
        continue
    # only p1 got full house
    elif three_kind[0] > 0 and one_pair[0] > 0 and (three_kind[1] == 0 or one_pair[1] == 0):
        p1_wins += 1
        continue
    # opposite
    elif three_kind[1] > 0 and one_pair[1] > 0 and (three_kind[0] == 0 or one_pair[0] == 0):
        continue
    # straight
    elif straight[0] and not straight[1]:
        p1_wins += 1
        continue
    elif straight[1] and not straight[0]:
        continue
    # three kind
    elif three_kind[0] > three_kind[1]:
        p1_wins += 1
        continue
    elif three_kind[1] > three_kind[0]:
        continue
    # two pairs
    elif two_pair[0] > two_pair[1]:
        p1_wins += 1
        continue
    elif two_pair[1] > two_pair[0]:
        continue
    # one pair
    elif one_pair[0] > one_pair[1]:
        p1_wins += 1
        continue
    elif one_pair[1] < one_pair[0]:
        continue

    for i in range(5):
        if highest_cards[0][i] > highest_cards[1][i]:
            p1_wins += 1
            break
        elif highest_cards[1][i] < highest_cards[0][i]:
            break
    print("Draw?")
print(p1_wins)

