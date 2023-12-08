from collections import Counter

# Read the card data from the file and split each line into a list of cards
cards = [card.split() for card in open("day_7_camel_cards/data.txt")]


# Function to determine the type of card hand
def card_type(hand):
    # Count the occurrences of each card in the hand
    counts = Counter(hand)
    score = []
    wildcards = 0

    # Iterate through the counts and handle wildcards ('J')
    for card, count in counts.items():
        if card == "J" and count < 5:
            wildcards = count
        else:
            score.append(count)

    # If there are wildcards, add them to the highest count
    if wildcards:
        score[score.index(max(score))] += wildcards

    # Sort the score to match with the patterns below
    score.sort()
    # Determine the type of hand based on the score pattern
    match score:
        case [5]:
            return "Five of a kind"
        case [1, 4]:
            return "Four of a kind"
        case [2, 3]:
            return "Full house"
        case [1, 1, 3]:
            return "Three of a kind"
        case [1, 2, 2]:
            return "Two Pair"
        case [1, 1, 1, 2]:
            return "One Pair"
        case _:
            return "High card"


# List of card strings in descending order of rank
card_str = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]


# Function to rank a hand based on the card types
def hand_rank(hand, hand_type):
    # Create a dictionary to map card strings to their rank
    card_str_rank = {card: rank for rank, card in enumerate(card_str, start=1)}

    # Return a list of ranks for the cards in the hand
    return [card_str_rank[card] for card in hand[0] if card in card_str_rank]


# Dictionary to map hand types to their rank
hand_type_rank = {
    "Five of a kind": 1,
    "Four of a kind": 2,
    "Full house": 3,
    "Three of a kind": 4,
    "Two Pair": 5,
    "One Pair": 6,
    "High card": 7,
}

# Initialize a dictionary to group hands by their type
card_types = {hand_type: [] for hand_type in hand_type_rank}

# Group the hands by their type
for idx, hand in enumerate(cards):
    hand_type = card_type(hand[0])
    card_types[hand_type].append(hand)

# Sort the hands first by hand type rank, then by individual card ranks
sorted_hands = []
for hand_type in sorted(hand_type_rank, key=hand_type_rank.get):
    sorted_hands.extend(
        sorted(card_types[hand_type], key=lambda hand: hand_rank(hand, hand_type))
    )

# Calculate the sum of the scores for each hand
total_score = 0
for idx, hand in enumerate(sorted_hands):
    total_score += int(hand[-1]) * (len(sorted_hands) - idx)

# Print the total score
print(total_score)
