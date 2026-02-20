#ES 1rst highscore tracker implementation

#define highscore save function with parameters game, new_score, account
def highscore_safe(game, new_score,account):
    #depending on the specific game set an index variable to a certain number (ex. game = "flappy bird": index = 2)
    index = {}
    #open csv file and write it as file 

        #append a new line to the file with username, password, and the score of the game that the user played as well as zeros for every other score

        #try
            #skip header line

            #make a for loop for line in file 

                #if index is flappy bird (2)
                    #append the score at that index to a list called scores

                #elif index is reaction time (3)
                    #append the score at that index to a list called scores
                    
                #elif index is pong (4)
                    #append the score at that index to a list called scores

        #except print that there is no info in the file 

        #else
            #order scores in order of what is greater (for flappy bird and pong) or lower (for pong)

            #return the first 10 values in scores