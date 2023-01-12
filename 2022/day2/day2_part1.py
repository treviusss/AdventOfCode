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

convert_inputs = {
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
    "A": "rock",
    "B": "paper",
    "C": "scissors"  
}

win_outcome = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

score = 0

with open('day2_input', 'r') as f:
    for line in f:
        opponent, player = line.strip('\n').split(" ")
        # Convert inputs to be more human friendly
        opponent = convert_inputs[opponent]
        player = convert_inputs[player]
        # Add points based on the shape
        score += shape_points[player]
        # Add points based on the outcome
        if player == opponent:
            score += outcome_points["draw"]
        elif win_outcome[opponent] == player:
            score += outcome_points["lose"]
        else:
            score += outcome_points["win"]


    print(score)


        



    