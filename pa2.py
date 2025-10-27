'''
Make a flashcard review game that reads through a file
where each line consists of a term and its definition.

An example text file and an example CSV file have been provided to you.

A masterful program includes the ability to create a new file
and load your own terms/definitions into it, before running the quiz on that file.

Save game records to a different file. Log username and high score.
Allow the user the option to view this file by printing it to the console.

You should at minimum edit the helper functions.
You may not necessarily have to edit the main function.
'''

#Need to ask for help because code is not adding to my score even though I have put the answer in correctly

Score_file = "score_history.txt" #Python makes this file so it can put your saved score + usernames 


def play_quiz(filename):

    flashcards = load_flashcards(filename) #Reads terms/definitions from an existing text/csv file and runs the quiz.
    
    print("Starting the flashcard quiz! Type 'quit' to stop early.\n")
 
    score = 0 #inital score

    for term, definition in flashcards: #for loop goes through each flashcard one by one
        print(f"Question: {term}") #Shows question with the variable defined as {term}
        answer = input("What is the answer? ").strip().lower()
        if answer.lower() == "quit":
            break
        if answer.lower() == definition: #Shows definiton with the variable defined as definition
            print("Correct!\n")
            score += 1
        else:
            print(f"Nope...The correct answer was: {definition}\n")

    print(f"Final Score: {score}\n")
    username = input("Enter your username\n> ").strip()
    add_scores(username,score)
    print("Your score has been saved!\n")


def load_flashcards(filename):
    flashcards = []
    with open(filename, "r") as f: #read function = r; python opens file in read mode
        for line in f:
            if "-" in line: #only processes lines that contain a -
                term, definiton = line.split("-", 1) #split() function, + setting the maxsplit parameter to 1, will return a list with 2 elements. https://www.w3schools.com/python/ref_string_split.asp
                flashcards.append((term, definiton)) 
    return flashcards #returns the list of flashcards


def add_scores(username, score):
    #Record scores in the score history file.
    with open(Score_file, "a") as f:
        f.write(f"{username} : {score}\n")


def show_scores():
    #Print all saved scores from the score history file.

    print("\nScore History:")
    with open(Score_file, "r") as f:
        lines = f.readlines()
        if not lines:
            print("No scores to show.\n")
        else:
            for line in lines:
                print(line)
    print()


def print_error():
    print("*" * 50)
    print(" " * 22 + "error!" + " " * 22)
    print(" " * 12 + "that is not a valid option" + " " * 12)
    print(" " * 17 + "please try again" + " " * 17)
    print("*" * 50)



def main():
    #initialize variables
    initial_choices = ["play","see history","exit"]
    file_types = [".txt", "txt", ".csv", "csv"]
    p_options = ["play","p","play game"]
    h_options = ["see history", "history", "h", "see", "sh", "s"]
    e_options = ["exit","e","exit game"]
    first_choice = ""
    game_on = True

    while game_on:
        print("welcome to the review game")
        
        while first_choice not in e_options: #while not exiting (runs because their first choice is an empty string (== ""), then because they haven't typed 'exit')
            for item in initial_choices: #print out play, see history, and exit
                print(f"- {item}")
            first_choice = input("What would you like to do?\n> ").lower().strip()
            if first_choice in p_options: #playing the game
                quiz_fn = input("What is the name of your file?\n> ").lower().strip()
                quiz_ext = input("Is it a .txt or .csv file?\n> ").lower().strip() 
                while quiz_ext not in file_types: #if it is not a csv or txt then it will raise an error
                    print_error()
                    print("Your choices are:")
                    for item in file_types: #prints out txt and csv
                        print(f"- {item}")
                    quiz_ext = input("Is it a .txt or .csv file?\n> ").lower().strip() #file types that are applicable
                if quiz_ext in [".csv","csv"]: #comma seperated value file
                    file_url = quiz_fn+".csv"
                else:
                    file_url = quiz_fn+".txt"
                play_quiz(file_url)
            elif first_choice in h_options: #looking at previous scores
                show_scores()
            elif first_choice in e_options: #exiting
                game_on = False
            else:
                print_error()
        
        print("goodbye!")


if __name__ == "__main__":
    main()
