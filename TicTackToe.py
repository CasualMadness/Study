board = list(range(1,10))
pole = 3
win_lines = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
def show_board():
    print("_" * 4 * pole )
    for i in range(pole):
        print((" " * 3 + "|")* 3)
        print("" , board[i * 3], '|', board[1+ i * 3], "|", board[2+ i * 3], "|")
        print(("_" * 3 + "|") * 3)


def movement(player):
    while True:
        move = input("Где поставить " + player + " ?")
        if not (move in "123456789") or move == "":
            print("Ошибка ввода,введите чило от 1-9")
            continue
        move = int(move)
        if str(board[move - 1]) in "XO":
            print("Клетка уже занята :(")
            continue
        board[move - 1] = player
        break


def win_statement():
    for i in win_lines:
        if (board[i[0] - 1]) == (board[i[1] - 1]) == (board[i[2] - 1]):
            return board[i[1] - 1]
    else:
        return False


def game():
    count = 0
    while True:
        show_board()
        if count % 2 == 0:
            movement("X")
        else:
            movement("O")
        if count > 3:
            winner = win_statement()
            if winner:
                show_board()
                print("Победили " + winner + "!!!")
                break
        count += 1
        if count > 8:
            show_board()
            print("НИЧЬЯ!!!")
            break
print(" Добро пожаловать в Крестики-нолики!!!!")
print("Ходы выполняются по таблице,которую вы видите от 1 до 9")
game()