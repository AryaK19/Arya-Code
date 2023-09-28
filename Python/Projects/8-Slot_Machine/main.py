import random as rn

def slot_r():
    slot = open('Slot.txt','r')
    s_data = slot.read()
    slot.close()
    return s_data

def slot_w(write):
    slot = open('Slot.txt','w')
    slot.write(write)
    slot.close()

def bank_r():
    bank = open('Bank.txt','r')
    b_data = bank.read()
    bank.close()
    return b_data

def bank_w(write):
    bank = open('Bank.txt','w')
    bank.write(write)
    bank.close()





def bet_f(bet):

    s_data = slot_r()
    print(f"Balance : ${s_data}")
    
    if bet == "quit":
        quit = True
    
    
    if int(bet) <= int(s_data):
        s_data = slot_r()
        slot_w(str(int(s_data) - int(bet)))

        slot_1 = rn.choice(["@","#","$"])
        slot_2 = rn.choice(["@","#","$"])
        slot_3 = rn.choice(["@","#","$"])

        print("\n")
        print("-------------------")
        print(f"|  {slot_1}  |  {slot_2}  |  {slot_3}  |")
        print("-------------------")
        print("\n")

        if slot_1 == slot_2 == slot_3:
            won = True
           
            print("You Won!")
            print("\n")
        
        else:
            won = False
            print("You Lost!")
            print(f"- {bet}")
            print("\n")
            s_data = slot_r()
            print(f'Balance : {s_data}')

    else :
        print("You don't have enough Money...")
        print("Try Again...")
        bet()
    
    return won

def deposit():
    bank = open('Bank.txt')
    b_data = bank.read()
    print(f"Bank Balance : ${b_data}")

    amount_d = input("Amount To Be Deposited ($) : ")

    if int(b_data) >= int(amount_d):
        slot = open('Slot.txt')
        s_data = slot.read()
        
        bank = open('Bank.txt','w')
        slot = open('Slot.txt','w')
        
        slot.write(str(int(s_data) + int(amount_d)))
        bank.write(str(int(b_data) - int(amount_d)))

        slot.close()
        bank.close()

    else:
        print("You don't have enough Money...")
        print("Try Again...")
        deposit()

def withdraw():
    s_data = slot_r()
    print(f"Balance : ${s_data}")
    amount_w = input('Enter Amount : ')

    if int(s_data) >= int(amount_w):
        b_data = bank_r()
        
        slot_w(str(int(s_data) - int(amount_w)))
        bank_w(str(int(b_data) + int(amount_w)))
    else:
        print("You don't have enough Money...")
        print("Try Again...")
        withdraw()
        

def win_a(bet):
    win = int(bet) * 3
    print(f'+{win}')
    s_data = slot_r()
    slot_w(str(int(win) + int(s_data)))
    
    s_data = slot_r()
    print(f'Balance : {s_data}')
    

def main():
   
    quit = False
    while not quit:
        won = False
        print("\n")
        print("bet/bal/dep/wit/bank/quit")
        command = input("Command : ")
        if command == "bet":
            bet = input("Your Bet : ")
            won = bet_f(bet)
            if won:
                win_a(bet)

        elif command == "dep":
            deposit()
        elif command == "wit":
            withdraw()
        elif command == "bal":
            print(f"Balance : ${slot_r()}")
        elif command == "bank":
            print(f"Bank Balance : ${bank_r()}")
        elif command == "quit":
            quit = True


    

if __name__=="__main__":
    main()