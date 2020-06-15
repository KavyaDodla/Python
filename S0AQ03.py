import random
def get_names():
    players=input("Please enter the name of 10 players seperated by spaces->")
    players_list=players.split()
    print(players_list)
    return players_list
def cards():
    card_list=[]
    count=0
    while count<10:
        x=random.randint(300,325)
        if x not in card_list:
            count=count+1
            card_list.append(x)
        else:
            count=count
    print(card_list)
    return card_list

def winner(players_list,card_list):
    count=1
    x=0
    for i in card_list:
        count=count+1
        if i>x:
            x=i
    print("Highest number in card is:",x)
    index=card_list.index(x)
    print("The winner of the game is->",players_list[index])

def main():
    players_list=get_names()
    card_list=cards()
    winner(players_list,card_list)
main()
