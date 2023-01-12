shape_points = {
    "rock": 1,
    "paper": 2,
    "scissors": 3
}
outcome_points = {
    "win": 6,
    "draw": 3,
    "lose": 0
}

convert_opponent_input = {
    "A": "rock",
    "B": "paper",
    "C": "scissors"  
}

convert_outcome_input = {
    "X": "lose",
    "Y": "draw",
    "Z": "win"  
}

lose_outcome = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

win_outcome = dict(
    zip(
        lose_outcome.values(), lose_outcome.keys()
        )
    )

score = 0

with open('day2_input', 'r') as f:
    for line in f:
        opponent, outcome = line.strip('\n').split(" ")
        # Convert inputs to be more human friendly
        player = ""
        opponent = convert_opponent_input[opponent]
        outcome = convert_outcome_input[outcome]
        # Add points based on the outcome
        if outcome == "draw":
            player = opponent
            score += outcome_points["draw"]
        elif outcome == "lose":
            player = lose_outcome[opponent]
            score += outcome_points["lose"]
        else:
            player = win_outcome[opponent]
            score += outcome_points["win"]

        # Add points based on the shape
        score += shape_points[player]

    print(score)


        



    