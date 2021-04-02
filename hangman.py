print("Welcome to HANGMAN.")

def game_play():

    # pick a random word from sowpods text file
    import random
    def pick_word():
        fh = open("hangman-sowpods.txt")
        return random.choice(list(fh)).rstrip()
    picked_word = pick_word()

    # initialise variables
    attempts = 6
    guessed_letters = []
    
    # ask user to guess character
    def ask_char():
        print("Attempts left:", attempts)
        return input("Guess your letter: ").upper()

    # function for finding the position of a character in a string
    def find_pos(str, ch):
        return [i for i, ltr in enumerate(str) if ltr == ch]

    current_formation = list("—" * len(picked_word))    # current status of word, insert input chars if true
    print((" ").join(current_formation))

    while "—" in current_formation or attempts >= 0:
        if attempts == 0:
            print("You ran out of attempts.")
            print("The correct word was", picked_word)
            break
        elif "—" not in current_formation:
            print("You guessed the word correctly!")
            break
        else:
            input_char = ask_char()
            if input_char in guessed_letters:
                print("Letter already guessed. Try again!")

            elif input_char in picked_word:
                guessed_letters.append(input_char)
                for pos in find_pos(picked_word, input_char):
                    current_formation[pos] = input_char
                print((" ").join(current_formation))

            elif input_char not in guessed_letters and picked_word:
                guessed_letters.append(input_char)
                attempts -= 1
                print("Wrong!", end=" ")
    response = input("Do you want to play another game (Y/N): ").upper()
    if response == "Y":
        game_play()
    if response == "N":
        print("Thank you for playing hangman.")

game_play()