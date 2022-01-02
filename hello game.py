def hangman(word): # создаём функцию которая принимает слово для угадывания
    wrong = 0
    stages = [" ", # создаём список из строк чтобы постепенно выресовывать
            "----------— ",
            "|      |      ",
            "|      |      ",
            "|      0      ",
            "|    / | \    ",
            "|     / \     ",
            "| "
             ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Добро пожаловать")
    while wrong < len(stages): # создаём цикл игры
        print("\n")
        msg = "введите букву"
        char = input(msg)
        if char in rletters: # если вы угадали
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else: # если вы не угадали
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "__" not in board: # если не осталось букв
            print("вы выйграли")
            print(" ".join(board))
            win = True
            break
    if not win: #если вы не выйграли
       print("\n".join(stages[0: wrong]))
       print("вы выйграли, было загадоно слово: ",word)
hangman("кот")

