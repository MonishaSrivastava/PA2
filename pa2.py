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

Score_file = "score_history.txt" #Python makes this file so it can put your scores in it


def play_quiz(filename):

    flashcards = load_flashcards(filename) #Reads terms/definitions from an existing text/csv file and runs the quiz.
    
    print("\n Starting the flashcard quiz! Type 'quit' to stop early.\n")
 
    score = 0 #start score

    for term, definition in flashcards:
        print(f"Question: {term}")
        answer = input("What is the answer? ").strip().lower()
        if answer.lower() == "quit":
            break
        if answer.lower() == definition:
            print("Correct!\n")
            score += 1
        else:
            print(f"Nope...The correct answer was: {definition}\n")

    print(f"Final Score: {score}\n")
    username = input("Enter your username > ").strip()
    add_scores(username,score)
    print("Your score has been saved!\n")


def load_flashcards(filename):
    flashcards = []
    with open(filename, "r") as f: #read function = r
        for line in f:
            if "-" in line:
                term, definiton = line.split("-", 1) #split() function, # setting the maxsplit parameter to 1, will return a list with 2 elements. https://www.w3schools.com/python/ref_string_split.asp
                flashcards.append((term, definiton)) #reads then adds flashcard but i think i did something wrong in the parantheses...
    return flashcards


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
        
        while first_choice not in e_options:
            for item in initial_choices:
                print(f"- {item}")
            first_choice = input("what would you like to do?\n> ").lower().strip()
            if first_choice in p_options:
                quiz_fn = input("what is the name of your file?\n> ").lower().strip()
                quiz_ext = input("is it a .txt or .csv file?\n> ").lower().strip()
                while quiz_ext not in file_types:
                    print_error()
                    print("your choices are:")
                    for item in file_types:
                        print(f"- {item}")
                    quiz_ext = input("is it a .txt or .csv file?\n> ").lower().strip()
                if quiz_ext in [".csv","csv"]:
                    file_url = quiz_fn+".csv"
                else:
                    file_url = quiz_fn+".txt"
                play_quiz(file_url)
            elif first_choice in h_options:
                show_scores()
            elif first_choice in e_options:
                game_on = False
            else:
                print_error()
        
        print("goodbye!")


if __name__ == "__main__":
    main()
