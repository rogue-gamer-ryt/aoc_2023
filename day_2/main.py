from collections import defaultdict
import re
import math

data = open("input", "r").read()

valid_counts = {
        "red": 12,
        "green": 13,
        "blue": 14
}
pattern = re.compile(r"Game (\d+):(.*?)(?=(?:Game \d+|$))", re.DOTALL)


def validate(ball_counts):
    for count, ball in ball_counts:
        if count > valid_counts[ball]:
            return False
    else:
        return True
    
def update_min_balls(ball_counts, min_balls):
    for count, ball in ball_counts:
        # print(count, ball, min_balls)
        if count > min_balls[ball]:
            min_balls[ball] = count
    return min_balls


def sum_games(input_text):
    pattern = re.compile(r"Game (\d+):(.*?)(?=(?:Game \d+|$))", re.DOTALL)
    matches = pattern.findall(input_text)

    games = []
    for game_id, match in matches:
        rounds = [s.strip() for s in match.split(';')]
        for round in rounds:
            ball_counts = re.findall(r"(\d+) (green|red|blue)(?:,|$)", round)
            ball_counts = [(int(count), color) for count, color in ball_counts]

            # print(validate(ball_counts))
            if not validate(ball_counts):
                break
        else:
            games.append(int(game_id))
    # print(games)
    print(sum(games))


def power_sets(input_text):
    matches = pattern.findall(input_text)
    res = 0
    for game_id, match in matches:
        rounds = [s.strip() for s in match.split(';')]
        min_balls = defaultdict(int)
        # print(game_id, rounds)
        for round in rounds:
            ball_counts = re.findall(r"(\d+) (green|red|blue)(?:,|$)", round)
            ball_counts = [(int(count), color) for count, color in ball_counts]

            # Before validating
            min_balls = update_min_balls(ball_counts, min_balls)
        power_set = math.prod(min_balls.values())
        res += power_set
        # print(power_set)
    print(res)
    


sum_games(data)
power_sets(data)