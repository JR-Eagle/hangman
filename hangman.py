import os

def hangman(word):
    wrong = 0
    stages = ["",
              "  ________________              ",
              "  |              |              ",
              "  |              O              ",
              "  |             \|/             ",
              "  |              |              ",
              "  |             / \             ",
              "  |                             ",
              "__|______________________________"
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman!")

    while wrong < len(stages):
        ip = input("Please enter one character:")
        if ip in rletters:
            id = rletters.index(ip)
            board[id] = ip
            rletters[id] = "$"
            print(" ".join(board))
        else:
            wrong += 1
            e = wrong
            print("You guess incorrectly for {} time".format(e))
            print("You have {} chance reamined".format(len(stages) - e))
            print("\n".join(stages[0:e]))
            print("\n")

        if "_" not in board:
            print("Player2 winned!")
            print("".join(board))
            win = True
            break
    if not win:
        print("Player1 completed the picture and winned!")
        print("The right answer is [{}].".format(word))
            

hangman("Welcome")
    
    
