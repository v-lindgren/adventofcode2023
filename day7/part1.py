import sys
sys.path.append('../')
from parse_input import parse_input

TYPE_HIGH_CARD = 0
TYPE_ONE_PAIR = 1
TYPE_TWO_PAIRS = 2
TYPE_THREE_OF_A_KIND = 3
TYPE_FULL_HOUSE = 4
TYPE_FOUR_OF_A_KIND = 5
TYPE_FIVE_OF_A_KIND = 6

CARD_VALUES = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10
}

# identify hand type
def get_hand_type(hand):
    card_counts = { x: hand.count(x) for x in hand }

    match max(card_counts.values()):
        case 5:
            return TYPE_FIVE_OF_A_KIND
        case 4:
            return TYPE_FOUR_OF_A_KIND
        case 3:
            if all( x in card_counts.values() for x in (3, 2) ):
                return TYPE_FULL_HOUSE
            else:
                return TYPE_THREE_OF_A_KIND
        case 2:
            if sum(val == 2 for val in card_counts.values()) == 2:
                return TYPE_TWO_PAIRS
            else:
                return TYPE_ONE_PAIR
        case _:
            return TYPE_HIGH_CARD

def value_of(card):
    if card.isdigit():
        return int(card)
    else:
        return CARD_VALUES[card]

def rank(hand, rankings):
    old_rankings = rankings.copy()
    for existing_hand in old_rankings:

        if current_hand_info['type'] > hand_info[existing_hand]['type']:
            rankings.insert(rankings.index(existing_hand), current_hand)
            return rankings

        # Then by cards in each position
        elif current_hand_info['type'] == hand_info[existing_hand]['type']:
            for pos in range(0,5):
                if value_of(current_hand[pos]) > value_of(existing_hand[pos]):
                    rankings.insert(rankings.index(existing_hand), current_hand)
                    return rankings
                elif value_of(current_hand[pos]) < value_of(existing_hand[pos]):
                    break # hand is worse, check against next hand

                # edge case: identical hands, insert in front
                if pos == 4 and value_of(current_hand[pos]) == value_of(existing_hand[pos]):
                    rankings.insert(rankings.index(existing_hand), current_hand)
                    return rankings

    # if it didn't fit in front of anything else, put it at the back.
    if current_hand not in rankings:
        rankings.append(current_hand)
        return rankings

def payout(rankings, hand_info):
    payout = 0

    points = 1
    for hand in rankings[::-1]:
        bet = hand_info[hand]['bet']
        payout += points * bet
        points += 1

    return payout

hands = parse_input('input.txt', 'list')
hand_info = {}
for line in hands:
    hand, bet = line.split(' ')
    hand_info[hand] = {'bet': int(bet)}

# add to dict
for hand, info in hand_info.items():
    info['type'] = get_hand_type(hand)

# Rank hands
rankings = []
for current_hand, current_hand_info in hand_info.items():
    if len(rankings) == 0:

        rankings.append(current_hand)
    else:
        rankings = rank(hand, rankings)

print(payout(rankings, hand_info))