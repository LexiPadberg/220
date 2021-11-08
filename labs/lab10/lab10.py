"""
Name: <Lexi Padberg>
<Lab10>.py
"""


def build_board():
    tic_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return tic_list


def board_display(tic_list):
    print("-" * 10)
    counter = 0
    for i in range(3):
        print("|", end="")
        for j in range(3):
            print(tic_list[counter], end="|")
            counter += 1
        print()
        print("-" * 10)


def place_spot(tic_list, spot, marker):
    tic_list[spot-1] = marker


def legal_spot(tic_list, spot, marker):
    if (tic_list[spot-1] == "x" or tic_list[spot-1] == "o") \
            or (spot < 1 or spot > 9):
        return False
    else:
        return True


def win_game(tic_list):
    winner = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for condition in winner:
        counter = 0
        for spot in condition:
            if tic_list[spot - 1] == "x":
                counter += 1
        if counter == 3:
            return "x wins"

        counter = 0
        for spot in condition:
            if tic_list[spot - 1] == "o":
                counter += 1
        if counter == 3:
            return "o wins"



def game_over(tic_list, turnCount):
    if (win_game(tic_list) == "x wins" or win_game(tic_list) == "o wins") or (turnCount > 9):
        return True
    else:
        return False


def play_game(tic_list):
    turnCount = 1
    board_display(tic_list)
    while not(game_over(tic_list, turnCount)):
        x_turn = eval(input("enter which spot to put an x:"))
        if legal_spot(tic_list, x_turn, "x"):
            place_spot(tic_list, x_turn, "x")
        board_display(tic_list)
        if win_game(tic_list) == "x wins":
            print("x wins")
            break

        o_turn = eval(input("enter  which spot to put an o:"))
        if legal_spot(tic_list, o_turn, "o"):
            place_spot(tic_list, o_turn, "o")
        board_display(tic_list)
        if win_game(tic_list) == "o wins":
            print("o wins")
            break
        turnCount += 1
    if turnCount == 9:
        print("tie game")




def main():
    tic_list = build_board()
    play_game(tic_list)
    pass


main()
