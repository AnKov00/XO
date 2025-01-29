import sys
board = [] #Переменная содержащая игровое поле
a,b = None,None # Две переменных каординат
x = "X"
o = "O"
Win_X = 0       #Щетчик побед
Win_O = 0
No_win = 0
def start():
    """Функция форматирующая игровое поле"""
    game = (input("Введите start, чтобы началть игру: "))
    if game != 'start':#Для начала, либо пркекращения игры
        print('Игра окончена')
        print(f"Игорк Х победил {Win_X} раз, игок О {Win_O} раз, {No_win} сыграно в ничью")
        sys.exit()
        return
    global board
    board = [["." for j in range(4) ] for i in range(4)] #Доска - это матрица 3х3. Используем генератор списков.
    board[0][0], board [0][1], board [0][2], board [0][3]= "*", 'A', 'B', 'C'# Для эстетики меняю верхние цифры на буквы.
    board[1][0], board[2][0], board[3][0]= 1,2,3
    print(board[0][0], board[0][1], board[0][2], board[0][3])
    print(board[1][0], '\n', board[2][0], '\n', board[3][0], sep="")
    step_X()
    return

def step_X ():
   '''Функция принимает 2 координаты, проверяет корректность и вносит на поле'''
   global board #Объявление переменной "поле" глобальной для внесения ХО
   a,b = input("Введите координату точки Х по горизонтали: ").lower(), input("Введите координату точки X по вертикали: ")
   if a == 'a':# Проверка координаты j и присвоение численного значения
       a = 1
   elif a == 'b':
       a = 2
   elif a =='c':
       a = 3
   else: print("Введена неправильная координата по горизонтали"), step_X()

   if b not in ['1', '2', '3']:#Проверка координаты по вертикали
       print("Введена неправильная координата по вертикали"), step_X()
   b = int(b)
   if board[b][a]=='.':#Прверка координат и внесение на поле
       board[b][a] = x
       print(*board, sep='\n')
       win_check()
       step_O()#Переход хода
       return
   else:print("Ячейка занята, выберите другую ячейку"), step_X()
   return

def step_O():
    '''Функция принимает 2 координаты, проверяет корректность и вносит на поле'''
    global board  # Объявление переменной "поле" глобальной для внесения ХО
    a, b = input("Введите координату точки O по горизонтали: ").lower(), input("Введите координату точки O по вертикали: ")
    if a == 'a':  # Проверка координаты j и присвоение численного значения
        a = 1
    elif a == 'b':
        a = 2
    elif a == 'c':
        a = 3
    else:
        print("Введена неправильная координата по горизонтали"), step_O()

    if b not in ['1', '2', '3']:  # Проверка координаты по вертикали
        print("Введена неправильная координата по вертикали"), step_O()
    b = int(b)

    if board[b][a] == '.':  # Прверка координат и внесение на поле
        board[b][a] = o
        print(*board, sep='\n')
        win_check()
        step_X() #Переход хода Х
        return
    else:
        print("Ячейка занята, выберите другую ячейку"), step_O()
    return

def win_check():
    board_1 = board[1]
    board_2 = board[2]
    board_3 = board[3]
    board_4 = [board[1][1],board[2][1], board[3][1]]
    board_5 = [board[1][2],board[2][2], board[3][2]]
    board_6 = [board[1][3],board[2][3], board[3][3]]
    board_7 = [board[1][1],board[2][2], board[3][3]]
    board_8 = [board[1][3],board[2][2], board[3][1]]
    def win_chek_len(len_x):
        count_X = 0
        count_O = 0
        for i in len_x:

            if i == 'X':
                count_X += 1
            if i == 'O':
                count_O += 1
        if count_X == 3:
            print("Победил Х")
            global Win_X
            Win_X +=1
            start()
        if count_O == 3:
            print("Победил О")
            global Win_O
            Win_O += 1
            start()
        else:return
    win_chek_len(board_1)
    win_chek_len(board_2)
    win_chek_len(board_3)
    win_chek_len(board_4)
    win_chek_len(board_5)
    win_chek_len(board_6)
    win_chek_len(board_7)
    win_chek_len(board_8)
    count_point = 0 #Счетчик свободных ячеек
    for j in board:
        for i in  j:
            if i == '.':
                count_point+=1
    if count_point == 0:
        global No_win
        No_win+=1
        print("Ничья")
        start()
    return

start()