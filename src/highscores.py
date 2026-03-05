#ES 1rst highscore tracker implementation
#score for flappy bird, high schore
#reaction_time for reaction time, high score
#score for score


import csv
#define highscore save function with parameters game, new_score, account
def highscore_save(game, new_score, account):
    #depending on the specific game set an index variable to a certain number (ex. game = "flappy bird": index = 2)
    if game == "flappy bird":
        index = 2
    elif game == "reaction time":
        index = 3
    elif game == "pong":
        index = 4
    else:
        print("Invalid game")
        return
    
    rows = []
    user_found = False

    #open csv file and write it as file 
    try:
        with open("docs//accounts.csv", "r") as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                    if row[0] == account[0]:  # match by username
                        user_found = True
                        try:
                            current_score = int(row[index])
                        except:
                            current_score = 0
                        if new_score > current_score:
                            row[index] = new_score
                    rows.append(row)
    except:
        print("File not found")
        return

    if not user_found:
        new_row = [account[0], account[1], 0, 0, 0]
        new_row[index] = new_score
        rows.append(new_row)

    with open("docs/accounts.csv", "w", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(rows)

def highscore_print(game):
    scores = []

    if game == "flappy bird":
        index = 2
    elif game == "reaction time":
        index = 3
    elif game == "pong":
        index = 4
    else:
        print("Invalid game")
        return

    with open("docs//accounts.csv", "r") as file:
        csv_reader = csv.reader(file)

        for row in csv_reader:
            try:
                row[index] = int(row[index])
                scores.append(row)
            except:
                continue
    
    scores.sort(key=lambda row: row[index], reverse=True)

    if game == "reaction time":
        scores.reverse()
    
    print("\nTop 10 scores: ")
    for i, row, in enumerate(scores[:10]):
        print(f"{i+1}. {row[0]}: {row[2]}")
    print()