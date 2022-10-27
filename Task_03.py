board = list(range(1,10))

def print_board(board):
    print('-------------')
    for i in range(3):
        print('|', board[0+i*3], '|', board[1+i*3], '|', board[2+i*3], '|')
        print('-------------')

def take_input(sign):
    valid = False
    while not valid:
        player_move = input('Делает ход игрок ' + sign + ': ')
        try:
            player_move = int(player_move)
        except:
            print('Некорректный ввод')
            continue
        if player_move >= 1 and player_move <= 9:
            if (str(board[player_move-1]) not in "XO"):
                board[player_move-1] = sign
                valid = True
            else:
                print('Эта клетка занята')
        else:
            print('Некорректный ввод')


def check_win(board):
    win_kort = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for i in win_kort:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return board[i[0]]
    return False

count = 0
win = False
while not win:
    print_board(board)
    if count % 2 == 0:
        take_input("X")
    else:
        take_input("O")
    count += 1
    if count > 4:
        tmp = check_win(board)
        if tmp:
            print(tmp, 'Поздравляем, вы выиграли!')
            win = True
            break
    if count == 9:
        print('Ничья!')
        break
print_board(board)