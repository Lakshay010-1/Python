from wonderwords import RandomWord


def display_board():
    print("<--- HANGMAN --->")
    print("Guess the word before the man is hanged!")
    print()


def get_random_word() -> str:
    return (
        RandomWord()
        .word(word_min_length=6, word_max_length=7, include_parts_of_speech=["nouns"])
        .lower()
    )


def update_guessed_word(word: str) -> list[str]:
    return ["_" for i in range(len(word))]


def display_game_state(guessed_word, guesses_left):
    print("Word to guess = ", "".join(guessed_word))
    print(f"You have {guesses_left} guesses available")


def get_guess(guessed_letters):
    invalid_input = True
    while invalid_input:
        guess = input("Guess a letter (a-z): ").lower()
        if len(guess) != 1:
            print("Enter exactly one letter")
            continue
        elif not guess.isalpha():
            print("Only alphabets are allowed")
            continue
        elif guess in guessed_letters:
            print("You already entered this alphabet.")
        else:
            invalid_input = False
            return guess


def check_game_status(guessed_word, guesses_left):
    player_won = "_" not in guessed_word
    player_lost = guesses_left == 0
    return player_won or player_lost, player_won


def play_game(MAX_GUESSES):
    game_finished = False
    word = get_random_word()
    guessed_word = update_guessed_word(word)
    guesses_left = MAX_GUESSES
    guessed_letters = set()
    display_board()

    while not game_finished:
        display_game_state(guessed_word, guesses_left)
        user_guess = get_guess(guessed_letters=guessed_letters)
        if user_guess in word:
            for idx, letter in enumerate(word):
                guessed_word[idx] = (
                    letter if user_guess == letter else guessed_word[idx]
                )
            print("Alphabet is present in the word.")
            print("You are one step closer to saving the man's life")
        else:
            guesses_left -= 1
            print("Alphabet is not present in the word.")
        guessed_letters.add(user_guess)
        print()
        game_finished, player_won = check_game_status(
            guessed_word=guessed_word, guesses_left=guesses_left
        )

        if game_finished:
            if player_won:
                print("Congratulations, You saved the man's life")
            else:
                print("Sadly, The Man is hanged.\nBetter luck next time.")
            print(f"The Word was {word}\n")


playing: bool = True
MAX_GUESSES: int = 6

try:
    while playing:
        play_game(MAX_GUESSES=MAX_GUESSES)
        playing = True if input("Play again? (y/n): ").lower() == "y" else False
        print("\n" * 5 if playing else "", end="")

except KeyboardInterrupt:
    print()
    print("Game Exited.")
