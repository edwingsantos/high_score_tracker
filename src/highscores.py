#ES 1rst highscore tracker implementation

#score for flappy bird, high schore
#reaction_time for reaction time, high score
#score for score


import csv
#define highscore save function with parameters game, new_score, account
def highscore_safe(game, new_score,account):
    #depending on the specific game set an index variable to a certain number (ex. game = "flappy bird": index = 2)
    index = {}
    scores = {}
    #open csv file and write it as file 
    with open("docs/accounts.csv","w") as file:
        #append a new line to the file with username, password, and the score of the game that the user played as well as zeros for every other score
        file.append(file)

        csv_reader = csv.reader(file)
        #try
        try:
            #skip header line
            next(csv_reader, None)
            #make a for loop for line in file 
            for line in file:
                #if index is flappy bird (2)
                if index == flappy_bird
                    #append the score at that index to a list called scores
                    score.append(scores)
                #elif index is reaction time (3)
                elif index == reaction_time_game
                    #append the score at that index to a list called scores
                    reaction_time.append(scores)
                #elif index is pong (4)
                elif index == pong
                    #append the score at that index to a list called scores
                    score.append(scores)
            file.close()
        #except print that there is no info in the file 
        except:
            print("File not found")
        #else
        else:
            #order scores in order of what is greater (for flappy bird and pong) or lower (for pong)

            #return the first 10 values in scores