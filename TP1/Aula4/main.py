import argparse
from readchar import readkey
import random
import string
import time

# Selects Game Mode
def gameMode():

    parser = argparse.ArgumentParser(description = 'Definition of test mode.')
    parser.add_argument('-utm', '--use_time_mode', type=int,
                    help="Max number of secs for time mode or maximum number of inputs for number of inputs mode.\n")
    parser.add_argument('-mv', '--max_value', type=int,
                    help="Max number of secs for time mode or maximum number of inputs for number of inputs mode.")

    # creates the dictionary with {utm : input , mv : input}
    args = vars(parser.parse_args())
    #assigns the values to the values variable
    mv = args["max_value"]
    utm = args["use_time_mode"]

    # when there is no input to max value, the game will run in time mode
    if mv == None:
        print("User Time Mode selected, you have " + str(utm) + " seconds to type!")
        return {"game_time": utm}
    else:
        print("Maximum Value Mode selected, you have" + str(mv) + "chances!")
        return {"max_input": mv}

# Starts the game with any key
def gameStart():
    print("Press any key to start the game!")
    
    start_key = readkey()
    if start_key != None:
        return True  


def gameTime(t):
    results = {}
    t_end = time.time() + t
    gameStart()
    
    while time.time() < t_end:
        random_letter = random.choice(string.ascii_letters).lower()
        print(random_letter)
        inserted_key = readkey()
        
        if inserted_key == random_letter:
            answer = "Resposta Correta"
        else:
            answer = "Resposta Errada"
        
        print(inserted_key + ":" + answer)
        if inserted_key == " ":
            break

        results[random_letter] = inserted_key
    
    #print(results)
        
    return

def maxInput(m):
    results = {}
    
    gameStart()
    
    for i in range(0, m):
        answer = ""

        random_letter = random.choice(string.ascii_letters).lower()
        inserted_key = readkey()
        
        if inserted_key == random_letter:
            answer = "Resposta Correta"
        else:
            answer = "Resposta Errada"
        
        print(inserted_key + ":" + answer)

        if inserted_key == " ":
            break
        results[random_letter] = inserted_key
    
    #print(results)
        
    return

def main():

    # Defines game type and calls the corresponding mode
    game_type = gameMode()

    # FAZER NA MAIN
    if  list(game_type.keys())[0]== "game_time":
        gameTime(game_type["game_time"])
    else:
        maxInput(game_type["max_input"])

if __name__ == "__main__":
    main()