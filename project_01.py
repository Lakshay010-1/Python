import random

# Rock, Paper, Scissors, Lizard, Spock Game
# 0 = Rock, Defeats = Scissors, Lizard
# 1 = Paper, Defeats = Rock, Spock
# 2 = Scissors, Defeats = Paper, Lizard
# 3 = Lizard, Defeats = Spock, Paper
# 4 = Spock, Defeats = Scissors, Rock
moves = {0: "Rock", 1: "Paper", 2: "Scissors", 3: "Lizard", 4: "Spock"}
winning_rules = [[2, 3], [0, 4], [3, 1], [1, 4], [0, 2]]


def show_rules():
    print("Valid Moves : ")
    for move in moves:
        print(f"{move} -> {moves.get(move)}")
    print()


def get_user_move():
    is_valid_move = False
    user_move = ""
    while not is_valid_move:
        user_move = input("Play your move : ")
        is_valid_move = user_move.isnumeric() and int(user_move) in moves
        if not is_valid_move:
            print("Play valid move.")
            show_rules()
    return int(user_move)


def show_result(user_move, computer_move):
    user_result = computer_move in winning_rules[user_move]
    message = ""
    if user_move == computer_move:
        message = f"Match DRAW, You and Computer both chooses {moves.get(user_move)}"
    elif user_result:
        message = f"You WIN, {moves.get(user_move)} DEFEATS {moves.get(computer_move)}."
    else:
        message = (
            f"Computer WIN, {moves.get(computer_move)} DEFEATS {moves.get(user_move)}."
        )
    print(message)


def main():
    try:
        print("Rock, Paper, Scissors, Lizard and Spock")
        show_rules()

        playing = True

        while playing:
            computer_move = random.randint(0, len(moves) - 1)
            user_move = get_user_move()

            print()
            print(f"Your move -> {moves.get(user_move)}")
            print(f"Computer move -> {moves.get(computer_move)}")
            print()

            show_result(user_move=user_move, computer_move=computer_move)
            print("\n" * 2)

            playing = (
                True if input("Continue playing (y/n)? : ").lower() == "y" else False
            )

    except KeyboardInterrupt:
        print()
        print("Game Interrupted.")


if __name__ == "__main__":
    main()
