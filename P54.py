### NOTE TEMPORARILY ABANDONED PROBLEM DUE TO NON-ELEGANT SOLUTION ###

## Problem 54

## In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

##    High Card: Highest value card.
##    One Pair: Two cards of the same value.
##    Two Pairs: Two different pairs.
##    Three of a Kind: Three cards of the same value.
##    Straight: All cards are consecutive values.
##    Flush: All cards of the same suit.
##    Full House: Three of a kind and a pair.
##    Four of a Kind: Four cards of the same value.
##    Straight Flush: All cards are consecutive values of same suit.
##    Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

## The cards are valued in the order:
## 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

## If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

## Consider the following five hands dealt to two players:
## Hand	 	Player 1	 	Player 2	 	Winner
## 1	 	5H 5C 6S 7S KD
## Pair of Fives
## 	 	2C 3S 8S 8D TD
## Pair of Eights
## 	 	Player 2
## 2	 	5D 8C 9S JS AC
## Highest card Ace
## 	 	2C 5C 7D 8S QH
## Highest card Queen
## 	 	Player 1
## 3	 	2D 9C AS AH AC
## Three Aces
## 	 	3D 6D 7D TD QD
## Flush with Diamonds
## 	 	Player 2
## 4	 	4D 6S 9H QH QC
## Pair of Queens
## Highest card Nine
## 	 	3D 6D 7H QD QS
## Pair of Queens
## Highest card Seven
## 	 	Player 1
## 5	 	2H 2D 4C 4D 4S
## Full House
## With Three Fours
## 	 	3C 3D 3S 9S 9D
## Full House
## with Three Threes
## 	 	Player 1

## The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): 
## the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid 
## (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

## How many hands does Player 1 win? (note code only counts Ace as high card, not as low)

def poker_hands():

	# import timeit and start timer to measure time of function
	import timeit
	start = timeit.default_timer()
	
	# import urllib2 package to download poker.txt file from Project Euler website
	import urllib2 
    
    # download poker.txt and store in "data" object
	data = urllib2.urlopen("https://projecteuler.net/project/resources/p054_poker.txt")
	
	solution = [] # list to hold Player 1/2 win tally
	
	card_dict = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10, "J":11, "Q":12, "K":13, "A":14} # dictionary for face cards to numbers
	
	poker_hands = [] # initialize list for holding tuples - all ten cards in sequence in each tuple
	
	# transform poker.txt "data" object to "poker" list of tuples - index for Player 1 five cards is 0-1, 3-4, 6-7, 9-10, 12-13 & Player 2 five cards are
	# 15-16, 18-19, 21-22, 24-25, 27-28
	
	for line in data:
		poker_hands.append(line)
    
	for hand in range(0,len(poker_hands)-1): # iterate through length of poker hands text file
	
		# if player 1 has a royal flush - score win
		if card_dict[poker_hands[hand][0]] + card_dict[poker_hands[hand][3]] + card_dict[poker_hands[hand][6]] + \
		card_dict[poker_hands[hand][9]] + card_dict[poker_hands[hand][12]] == 60 \
		and set(poker_hands[hand][1] + poker_hands[hand][4] + poker_hands[hand][7] + poker_hands[hand][10] + poker_hands[hand][13]) == 1:
			solution.append("Player 1")
		
		# if player 2 has a royal flush - score win
		if card_dict[poker_hands[hand][15]] + card_dict[poker_hands[hand][18]] + card_dict[poker_hands[hand][21]] + \
		card_dict[poker_hands[hand][24]] + card_dict[poker_hands[hand][27]] == 60 \
		and set(poker_hands[hand][16] + poker_hands[hand][19] + poker_hands[hand][22] + poker_hands[hand][25] + poker_hands[hand][28]) == 1:
			solution.append("Player 2")
			
		# if player 1 has a straight flush - score win
		if card_dict[poker_hands[hand][12]] - card_dict[poker_hands[hand][9]] == 1 and card_dict[poker_hands[hand][9]] - card_dict[poker_hands[hand][6]] == 1 \
		and card_dict[poker_hands[hand][6]] - card_dict[poker_hands[hand][3]] == 1 and card_dict[poker_hands[hand][3]] - card_dict[poker_hands[hand][0]] == 1 \
		and set(poker_hands[hand][1] + poker_hands[hand][4] + poker_hands[hand][7] + poker_hands[hand][10] + poker_hands[hand][13]) == 1:
			solution.append("Player 1")
		
		# if player 2 has a straight flush - score win
		if card_dict[poker_hands[hand][27]] - card_dict[poker_hands[hand][24]] == 1 and card_dict[poker_hands[hand][24]] - card_dict[poker_hands[hand][21]] == 1 \
		and card_dict[poker_hands[hand][21]] - card_dict[poker_hands[hand][18]] == 1 and card_dict[poker_hands[hand][18]] - card_dict[poker_hands[hand][15]] == 1 \
		and set(poker_hands[hand][16] + poker_hands[hand][19] + poker_hands[hand][22] + poker_hands[hand][25] + poker_hands[hand][28]) == 1:
			solution.append("Player 2")		
		
		# if player 1 has four of a kind - score win	
		check_list = [] # initialize temporary list
		check_list.append(poker_hands[hand][0]), check_list.append(poker_hands[hand][3]), check_list.append(poker_hands[hand][6]), check_list.append(poker_hands[hand][9]), check_list.append(poker_hands[hand][12])
		if sorted(check_list)[0] == sorted(check_list)[1] and sorted(check_list)[1] == sorted(check_list)[2] and sorted(check_list)[2] == sorted(check_list)[3]:
			solution.append("Player 1")
			
		if sorted(check_list)[1] == sorted(check_list)[2] and sorted(check_list)[2] == sorted(check_list)[3] and sorted(check_list)[3] == sorted(check_list)[4]:
			solution.append("Player 1")	
			
		# if player 2 has four of a kind - score win	
		check_list = [] # initialize temporary list
		check_list.append(poker_hands[hand][15]), check_list.append(poker_hands[hand][18]), check_list.append(poker_hands[hand][21]), check_list.append(poker_hands[hand][24]), check_list.append(poker_hands[hand][27])
		if sorted(check_list)[0] == sorted(check_list)[1] and sorted(check_list)[1] == sorted(check_list)[2] and sorted(check_list)[2] == sorted(check_list)[3]:
			solution.append("Player 2")
			
		if sorted(check_list)[1] == sorted(check_list)[2] and sorted(check_list)[2] == sorted(check_list)[3] and sorted(check_list)[3] == sorted(check_list)[4]:
			solution.append("Player 2")	
			
		# if player 1 has a full house - score win	
		check_list = [] # initialize temporary list
		check_list.append(poker_hands[hand][0]), check_list.append(poker_hands[hand][3]), check_list.append(poker_hands[hand][6]), check_list.append(poker_hands[hand][9]), check_list.append(poker_hands[hand][12])
		if sorted(check_list)[0] == sorted(check_list)[1] and sorted(check_list)[1] == sorted(check_list)[2] and sorted(check_list)[3] == sorted(check_list)[4]:
			solution.append("Player 1")
			
		if sorted(check_list)[4] == sorted(check_list)[3] and sorted(check_list)[3] == sorted(check_list)[2] and sorted(check_list)[1] == sorted(check_list)[0]:
			solution.append("Player 1")	
			
		# if player 2 has a full house - score win	
		check_list = [] # initialize temporary list
		check_list.append(poker_hands[hand][15]), check_list.append(poker_hands[hand][18]), check_list.append(poker_hands[hand][21]), check_list.append(poker_hands[hand][24]), check_list.append(poker_hands[hand][27])
		if sorted(check_list)[0] == sorted(check_list)[1] and sorted(check_list)[1] == sorted(check_list)[2] and sorted(check_list)[3] == sorted(check_list)[4]:
			solution.append("Player 2")
			
		if sorted(check_list)[4] == sorted(check_list)[3] and sorted(check_list)[3] == sorted(check_list)[2] and sorted(check_list)[1] == sorted(check_list)[0]:
			solution.append("Player 2")		
		
		# if player 1 has a flush - score win
		if card_dict[poker_hands[hand][0]] + card_dict[poker_hands[hand][3]] + card_dict[poker_hands[hand][6]] + \
		card_dict[poker_hands[hand][9]] + card_dict[poker_hands[hand][12]] != 60 \
		and set(poker_hands[hand][1] + poker_hands[hand][4] + poker_hands[hand][7] + poker_hands[hand][10] + poker_hands[hand][13]) == 1:
			solution.append("Player 1")
		
		# if player 2 has a flush - score win
		if card_dict[poker_hands[hand][15]] + card_dict[poker_hands[hand][18]] + card_dict[poker_hands[hand][21]] + \
		card_dict[poker_hands[hand][24]] + card_dict[poker_hands[hand][27]] != 60 \
		and set(poker_hands[hand][16] + poker_hands[hand][19] + poker_hands[hand][22] + poker_hands[hand][25] + poker_hands[hand][28]) == 1:
			solution.append("Player 2")
		
		# if player 1 has straight, score win
		check_list = [] # initialize temporary list
		check_list.append(poker_hands[hand][0]), check_list.append(poker_hands[hand][3]), check_list.append(poker_hands[hand][6]), check_list.append(poker_hands[hand][9]), check_list.append(poker_hands[hand][12])
		if card_dict[sorted(check_list, reverse=True)[0]] - card_dict[sorted(check_list, reverse=True)[1]] == 1 and card_dict[sorted(check_list, reverse=True)[1]] - card_dict[sorted(check_list, reverse=True)[2]] == 1 and card_dict[sorted(check_list, reverse=True)[2]] - card_dict[sorted(check_list, reverse=True)[3]] == 1 and card_dict[sorted(check_list, reverse=True)[3]] - card_dict[sorted(check_list, reverse=True)[4]] == 1:
			solution.append("Player 1")
			
		# if player 2 has straight, score win
		check_list = [] # initialize temporary list
		check_list.append(poker_hands[hand][15]), check_list.append(poker_hands[hand][18]), check_list.append(poker_hands[hand][21]), check_list.append(poker_hands[hand][24]), check_list.append(poker_hands[hand][27])
		if card_dict[sorted(check_list, reverse=True)[0]] - card_dict[sorted(check_list, reverse=True)[1]] == 1 and card_dict[sorted(check_list, reverse=True)[1]] - card_dict[sorted(check_list, reverse=True)[2]] == 1 and card_dict[sorted(check_list, reverse=True)[2]] - card_dict[sorted(check_list, reverse=True)[3]] == 1 and card_dict[sorted(check_list, reverse=True)[3]] - card_dict[sorted(check_list, reverse=True)[4]] == 1:
			solution.append("Player 2")	
			
	print solution
	
	# stop timer and print total elapsed time
	stop = timeit.default_timer()
	print "Total time:", stop - start