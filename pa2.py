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
#WWW > I think I was proud of the fact that I was able to learn a new string function called split.() which basically allowed python to spit a sentence into two parts based on whatever is defined (in my class it was the dash).  I also was proud of the fact that I was able to get python to create a new file (score_history.txt) where all saved scores and usernames were placed. I ran into the problem when even though I knew my code was correct and that it should be running properly with any file type (if they have the valid seperators) like the periodic_table.txt it would say "file not found" but i ended up figuring out that it wasn't in my PA2 folder which raises an error for python because it can't seem to find it in my computer. I also learnt what tuples are so I think that is pretty cool too.
#EBI > It would be nice if I had a function where I could delete all previous history in my saved file. I also think it would be cool: for a question where there is a lot of possibilities I could make it so if someone types one of the correct answers it would be correct instead of incorrect. I also hoped that I could figure how to make it so if you got the filename wrong you would still be able to go back to the question

f = open("Score_file", "x") #Python makes this file so it can put your saved score + usernames https://www.w3schools.com/python/python_file_write.asp


def play_quiz(filename):

    flashcards = load_flashcards(filename) #Reads terms/definitions from an existing text/csv file and runs the quiz.
    
    print("Starting the flashcard quiz! Type 'quit' to stop early.\n")
 
    score = 0 #inital score

    for term, definition in flashcards: #Python goes through each flashcard one by one in file
        print(f"Question: {term}") #Shows question with the variable defined as {term}
        answer = input("What is the answer? ").strip()
        if answer.lower() == "quit":
            break #stops the code
        if answer.lower().strip() == definition: #Shows definiton with the variable defined as definition
            print("Correct!\n")
            score += 1
        else:
            print(f"Nope...The correct answer was: {definition}\n")

    print(f"Final Score: {score}\n")
    username = input("Enter your username\n> ").strip()
    add_scores(username,score)
    print("Your score has been saved!\n")

    return score


def load_flashcards(filename):
    flashcards = []
    with open(filename, "r") as f: #read function = r; python opens file in read mode
        for line in f: #loops through each line
            line = line.strip() #cleans every line by removing extra spaces before and after the text
            if not line: #after cleaning every line it skips empty lines and moves on to the next so the program doesnt process blank entries
                continue 
            if "-" in line: #only processes lines that contain a -
                term, definition = line.split("-", 1) #split() function, + setting the maxsplit parameter to 1, will return a list with 2 elements. https://www.w3schools.com/python/ref_string_split.asp
            elif "," in line:
                term, definition = line.split(",", 1)
            elif ":" in line:
                term, definition = line.split(":", 1)
            else:
                print("Sorry, can't play please make a flashcard quiz that is combined by either: a dash, comma, or semicolon")
                continue #continue function skips lines that don't have a valid seperator: - , :

            #without this part the code would still run EXCEPT it wont be able to define the right answers because if user types "hydrogen" python would read it as something else even though the correct answer IS hydrogen
            term = term.strip()
            definition = definition.lower().strip() #helps clean extra space around {term} (question part) and converts definition (answer part) to lowercase and removes any spaces when user is typing out answer
            flashcards.append((term, definition)) #adding a new flashcard (a pair of values) to a list called flashcards (term, definition) is a tuple, which is basically a pair of values grouped together. This line adds a new tuple to the list. 1. I used this to learn about tuples https://www.w3schools.com/python/python_tuples.asp 2. I used this to see how to append a tuple in a list https://stackoverflow.com/questions/31175223/append-a-tuple-to-a-list-whats-the-difference-between-two-ways

    return flashcards #returns the list of flashcards


def add_scores(username, score):
    #Python records these scores in the score history file.
    with open("Score_file", "a") as f: #a = append, adds new content into the score file instead of removing it and replacing it https://www.w3schools.com/python/python_file_write.asp
        f.write(f"{username} : {score}\n") #https://www.w3schools.com/python/python_file_write.asp


def show_scores():
    #Print all saved scores from the score history file.

    print("\nScore History:")
    with open("Score_file", "r") as f:
        lines = f.readlines() #python reads score_file.txt where all previous usernames and scores are held
        if not lines: #checks if it is empty
            print("No scores to show.\n") #if there is no scores presented in score_file.txt
        else: #Basically tells python: if there are saved scores, print every score line by line, if not, say there are no scores
            for line in lines: #loops through each individual line in the list inside the txt file
                print(line) #prints each line
    print() #prints your scores all together


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
        print("Welcome amazing person! > Make sure your flashcards term and definition is seperated by one of these seperators -> dash, comma, semicolon.")
        
        while first_choice not in e_options: #while not exiting (runs because their first choice is an empty string (== ""), then because they haven't typed 'exit')
            for item in initial_choices: #print out play, see history, and exit
                print(f"- {item}")
            first_choice = input("What would you like to do?\n> ").lower().strip()
            if first_choice in p_options: #playing the game
                quiz_fn = input("Name of the file? (pls type either (you won't be able to play if you don't)): contents or periodic_table)\n> ").lower().strip()
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
                #user_score = play_quiz(file_url)
                #add_scores(user_score) #already have this function in my add scores--adding it would just create duplicate entries in the score file causing an error
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
