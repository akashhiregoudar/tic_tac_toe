import random
from os import system
mylist=['#',1,2,3,4,5,6,7,8,9]
player1=input("Enter name of player 1: ")
player2=input("Enter name of player 2: ")


def display_board() :
    system('cls')
    print("\t\t\t\tWelcome to XOX game")
    print(f'\t\t\t\t|{mylist[7]}|{mylist[8]}|{mylist[9]}|')
    print("\t\t\t\t|-|-|-|")
    print(f'\t\t\t\t|{mylist[4]}|{mylist[5]}|{mylist[6]}|')
    print("\t\t\t\t|-|-|-|")
    print(f'\t\t\t\t|{mylist[1]}|{mylist[2]}|{mylist[3]}|')


def set_mark(player1,player2) :
    choice=random.randint(0,1)
    #player2_marker=''
    if choice==1 :
        player1_marker=input(player1+" Choose ur marker X or O: ")
        if player1_marker.upper()=='X' :
            player2_marker='O'
        else :
            player2_marker='X'
    else :
        player2_marker=input(player2+" Choose ur marker X or O: ")
        if player2_marker.upper()=='X' :
            player1_marker='O'
        else :
            player1_marker='X'
    return player1_marker,player2_marker


def insert_marker(player1_marker,player2_marker,player1,player2) :
    if win_check(mylist,'X',player1,player2) or win_check(mylist,'O',player1,player2) :
        print("Game Over!!!")
    else :
        player1_position=int(input(player1+" enter ur position: "))
        mylist[player1_position]=player1_marker
        display_board()
    if win_check(mylist,'X',player1,player2) or win_check(mylist,'O',player1,player2) :
        print("Game Over!!!")
    else :
        player2_position=int(input(player2+" enter ur position: "))
        mylist[player2_position]=player2_marker
        display_board()

def win_check(mylist, mark,player1,player2):
    if (mylist[1]==mylist[2]==mylist[3]==mark) or (mylist[4]==mylist[5]==mylist[6]==mark) or (mylist[7]==mylist[8]==mylist[9]==mark) :
        if mark==player1_marker :
            print("Congratulations!! "+player1+ " has WON")
        else:
            print("Congratulations!! "+player2+ " has WON")
        return True
    elif (mylist[7]==mylist[4]==mylist[1]==mark) or (mylist[8]==mylist[5]==mylist[2]==mark) or (mylist[9]==mylist[6]==mylist[3]==mark) :
        if mark==player1_marker :
            print("Congratulations!! "+player1+ " has WON")
        else:
            print("Congratulations!! "+player2+ " has WON")
        return True
    elif (mylist[7]==mylist[5]==mylist[3]==mark) or (mylist[9]==mylist[5]==mylist[1]==mark) :
        if mark==player1_marker :
            print("Congratulations!! "+player1+ " has WON")
        else:
            print("Congratulations!! "+player2+ " has WON")
        return True
    else :
        if c==10:
            print("Matched Tied!!!!!!")
while True :
    c=1
    player1_marker,player2_marker=set_mark(player1,player2)
    while c<=5:
        display_board()
        insert_marker(player1_marker,player2_marker,player1,player2)
        c+=1
    play_again=input("Do you want to play again? Yes or No: ")
    if play_again.lower()=='yes':
        c=1
        mylist=['#',1,2,3,4,5,6,7,8,9]
        continue
    else:
        break

    

