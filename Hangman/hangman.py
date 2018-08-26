#Hangman program with GUI
#Trying out documentation for class

#Features:
#   Display a few letters of the hidden word. Number depends on length of word OK
#   Hidden letters are replaced with underscore. OK
#   Actual hangman being drawn. OK
#   GameOver once hangman drawing is completed.  OK
#   New game when words are guessed correctly.   OK
#   A library of many words to choose from. **Can use txt file to compile lists of words.
#   Difficulty levels, easy and hard.


try:
    import tkinter

except ImportError:
    import Tkinter as tkinter   #For python2

import random

#Class and functions
class hangMan(object):

    '''This class encompasses the whole hang man game. Each instances will be a hangman game.

        Attributes:
            __mode (str) : the mode of the game
            __randomWord (str) : The random word chosen from __wordList
            __wrongCounter (str) : The counter to determine when will the game be over
            __checkList (str) : A list that updates when user key in the correct letter.
                    Will be used to check if the user have correctly typed out the correct word.
            __wordDict (dict) : A dictionary containing keys which indicates category.
                    Under each key(category), there will be a set of words which fufils the category.
                    The key will be used as hints.

        Methods:
            start(self) : To start the game.
            _randomWordGen(self) : From __wordList, pick a random word from a random category.
                    Chosen word will be __randomWord.

            _displayHidWord(self, randomWord (str)) : Displays the argument, randomWord, on the game screen, hidden with '_'.
                    Depending on the length of randomWord, different number of letters of randomWord will be revealed.

            inputChecker(self, letter (str)) : Takes in the arguement, letter, and check if
                    the argument is the correct letter of the __randomWord.
                    It will handle the outcome of getting the right and wrong letters.
    '''



    def __init__(self,mode):
        self.__mode = mode
        self.__randomWord = ''
        self.__wrongCounter = 0
        self.__checkList = []
        self.__wordDict = {'Animals':{'ELEPHANT','BIRD','DOG','DINOSAUR','BEAR','MONKEY'},
                           'Vehicles':{'PLANE','CAR','TRUCK','MOTORBIKE','BOAT','TRAIN'},
                           }


    #Random word generator
    def _randomWordGen(self):

        #random.choice work with index. Therefore, a list of keys is needed.
        #Choose a random key(category).
        randomCat = random.choice(list(self.__wordDict))
        #Display hint.
        category.set('hint : ' + randomCat)

        #Storing the random word choosing the the category.
        self.__randomWord = random.choice(list(self.__wordDict[randomCat]))

        #Pass the chosen word to display appropriately on screen.
        self._displayHidWord(self.__randomWord)

    #Display the chosen word as '_'. Revealing only some
    def _displayHidWord(self, randomWord):
        '''Args:
            randomWord (str) : The string of the random chosen word to be hidden and displayed on the game screen.

           Functions:
               reveal (numToReveal (int)) : Decides how many letters of the chosen word to reveal.

        '''


        #Function to decide how many letters to reveal
        def reveal(numToReveal):
            '''Args:
                numToReveal (int) : Indicates how many letters of the chosen word to reveal.
            '''

            #sample returns a list of number(To be used as indexes).
            #To decide which index of the chosen word to reveal.
            #Second argument of sample indicates how many samples to collect.
            ranIndex = random.sample(range(0,len(randomWord)),numToReveal)

            #Using index to link display and the chosen word.
            for i in range(0,len(randomWord)):

                #If index number is in the sample, reveal the letter.
                if i in ranIndex:
                    listOfDisplay[i].set(randomWord[i])
                    #Add to check list.
                    self.__checkList.append(randomWord[i])
                #If now chosen to be revealed, hide the letter with '_'.
                else:
                    listOfDisplay[i].set('_')
                    #Add to check list.
                    self.__checkList.append('_')

                    #NOTE THAT SINCE LETTERS ARE LITERATED IN INDEX ORDER, CHECKLIST WILL BE APPENDED IN
                    #   ORDER AS WELL
                    #   What is displayed on the game screen will be the same as what is in the list.

        #reveal function in use.
        #Depending on the length of the random word, reveal different number of letters.
        #The difficulty level function can be added here. but im lazy lols.
        length = len(randomWord)

        if self.__mode == 'easy':

            if length <= 4:
                reveal(2)

            if 5 <= length <= 6:
                reveal(3)

            if length == 7:
                reveal(4)

            if length == 8:
                reveal(5)

            if length > 8:
                reveal(6)

        elif self.__mode == 'hard':

            if length <= 4:
                reveal(1)

            if 5 <= length <= 6:
                reveal(2)

            if length == 7:
                reveal(2)

            if length == 8:
                reveal(3)

            if length > 8:
                reveal(4)

    #Starts the game by calling the function that generates random words.
    def start(self):
        self._randomWordGen()





    #Keying in alphabets.
    def inputChecker(self, letter):
        '''Args:
            letter (str) : The argument is the letter that is linked to each button.
                Using the letter, the function will check and decide the outcome of the game.
            Functions:
                newGame : Restarts the game after game is over, win or lose.
                gameOver : Indicates game over.
                wrongLetter (count(int)) : Keep tracks of the number of chances left
                    and draws the hang man stroke by stroke.
        '''

        def newGame():

            #Making sure these variables are global, otherwise, other functions
            #   that need these variables will be unable to access it.
            global GTWLabel
            global category
            global hint
            global letterFrame
            global hangManCanvas
            global newGameButton


            #Destroy new game button after clicking on the button
            newGameButton.destroy()

            #Reset counters and checklist
            self.__wrongCounter = 0
            self.__checkList = []

            #clear hidword display(max 10 letters)
            for i in range(0,10):
                listOfDisplay[i].set('')

            #clear dead hangman drawing.
            hangManCanvas.destroy()

            #Label 'guess the word' display again.
            GTWLabel = tkinter.Label(wordFrame,background='black', foreground='white', text='Guess the word!')
            GTWLabel.grid(row=0,column=0,sticky='ew')

            #Hint label again.
            category = tkinter.StringVar()
            hint = tkinter.Label(wordFrame, background='black', foreground='white', textvariable=category)
            hint.grid(row=1,column=0,sticky='ew')

            #Frame and buttons for the letters A to Z again.
            letterFrame = tkinter.Frame(wordFrame, background='black')
            letterFrame.grid(row=3,column=0,sticky='nsew')
            #Cannot use for row in range(0,5) as the number will only go to the next one
            #   when the list is completely iterated.
            #   ie. row will be 0 until the buttons for last letterSet is created.
            #       resulting in the last letterSet being on row 0.
            #This will continue to the range, resulting in everyrow being the last letterSet only.

            row=0
            for letterSet in alphabets:
                column = 0
                for letter in letterSet:
                    tkinter.Button(letterFrame, background ='black', foreground='white', width=4, text=letter, command=lambda letter=letter: hMGame.inputChecker(letter)).grid(row=row,column=column,stick='nsew')
                    column += 1
                row +=1

            #Recreate hangman canvas
            hangManCanvas = tkinter.Canvas(hangManFrame, background='gray')
            hangManCanvas.grid(row=0,column=0,sticky='nsew')
            # (0,0) starts from the top left corner, everything within the canvas is postive.
            #create_line or create_oval has the coordinates argument format
            #   (fromX,fromY,toX,toY)

            #Kick start the game.
            hMGame.start()


        def gameOver():
            #making newGameButton a global variable as it is needed by all the functions
            #    in inputchecker.
            global newGameButton

            #Destroy all buttons, clear hint display and 'guess the word'.
            letterFrame.destroy()
            GTWLabel.destroy()
            hint.destroy()


            #Replace the chosen word display with game over.
            gameOverTxt = 'GAME OVER '

            for i in range(0,len(gameOverTxt)):
                listOfDisplay[i].set(gameOverTxt[i])

            #Create new game button.
            newGameButton = tkinter.Button(mainWindow, background ='black', foreground='white',text='New game',command=newGame)
            newGameButton.grid(row=1,column=0,sticky='nsew')




        def wrongLetter(count):
            #Hang man drawing, stroke by stroke, as wrong count increase.
            #support poles
            if count == 0:
                hangManCanvas.create_line(20,20,150,20,fill='white',width=6)

            elif count == 1:
                hangManCanvas.create_line(130,20,130,270,fill='white',width=6)

            #Rope
            elif count == 2:
                hangManCanvas.create_line(75,16,75,100,fill='brown', width=3)
            #head
            elif count == 3:
                hangManCanvas.create_oval(30,70,80,120,outline='white',fill='white',width=2)

            #torso and neck
            elif count == 4:
                hangManCanvas.create_line(70,120,80,112,fill='brown',width=7)
                hangManCanvas.create_line(75,123,75,180,fill='white',width=4)

            #arms
            elif count == 5:
                hangManCanvas.create_line(75,120,80,160,fill='white',width=4)

            elif count == 6:
                hangManCanvas.create_line(75,120,65,160,fill='white',width=4)

            #legs
            elif count == 7:
                hangManCanvas.create_line(75,180,65,240,fill='white',width=4)

            elif count == 8:
                hangManCanvas.create_line(75,180,85,240,fill='white',width=4)
                gameOver()

                #Under inputChecker
                #Updates the chosen word display letter by letter if the letter clicked by player is correct.
                #Comparing by repeated iteration for each letter clicked to allow
                #repeated letters to be updated. ie. MOON has 2 'O's. Using .find will only
                #result in the index of the first O to be returned, hence, the second O will
                #never be updated and the game will never end.
        for i in range(0,len(self.__randomWord)):
            #If letter clicked = letter of chosen Word in position i, update the display and checklist.
            if letter == self.__randomWord[i]:
                listOfDisplay[i].set(letter)
                self.__checkList[i] = letter

                #To see how the checklist updates as the game go on.
                print(self.__checkList)

                #Converts the chosen word into a list and compare it to the check list.
                #If both has the same value, The game will end and user will win.
                if list(self.__randomWord) == self.__checkList:

                    global newGameButton

                    letterFrame.destroy()
                    GTWLabel.destroy()
                    hint.destroy()

                    winGameTxt = 'CONGRATZ!!'

                    for i in range(0,len(winGameTxt)):
                        listOfDisplay[i].set(winGameTxt[i])

                    newGameButton = tkinter.Button(mainWindow, background ='black', foreground='white',text='New game',command=newGame)
                    newGameButton.grid(row=1,column=0,sticky='nsew')


        #If letter clicked do not exist in the chosen word, draw the hangman and update wrong counter.
        if letter not in self.__randomWord:
            wrongLetter(self.__wrongCounter)
            self.__wrongCounter += 1




if __name__ == '__main__':
    #The main window
    mainWindow = tkinter.Tk()
    mainWindow.title('Hangman')
    mainWindow.geometry('420x420+200+200')

    #Frame for the letter selections and words display.
    wordFrame = tkinter.Frame(mainWindow,background='black',relief='raised')
    wordFrame.grid(row=0,column=0,sticky='nswe')

    #Label 'guess the word' display.
    GTWLabel = tkinter.Label(wordFrame,background='black', foreground='white', text='Guess the word!')
    GTWLabel.grid(row=0,column=0,sticky='ew')

    #Hint label
    category = tkinter.StringVar()
    hint = tkinter.Label(wordFrame, background='black', foreground='white', textvariable=category)
    hint.grid(row=1,column=0,sticky='ew')



    #Frame and text for hiddenword display.
    hidWordFrame = tkinter.Frame(wordFrame, background='black', relief='sunken',borderwidth=10)
    hidWordFrame.grid(row=2, column=0,sticky='ew')


    #A way to produce many different displays will different tkinter.StringVar()
    #Assigning each key as number, in order of index, will link the position of each display to the position of each letter in the chosen word.
    #   Since indexes progresses similarly, ie. 0,1,2,3,4....
    listOfDisplay = dict()
    for i in range(0,10):
        listOfDisplay[i] = tkinter.StringVar()
        #Each button will get its text from different tkinter.StringVar() attached to different keys.
        hidWordLabel = tkinter.Label(hidWordFrame, background='black', foreground='white', textvariable=listOfDisplay[i])
        #The labels will be created will left to right, with it getting its text from tkinter.StringVar()
        #   that is attached to a number(acting as the index of the display)
        #It is like each display perfectly corresponds to each position of an iterable.
        hidWordLabel.grid(row=0,column=i,stick='nwes')
        #This implies that you can set the value of the label at a specific position that you want.




    #Frame and buttons for the letters A to Z
    letterFrame = tkinter.Frame(wordFrame, background='black')
    letterFrame.grid(row=3,column=0,sticky='nsew')

    alphabets = [('A','B','C','D','E'),('F','G','H','I','J'),('K','L','M','N','O'),
                 ('P','Q','R','S','T'),('U','V','W','X','Y','Z')]


    #Cannot use for row in range(0,5) as the number will only go to the next one
    #   when the list is completely iterated.
    #   ie. row will be 0 until the buttons for last letterSet is created.
    #       resulting in the last letterSet being on row 0.
    #This will continue to the range, resulting in everyrow being the last letterSet only.

    row=0
    for letterSet in alphabets:
        column = 0
        for letter in letterSet:
            #Lambda is like anon function in javascript.
            #Each letter iterated will be assigned to a default argument of the lambda expression.
            #       and each button will have the lambda expression with different letter as its default argument.
            tkinter.Button(letterFrame, background ='black', foreground='white', width=4, text=letter, command=lambda buttonLetter=letter: hMGame.inputChecker(buttonLetter)).grid(row=row,column=column,stick='nsew')
            column += 1
        row +=1


    #Frame and canvas for hangman drawing.
    hangManFrame = tkinter.Frame(mainWindow)
    hangManFrame.grid(row=0,column=1,sticky='nsew')

    hangManCanvas = tkinter.Canvas(hangManFrame, background='gray')
    hangManCanvas.grid(row=0,column=0,sticky='nsew')
    # (0,0) starts from the top left corner, everything within the canvas is postive.
    #create_line or create_oval has the coordinates argument format
    #   (fromX,fromY,toX,toY)



    #Initial launch of the game.
    hMGame = hangMan('hard')
    hMGame.start()

    mainWindow.mainloop()


