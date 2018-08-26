import random

try:
    import tkinter
except ImportError:   #For python 2
    import Tkinter as tkinter

#Function to load image.
def loadImage(cardsList):
    
    suits = ['club','diamond','heart','spade']
    faceCards = ['jack','queen','king']

    if tkinter.TkVersion >= 8.6:
        extension = '.png'

    else:
        extension = '.ppm'   #only tkinter ver8.6 and above can process png images.

    #building a string of card image path and adding them into cardList as tuple (card_number, uploadedImage)
    for num in range(1,11):
        for suit in suits:
            imageLocation = 'cardspng/cards/'+str(num)+'_'+suit+extension
            uploadedCards = tkinter.PhotoImage(file=imageLocation)
            cardsList.append((num,uploadedCards))
    for fCards in faceCards:
        for suit in suits:
            imageLocation = 'cardspng/cards/'+fCards+'_'+suit+extension
            uploadedCards = tkinter.PhotoImage(file=imageLocation)
            cardsList.append((10,uploadedCards))
    
#Function to deal cards
def dealCards(frame):
    #Draw card, then place the card at the bottom of the deck(Last item of deck)
    nextCard = deck.pop(0)
    deck.append(nextCard)
    #Display the card drawn
    tkinter.Label(frame,image=nextCard[1],relief='raised').pack(side='left')
    #pack and grid geometry manager should not be used together IN THE SAME WINDOW.
    #Return value of card, in this case, it is a tuple as defined previously
    #  when loading card images into cards list.
    return nextCard


#This function deals a card to dealer.
def dealDealer():
    #Extracting the value coressponding to the card image.
    #  while calling the function dealCards.
    cardValue = dealCards(cardFrameDealer)[0]
    #Initialising the variable totalPointsDealer.
    totalPointsDealer = sum(dealerHand)

    #Control flow to determine the value of Ace card
    if cardValue == 1:
        if totalPointsDealer < 11:
            cardValue = 11
            dealerHand.append(cardValue)
            #This line to update the value of totalPointsDealer
            totalPointsDealer = sum(dealerHand)
            #Display score to user
            scoreTextDealer.set(totalPointsDealer)
                
        elif totalPointsDealer >= 11:
            cardValue = 1
            dealerHand.append(cardValue)
            totalPointsDealer = sum(dealerHand)
            scoreTextDealer.set(totalPointsDealer)
                
    #If card is not Ace.
    #cardValue != 11 is not necessary as elif is used.
    #But if 'if' is used, it is crucial
    #elif will be overlooked if 'if' before itself is executed.
    #if will all be evaluated even if 'if' before itself is executed.
    else:
        dealerHand.append(cardValue)
        totalPointsDealer = sum(dealerHand)
        scoreTextDealer.set(totalPointsDealer)


    #If drawing results in a bust, this condition will convert the ace holding
    #   cardValue of 11 to 1.
    #Note that there can only be 1 ace holding cardValue of 11
    #   as filtered from the control flow to determine value of Ace card.
    if totalPointsDealer > 21:
        if 11 in dealerHand:
            dealerHand.remove(11)
            dealerHand.append(1)
            totalPointsDealer = sum(dealerHand)
            scoreTextDealer.set(totalPointsDealer)
        #else:
        #If there is no Ace card, it will be considered as an legit bust.
            #resultText.set('Player Wins!')
            
            #Creates the New game button. while removing the in-game button.
            #global is used to destroy and redefine buttonFrame variable
            #   in the global scope.
            #Without global, the code below can cause UnboundLocalError.
            #Read function notes for more info.
            #global buttonFrame
            #buttonFrame.destroy()
            #buttonFrame = tkinter.Frame(mainWindow)
            #buttonFrame.grid(row=3,column=0,sticky='w')
            #tkinter.Button(buttonFrame, text='New game', command=newGame).grid(row=0,column=0,sticky='w')
#THE COMMENTED CODE WILL NOT BE NECESSARY AS WHETHER THE DEALER BUST OR WIN AFTER
#   THE PLAYER STOP HITTING IS DECIDED IN THE FUNCTION stopHit
   
        
#See dealDealer for explanation of code. Its similar.
def dealPlayer():
    cardValue = dealCards(cardFramePlayer)[0]
    totalPointsPlayer = sum(playerHand)


    if cardValue == 1:
        if totalPointsPlayer < 11:
            cardValue = 11
            playerHand.append(cardValue)
            totalPointsPlayer = sum(playerHand)
            scoreTextPlayer.set(totalPointsPlayer)
                
        elif totalPointsPlayer >= 11:
            cardValue = 1
            playerHand.append(cardValue)
            totalPointsPlayer = sum(playerHand)
            scoreTextPlayer.set(totalPointsPlayer)

    elif cardValue != 1 or cardValue != 11:
        playerHand.append(cardValue)
        totalPointsPlayer = sum(playerHand)
        scoreTextPlayer.set(totalPointsPlayer)
        

    if totalPointsPlayer > 21:
        if 11 in playerHand:
            playerHand.remove(11)
            playerHand.append(1)
            totalPointsPlayer = sum(playerHand)
            scoreTextPlayer.set(totalPointsPlayer)
            
        else:
            #If there is no Ace card, it will be considered as an legit bust.
            resultText.set('Dealer Wins!')
            
            #Creates the New game button. while removing the in-game button.
            #global is used to destroy and redefine buttonFrame variable
            #   in the global scope.
            #Without global, the code below can cause UnboundLocalError.
            #Read function notes for more info.
            global buttonFrame
            buttonFrame.destroy()
            buttonFrame = tkinter.Frame(mainWindow)
            buttonFrame.grid(row=3,column=0,sticky='w')
            tkinter.Button(buttonFrame, text='New game', command=newGame).grid(row=0,column=0,sticky='w')

#When player stop hitting.
#This function lets the dealer hit appropriately and evaluate th result.
def stopHit():
    totalPointsDealer = sum(dealerHand)
    totalPointsPlayer = sum(playerHand)
    #Loop for dealer to draw appropriately
    while totalPointsDealer < 17 or totalPointsDealer == 17:
        if totalPointsDealer < 17:
            dealDealer()
            totalPointsDealer = sum(dealerHand)
       
        if totalPointsDealer == 17:
        #If soft 17, draw, if hard 17, stay.
            if 11 in dealerHand:
                dealDealer()
                totalPointsDealer = sum(dealerHand)
            else:
                break
        
    #Evaluating result of the match.
    if totalPointsDealer <= 21 and totalPointsDealer > totalPointsPlayer:
        resultText.set('Dealer Wins!')

    elif totalPointsDealer > 21:
        resultText.set('Player Wins!')
        
    elif totalPointsDealer < totalPointsPlayer:
        resultText.set('Player Wins!')

    elif totalPointsDealer == totalPointsPlayer:
        resultText.set('Draw!')
    
    global buttonFrame
    buttonFrame.destroy()
    buttonFrame = tkinter.Frame(mainWindow)
    buttonFrame.grid(row=3,column=0,sticky='w')
    tkinter.Button(buttonFrame, text='New game', command=newGame).grid(row=0,column=0,sticky='w')
        

#function for New game button.        
def newGame():
    #Clearing the cardframes,reset the decks, player/dealer hand
    #  reset result label and score labels.
    #global is used so that the variables in the global scope will be changed.
    #    instead of another variable with the same name, but in local scope.
    global cardFrameDealer
    global cardFramePlayer
    global playerHand
    global dealerHand
    global resultText
    global scoreTextDealer
    global scoreTextPlayer

    #Shuffle deck for next game
    random.shuffle(deck)

    #Clear hand
    dealerHand=[]
    playerHand=[]

    #Reset result and points display
    resultText.set('')
    scoreTextDealer.set(0)
    scoreTextPlayer.set(0)
   
    #Destroy cardframes, meaning clearing the card placed on gameTable.
    cardFrameDealer.destroy()
    cardFramePlayer.destroy()

    #Recreate cardFrames
    cardFrameDealer = tkinter.Frame(gameTable,background='green')
    cardFrameDealer.grid(row=0,column=1,sticky='nsew')

    cardFramePlayer = tkinter.Frame(gameTable,background='green')
    cardFramePlayer.grid(row=1,column=1,sticky='nsew')

    #Destroys New game button.
    global buttonFrame
    buttonFrame.destroy()
    buttonFrame = tkinter.Frame(mainWindow)
    buttonFrame.grid(row=3,column=0,sticky='w')
    
    #Recreate in-game buttons.
    playerButton = tkinter.Button(buttonFrame,text='Player draw',command=dealPlayer)
    playerButton.grid(row=0,column=1,sticky='w')

    stopHitting = tkinter.Button(buttonFrame, text='No more hit', command=stopHit)
    stopHitting.grid(row=0,column=2,sticky='w')

    #Computer dealer starts dealing initial cards.
    npcDealer()

#computer dealer to deal cards.
def npcDealer():
    global buttonFrame

    #Dealing cards in order according to rule.
    dealPlayer()
    dealDealer()
    dealPlayer()
    dealDealer()
    
    #To get the points for each side after dealing the cards.
    totalPointsDealer = sum(dealerHand)
    totalPointsPlayer = sum(playerHand)

    #Check for double blackjack
    if (totalPointsDealer == 21 and totalPointsPlayer == 21):
        resultText.set('Draw!')
        
        buttonFrame.destroy()
        buttonFrame = tkinter.Frame(mainWindow)
        buttonFrame.grid(row=3,column=0,sticky='w')
        newGameButton = tkinter.Button(buttonFrame, text='New game', command= newGame)
        newGameButton.grid(row=0,column=0,sticky='w')

    #If dealer gets blackjack    
    elif totalPointsDealer == 21:

        resultText.set('Dealer Wins!')
        
        
        buttonFrame.destroy()
        buttonFrame = tkinter.Frame(mainWindow)
        buttonFrame.grid(row=3,column=0,sticky='w')
        newGameButton = tkinter.Button(buttonFrame, text='New game', command= newGame)
        newGameButton.grid(row=0,column=0,sticky='w')


    #If player gets blackjack
    elif totalPointsPlayer == 21:

        resultText.set('Player Wins!')
        
        
        buttonFrame.destroy()
        buttonFrame = tkinter.Frame(mainWindow)
        buttonFrame.grid(row=3,column=0,sticky='w')
        newGameButton = tkinter.Button(buttonFrame, text='New game', command= newGame)
        newGameButton.grid(row=0,column=0,sticky='w')                       

#Allows game to start.
def play():
    npcDealer()
    #Keep the tkinter window up by looping the gui code
    mainWindow.mainloop()
    

#GUI using tkinter.
mainWindow = tkinter.Tk()
mainWindow.title('Blackjack')
mainWindow.geometry('640x480+200+200')
mainWindow.configure(background='green')

#Frame representing the whole table.
gameTable = tkinter.Frame(mainWindow,background='green')
gameTable.grid(row=1, column=0,columnspan=2,sticky='nsew')

#result display
resultText = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=resultText,background='green',font=30)
result.grid(row=0,column=0,sticky='ew')


#Score display for Dealer
#Frame for the display.
scoreFrameDealer = tkinter.Frame(gameTable, background='green',relief='raised')
scoreFrameDealer.grid(row=0,column=0,sticky='ns')

#Labels for displaying the points and 'Dealer' label
scoreTextDealer = tkinter.IntVar()
dealerLabel = tkinter.Label(scoreFrameDealer,text='Dealer',background='green',fg='white')
dealerLabel.grid(row=1,column=0,sticky='ew')
dealerScore = tkinter.Label(scoreFrameDealer,textvariable=scoreTextDealer,background='green',fg='white')
dealerScore.grid(row=2,column=0,sticky='ew')

#Score display for Player
#Frame for the display
scoreFramePlayer = tkinter.Frame(gameTable, background='green',relief='raised')
scoreFramePlayer.grid(row=1,column=0,sticky='ns')

#Labels for displaying the points and 'Player' label
scoreTextPlayer = tkinter.IntVar()
playerLabel = tkinter.Label(scoreFramePlayer,text='Player',background='green',fg='white')
playerLabel.grid(row=3,column=0,sticky='ew')
playerScore = tkinter.Label(scoreFramePlayer,textvariable=scoreTextPlayer,background='green',fg='white')
playerScore.grid(row=4,column=0,sticky='ew')

#Frame for dealer's cards on the table
cardFrameDealer = tkinter.Frame(gameTable,background='green')
cardFrameDealer.grid(row=0,column=1,sticky='nsew')

#Frame for player's's cards on the table
cardFramePlayer = tkinter.Frame(gameTable,background='green')
cardFramePlayer.grid(row=1,column=1,sticky='nsew')

#Buttons for player to hit.
#Frame for in-game buttons.
buttonFrame = tkinter.Frame(mainWindow)
buttonFrame.grid(row=3,column=0,sticky='w')
#Player hit button
playerButton = tkinter.Button(buttonFrame,text='Player draw',command=dealPlayer)
playerButton.grid(row=0,column=1,sticky='w')

#Button for the case when player no longer wants to hit.
stopHitting = tkinter.Button(buttonFrame, text='No more hit', command=stopHit)
stopHitting.grid(row=0,column=2,sticky='w')



#Code to prepare the game during first launch.
#load card images into list.
cards = []
loadImage(cards)

#From the list, create new deck
deck = list(cards)
#Good to make another list of cards so that the loaded cards list, cards,
#  will not be affected by players/dealers drawing cards and hence, we can
#  use the loaded cards list to create a new deck again.
random.shuffle(deck)

#Initialising list for player's/dealer's hand.
playerHand = []
dealerHand = []


#Condition for this program to run.(This allows proper importing of this program
#as a module to other program
if __name__ == '__main__':
    play()



