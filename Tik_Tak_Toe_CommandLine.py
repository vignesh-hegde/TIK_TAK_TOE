# TIK TAK TOE
from os import system

marks = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

isEmpty = lambda: " " in marks[0] or " " in marks[1] or " " in marks[2]


def win(current_mark, current_player):
    if not isEmpty():
        print("Draw")
        return True
    
    dia_1 = [marks[0][0], marks[1][1], marks[2][2]]
    dia_2 = [marks[0][-1], marks[1][-2], marks[2][-3]]
    if dia_1.count(current_mark) == 3 or dia_2.count(current_mark) == 3:
        print(f"{current_player} Won")
        return True

    for _ in range(3):
        if marks[_][0] == marks[_][1] == marks[_][2] == current_mark:
            print(f"{current_player} Won")
            return True
        if marks[0][_] == marks[1][_] == marks[2][_] == current_mark:
            print(f"{current_player} Won")
            return True

    return False


def draw_board():
    system("cls")
    print(f" {marks[0][0]}", "|", f"{marks[0][1]}", "|", f"{marks[0][2]}")
    print("-----------")
    print(f" {marks[1][0]}", "|", f"{marks[1][1]}", "|", f"{marks[1][2]}")
    print("-----------")
    print(f" {marks[2][0]}", "|", f"{marks[2][1]}", "|", f"{marks[2][2]}")


if __name__ == "__main__":
    player1_name = input("Enter Player 1 Name : ")

    flag = True
    while flag:
        player1_mark = input("Enter X or O : ").upper()
        flag = not (player1_mark in ["X", "O"])

    player2_name = input("Enter Player 2 Name : ")
    current_player = {True: [player1_mark, player1_name], False: ["X" if player1_mark == "O" else "O", player2_name]}

    flag = False

    while not win(current_player[flag][0], current_player[flag][1]):
        flag = not flag
        while True:
            x, y = list(map(int, input(f"{current_player[flag][1]} >> ").split()))
            if x < 3 and y < 3:
                if marks[x][y] == " ":
                    break
            print("Try again ! ")
        marks[x][y] = current_player[flag][0]
        draw_board()

    input()
