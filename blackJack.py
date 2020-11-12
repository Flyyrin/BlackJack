#Player can set the bet of chips,
# Closest to 21 wins
# You can choose to wait or get a card
# Over 21 means you lose
#If you wait, the dealer reveals and picks a new card
#keep track of money

import random



SC = [1,11]
S = random.choice(SC)
cards = [2,3,4,5,6,7,9,10,10,10,10,S]
#print("You got ", random.choice(cards))

#keep track of chips
chips_data = open("F:\python\projects\\blackjack\chips.txt", "r")
chips = chips_data.read()
chips_data.close     

#chips_data_write = open("F:\python\projects\\blackjack\chips.txt", "w")
#chips_data_write.write(chips)
#chips_data_write.close

#Pick cards
'''
player_cards = random.choice(cards)+random.choice(cards)
bot_visable_card = random.choice(cards)
bot_cards = random.choice(cards)+bot_visable_card
if player_cards > 20:
    cards_limet = [2,3,4,5,6,7,9,10,10,10,10,1]
    player_cards = random.choice(cards)+random.choice(cards_limet)
else:
'''    




def choose():
    print(" ")
    print("---------------------------")
    print("Your chips: "+str(chips))
    print("---------------------------")
    print("Enter:   ")
    print("P to play.")
    print("S to visit the chip store.")
    choise = input("     ")
    if choise is "P" or choise is "S":
        if choise == "P":
            print(set_bet())  
        else:
            print(visit_store())
    else:
        print("Follow the instructions.")            


def visit_store():
    chips_data2 = open("F:\python\projects\\blackjack\chips.txt", "r")
    chips = chips_data2.read()
    chips_data2.close
    print(" ")     
    print("---------------------------")
    print("------------STORE----------")
    print("---------------------------")
    print("Your chips: "+ str(chips))
    print("---------------------------")
    print("")
    print("Howmany chips would you like to buy?")
    credit = input("Enter amount: ")
    if credit.isnumeric():
        chips_data2_write = open("F:\python\projects\\blackjack\chips.txt", "w")
        new_credit = int(chips) + int(credit)
        chips_data2_write.write(str(new_credit))
        chips_data2_write.close 
        print(" ")
        print("You bought "+ str(credit)+" chips.")
        return("Total chips: "+str(int(chips)+int(credit)))
            

#Player can set the bet of chips,
def set_bet():
    chips_data = open("F:\python\projects\\blackjack\chips.txt", "r")
    chips = chips_data.read()
    chips_data.close
    print(" ")     
    print("Set a bet:")
    print("10.")
    print("50.")
    print("100.")
    print("1000.")
    print("2000.")
    print("Your chips: " + chips)
    bet_in = input("Bet:  ")
    bet = 0
    def start_game():
        chips_data_write = open("F:\python\projects\\blackjack\chips.txt", "w")
        left = int(chips) - int(bet)
        chips_data_write.write(str(left))
        chips_data_write.close
        print(" ")
        print("---------------------------")
        print("------------START----------")
        print("---------------------------")
        print("Your chips: "+ str(left))
        print("---------------------------")
        print("Your bet: "+ bet)
        print(" ")
        print(" ")
        print("Your cards: "+ str(pc1) +" and " + str(pc2)+"  Total: "+ str(pc1+pc2) )
        print(" ")
        print("Oponent cards: "+ str(bot_card1) +" and [HIDDEN]   Total: "+ str(bot_card1)+" + [HIDDEN]" )
        #Hit or take?
        print(" ")
        choise = input("Enter Hit or Take:   ")
        if choise is "H" or choise is "T":
            if choise == "H":
                #hit  
                pc3 = random.choice(cards)
                bot_card3 = random.choice(cards)
                print(" ")
                print("---------------------------")
                print("-------------HIT-----------")
                print("---------------------------")
                print("Your chips: "+ str(left))
                print("---------------------------")
                print("Your bet: "+ bet)
                print(" ")
                print(" ")
                print("Your cards: "+ str(pc1) +" and " + str(pc2)+" and "+ str(pc3)+"   Total: "+ str(pc1+pc2+pc3) )
                print(" ")
                print("Oponent cards: "+ str(bot_card1) +" and "+ str(bot_card2)+" and " + str(bot_card3)+  "   Total: "+ str(bot_card1+bot_card2+bot_card3) )
                if pc1+pc2+pc3 != bot_card1+bot_card2+bot_card3:
                    player_till_21 = (pc1+pc2+pc3)-21
                    bot_till_21 = (bot_card1+bot_card2+bot_card3)-21
                    player_till_21C = abs(player_till_21)
                    bot_till_21C = abs(bot_till_21)
                    if bot_till_21 > player_till_21:
                        bot_win = True
                    else:    
                        bot_win = False
                else:
                    chips_data3_write = open("F:\python\projects\\blackjack\chips.txt", "w")
                    new_credits = int(chips) + int(bet)
                    chips_data3_write.write(str(new_credits))
                    chips_data3_write.close     
                    print(" ")
                    print("-------------TIE------------")
                    print("You keep your bet of "+str(bet)+" chips")
                    print("Your chips: "+ str(left))
                    print("New chips total: "+ str(int(left)+int(bet)))
                    print("---------------------------")
                    print(" ")
                    print(" ")
                    print("Your cards: "+ str(pc1) +" and " + str(pc2)+" and "+ str(pc3)+"   Total: "+ str(pc1+pc2+pc3) )
                    print(" ")
                    return("Oponent cards: "+ str(bot_card1) +" and "+ str(bot_card2)+" and " + str(bot_card3)+  "   Total: "+ str(bot_card1+bot_card2+bot_card3) )
                if bot_card1+bot_card2+bot_card3 > 21 and pc1+pc2+pc3 > 21:
                    chips_data5_write = open("F:\python\projects\\blackjack\chips.txt", "w")
                    new_creditsT = int(chips) + int(bet)
                    chips_data5_write.write(str(new_creditsT))
                    chips_data5_write.close     
                    print(" ")
                    print("-------------TIE------------")
                    print("You keep your bet of "+str(bet)+" chips")
                    print("Your chips: "+ str(left))
                    print("New chips total: "+ str(int(left)+int(bet)))
                    print("---------------------------")
                    print("Both of you where above 21. ")
                    print(" ")
                    print("Your cards: "+ str(pc1) +" and " + str(pc2)+" and "+ str(pc3)+"   Total: "+ str(pc1+pc2+pc3) )
                    print(" ")
                    return("Oponent cards: "+ str(bot_card1) +" and "+ str(bot_card2)+" and " + str(bot_card3)+  "   Total: "+ str(bot_card1+bot_card2+bot_card3) )
                else:
                    if bot_card1+bot_card2+bot_card3 > 21:
                        bot_win = False
                    else:
                        bot_win = True    
                    if pc1+pc2+pc3 > 21:
                        bot_win = True
                    else:
                        bot_win = False        

                    if bot_win == True:
                        print(" ")
                        print("-------------LOSE-----------")
                        print("You lost your bet of "+str(bet)+" chips")
                        print("Your chips: "+ str(left))
                        print("New chips total: "+ str(int(left)-int(bet)))
                        print("---------------------------")
                        print(" ")
                        print(" ")
                        print("Your cards: "+ str(pc1) +" and " + str(pc2)+" and "+ str(pc3)+"   Total: "+ str(pc1+pc2+pc3) )
                        print(" ")
                        return("Oponent cards: "+ str(bot_card1) +" and "+ str(bot_card2)+" and " + str(bot_card3)+  "   Total: "+ str(bot_card1+bot_card2+bot_card3) )
                    else:
                        chips_data4_write = open("F:\python\projects\\blackjack\chips.txt", "w")
                        new_creditsW = int(chips) + int(bet)#*2
                        chips_data4_write.write(str(new_creditsW))
                        chips_data4_write.close     
                        print(" ")
                        print("-------------WIN------------")
                        print("You doubled your bet of "+str(bet)+" chips")
                        print("Your chips: "+ str(left)+" + " +str(int(bet)*2))
                        print("New chips total: "+ str(int(left)+(int(bet)*2)))
                        print("---------------------------")
                        print("You won "+ str(int(bet)*2)+" chips." )
                        print(" ")
                        print(" ")
                        print("Your cards: "+ str(pc1) +" and " + str(pc2)+" and "+ str(pc3)+"   Total: "+ str(pc1+pc2+pc3) )
                        print(" ")
                        return("Oponent cards: "+ str(bot_card1) +" and "+ str(bot_card2)+" and " + str(bot_card3)+  "   Total: "+ str(bot_card1+bot_card2+bot_card3) )

                

                

            else:
                #take
                bot_card3 = random.choice(cards)
                print(" ")
                print("---------------------------")
                print("-------------Take----------")
                print("---------------------------")
                print("Your chips: "+ str(left))
                print("---------------------------")
                print("Your bet: "+ bet)
                print(" ")
                print(" ")
                print("Your cards: "+ str(pc1) +" and " + str(pc2)+"   Total: "+ str(pc1+pc2) )
                print(" ")
                print("Oponent cards: "+ str(bot_card1) +" and "+ str(bot_card2)+" and " + str(bot_card3)+  "   Total: "+ str(bot_card1+bot_card2+bot_card3) )
                if pc1+pc2 != bot_card1+bot_card2+bot_card3:
                    player_till_21 = (pc1+pc2)-21
                    bot_till_21 = (bot_card1+bot_card2+bot_card3)-21
                    player_till_21C = abs(player_till_21)
                    bot_till_21C = abs(bot_till_21)
                    if bot_till_21 < player_till_21:
                        bot_win = True
                    else:    
                        bot_win = False
                else:
                    chips_data3_write = open("F:\python\projects\\blackjack\chips.txt", "w")
                    new_credits = int(chips) + int(bet)
                    chips_data3_write.write(str(new_credits))
                    chips_data3_write.close     
                    print(" ")
                    print("-------------TIE------------")
                    print("You keep your bet of "+str(bet)+" chips")
                    print("Your chips: "+ str(left))
                    print("New chips total: "+ str(int(left)+int(bet)))
                    print("---------------------------")
                    print(" ")
                    print(" ")
                    print("Your cards: "+ str(pc1) +" and " + str(pc2)+"   Total: "+ str(pc1+pc2) )
                    print(" ")
                    return("Oponent cards: "+ str(bot_card1) +" and "+ str(bot_card2)+" and " + str(bot_card3)+  "   Total: "+ str(bot_card1+bot_card2+bot_card3) )
                if bot_card1+bot_card2+bot_card3 > 21 and pc1+pc2 > 21:
                    chips_data5_write = open("F:\python\projects\\blackjack\chips.txt", "w")
                    new_creditsT = int(chips) + int(bet)
                    chips_data5_write.write(str(new_creditsT))
                    chips_data5_write.close     
                    print(" ")
                    print("-------------TIE------------")
                    print("You keep your bet of "+str(bet)+" chips")
                    print("Your chips: "+ str(left))
                    print("New chips total: "+ str(int(left)+int(bet)))
                    print("---------------------------")
                    print("Both of you where above 21. ")
                    print(" ")
                    print("Your cards: "+ str(pc1) +" and " + str(pc2)+"   Total: "+ str(pc1+pc2) )
                    print(" ")
                    return("Oponent cards: "+ str(bot_card1) +" and "+ str(bot_card2)+" and " + str(bot_card3)+  "   Total: "+ str(bot_card1+bot_card2+bot_card3) )
                else:
                    if bot_card1+bot_card2+bot_card3 > 21:
                        bot_win = False
                    else:
                        bot_win = True    
                    if pc1+pc2 > 21:
                        bot_win = True
                    else:
                        bot_win = False        

                    if bot_win == True:
                        print(" ")
                        print("-------------LOSE-----------")
                        print("You lost your bet of "+str(bet)+" chips")
                        print("Your chips: "+ str(left))
                        print("New chips total: "+ str(int(left)-int(bet)))
                        print("---------------------------")
                        print(" ")
                        print(" ")
                        print("Your cards: "+ str(pc1) +" and " + str(pc2)+"   Total: "+ str(pc1+pc2) )
                        print(" ")
                        return("Oponent cards: "+ str(bot_card1) +" and "+ str(bot_card2)+" and " + str(bot_card3)+  "   Total: "+ str(bot_card1+bot_card2+bot_card3) )
                    else:
                        chips_data4_write = open("F:\python\projects\\blackjack\chips.txt", "w")
                        new_creditsW = int(chips) + int(bet)#*2
                        chips_data4_write.write(str(new_creditsW))
                        chips_data4_write.close     
                        print(" ")
                        print("-------------WIN------------")
                        print("You doubled your bet of "+str(bet)+" chips")
                        print("Your chips: "+ str(left)+" + " +str(int(bet)*2))
                        print("New chips total: "+ str(int(left)+(int(bet)*2)))
                        print("---------------------------")
                        print("You won "+ str(int(bet)*2)+" chips." )
                        print(" ")
                        print(" ")
                        print("Your cards: "+ str(pc1) +" and " + str(pc2)+"   Total: "+ str(pc1+pc2) )
                        print(" ")
                        return("Oponent cards: "+ str(bot_card1) +" and "+ str(bot_card2)+" and " + str(bot_card3)+  "   Total: "+ str(bot_card1+bot_card2+bot_card3) )







        else:
            print("Follow the instructions.") 

    if bet_in.isnumeric():
        if bet_in <= chips:
            bet = bet_in
            #prepere game / Pick cards
            pc1 = random.choice(cards)
            pc2 = random.choice(cards)
            player_cards = pc1+pc2
            bot_visable_card = random.choice(cards)
            bot_card1 = bot_visable_card
            bot_card2 = random.choice(cards)
            bot_cards = bot_card1+bot_card2
            if player_cards > 20:
                cards_limet = [2,3,4,5,6,7,9,10,10,10,10,1]
                pc1 = random.choice(cards)
                pc2 = random.choice(cards_limet)
                player_cards = pc1+pc2
                #start game
                return(start_game())
                
            else:
                return(start_game())

        else:
            return("You dont have enough chips.")    
    else:
        return("Invalid bet.")       
    return(" ")    

'''
def prepere_game():
    #Pick cards
    player_cards = random.choice(cards)+random.choice(cards)
    bot_visable_card = random.choice(cards)
    bot_cards = random.choice(cards)+bot_visable_card
    if player_cards > 20:
        cards_limet = [2,3,4,5,6,7,9,10,10,10,10,1]
        player_cards = random.choice(cards)+random.choice(cards_limet)
        #start game
    else:
        #start game    
'''



#print(set_bet())        
print(choose())