# Added bold text, formatting code that I searched
# Also found about the fact that I need to an an "f" before the string to format this properly.
bold_text = "\033[1m"
reset_text = "\033[0m"

# Define my function to output a sentence based on a keyword from user
def prompt_sentence(keyword):
    # Multiple elif functions due to different possible toggles
    if keyword.lower() == "name":
        print()
        print(f"{bold_text}My name is Sam Rosales.{reset_text}")
        print()
    elif keyword.lower() == "pronouns":
        print()
        print(f"{bold_text}My pronouns are he/him.{reset_text}")
        print()
    elif keyword.lower() == "movie":
        print()
        print(f"{bold_text}My favorite movie is Star Wars: Episode VI - Return of the Jedi.{reset_text}")
        print()
    elif keyword.lower() == "food":
        print()
        print(f"{bold_text}My favorite food is Macaroni and Cheese.{reset_text}")
        print()
    # else function so that there's a buffer if the user doesn't input one of the words
    else:
        print()
        print(f"{bold_text}I don't have a specific sentence for that keyword.{reset_text}")
        print()

# Main program heading
if __name__ == "__main__":
    print()
    print(f"\033[4mHello! Would you like to know my name, my pronouns, my favorite movie, or my favorite food?\033[0m")
    print()
    
    # while function that shows after each user interaction, 
    # as to keep asking the questions rather than exiting
    while True:
        keyword = input("Enter 'name', 'pronouns', 'food', or 'movie' to learn more, or type 'exit' to exit the code: ")
        
        # However, if user is done, exit command to exit code
        if keyword.lower() == 'exit':
            print()
            print(f"{bold_text}Thanks for your time! Excited to learn more in this class.{reset_text}")
            print()
            break  # Exit the loop if the user enters 'exit'
       
        # This function is the backbone of the program.
        # It will continue to prompt the input command
        # along with connecting keywords that are typed by user 
        # to their corresponding response, until the user types 'exit'. 
        # Without it, the program will only accept 'exit' for it to do anything.
        prompt_sentence(keyword)