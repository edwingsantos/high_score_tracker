#ES 1rst highscore tracker implementation
#score for flappy bird, high schore
#reaction_time for reaction time, high score
#score for score


import csv
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(BASE_DIR, "docs", "accounts.csv")

def highscore_save(game, new_score, account):
    if game == "flappy bird":
        index = 2
    elif game == "reaction time":
        index = 3
    elif game == "pong":
        index = 4

    try:
        with open(CSV_PATH, "r", newline="") as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)
            rows = list(csv_reader)

        user_found = False
        for row in rows:
            if not row:
                continue
            if row[0] == account[0]: 
                current_score = int(row[index]) if row[index] else 0
                if game == "reaction time":
                    if new_score < current_score or current_score == 0:
                        row[index] = new_score
                else:
                    if new_score > current_score:
                        row[index] = new_score
                user_found = True
                break

        if not user_found:
            new_row = [account[0], account[1], 0, 0, 0]
            new_row[index] = new_score
            rows.append(new_row)

        with open(CSV_PATH, "w", newline="") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(header)
            csv_writer.writerows(row for row in rows if row)

    except Exception as e:
        print(f"Error: {e}")

def highscore_print(game):
    scores = []

    if game == "flappy bird":
        index = 2
    elif game == "reaction time":
        index = 3
    elif game == "pong":
        index = 4
    elif game == "all":
        with open(CSV_PATH, "r") as file:
            content = csv.reader(file)
            next(content)
            rows = []
            for line in content:
                rows.append([line[0], line[2], line[3], line[4]])
            
            print("\nUsername: Flappy Bird, Reaction Time Game, Pong")
            for row in rows:
                print(f"{row[0]}: {row[1]}, {row[2]}, {row[3]}")
            print()
            
        return
    else:
        print("Unknown game")
        return

    with open(CSV_PATH, "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            try:
                row[index] = int(row[index])
                scores.append(row)
            except:
                continue

    scores.sort(key=lambda row: row[index], reverse=True)

    if game == "reaction time":
        scores.reverse()
    
    scores = scores[:10]

    print()
    for i in scores:
        print(f"{i[0]}: {i[index]}")
    print()