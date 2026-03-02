#ES 1rst highscore tracker implementation
#score for flappy bird, high schore
#reaction_time for reaction time, high score
#score for score


import csv
#define highscore save function with parameters game, new_score, account
def highscore_save(game, new_score, account):
    #depending on the specific game set an index variable to a certain number (ex. game = "flappy bird": index = 2)
    line_to_append = ["username", "password", 0, 0, 0]

    line_to_append[0] = account[0]
    line_to_append[1] = account[1]

    #open csv file and write it as file 
    with open("docs/accounts.csv", "a") as file:
        #append a new line to the file with username, password, and the score of the game that the user played as well as zeros for every other score

        csv_writer = csv.writer(file)
        #try
        try:
            #skip header line
            next(csv_writer, None)
            #if index is flappy bird (2)
            if game == "flappy bird":
                #append the score at that index to a list called scores
                line_to_append[2] = new_score
            #elif index is reaction time (3)
            elif game == "reaction time":
                #append the score at that index to a list called scores
                line_to_append[3] = new_score
            #elif index is pong (4)
            elif game == "pong":
                #append the score at that index to a list called scores
                line_to_append[4] = new_score
            csv_writer.writerow(line_to_append)
        #except print that there is no info in the file 
        except:
            print("File not found")

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

    with open("docs/accounts.csv", "r") as file:
        csv_reader = csv.reader(file)

        for row in csv_reader:
            try:
                row[index] = int(row[index])
                scores.append(row)
            except:
                continue
    
    scores.sort()

    if game == "reaction time":
        scores.reverse()
    
    return scores[:10]