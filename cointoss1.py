import random
def coinToss(number):
    heads=0
    tails=0
    recordList = []
    for i in range(number):
        flip = random.randint(0, 1)
        if (flip == 0):
            print("Heads")
            recordList.append("Heads")
            heads+=1
            tails-=1
        else:
            print("Tails")
            recordList.append("Tails")
            heads-=1
            tails+=1
    
    print(str(recordList))
    print('Number of heads \t Number of tails')
    print(str(recordList.count("Heads")) ,'\t\t\t', str(recordList.count("Tails")))
    print('Points obtained by ')
    print('First player :',heads)
    print('Second player :',tails)
    if heads>tails:
        print("First player wins the game")
    else:
        print("Second Player wins the game")
    if heads==tails:
        print("There is a tie")
        
number = int(input("How many times you want to flip the coin: "))
coinToss(number)

