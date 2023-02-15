
from graphics import *
import random


class Mainball():                   
    '''Creates the guess ball'''
    def __init__(self, color):
        self.color = color
        self.diameter = 52

    def getColor(self):         #Retrieves the color
        return self.color

    def getDiameter(self):      #Retrieves the diameter
        return self.diameter

class Feedbackball():
    '''Creates the feedback ball'''
    def __init__(self, color):
        self.color = color
        self.diameter = 13
    
    def getColor(self):         #Retrieves the color which will be white or black
        return self.color
    
    def getDiameter(self):      #Retrieves the diameter
        return self.diameter


class Column():
    '''Creates a row for the graphics balls. Allows them to be drawn and the feedback to be manipulated.'''
    def __init__(self, mainList, feedback):
        self.mainList = mainList
        self.feedback = feedback

    def changeFeedback(self, newFeedback):      #changes the feedback 
        self.feedback = newFeedback
        return self.feedback

    def columnPlay(self, mainList, count, window):          #draws the four balls for a guess

        center = Point(56 + (mainList[0].getDiameter() + 20) * count, 56)     #the centre point starts at 56 + the diameter + 20 pixels away from the edge. 
                                                                            #Each time we call it, it draws the next ball 1 diameter and 20 pixels to the right of the previous column. 
        

        for item in mainList:                                               #draws the 4 balls in the guess
            ball = Circle(center, (item.getDiameter())//2)
            ball.draw(window)
            ball.setFill(item.getColor())                                   #sets the color to the color of the ball
            diameter = item.getDiameter()
            center = Point(int(center.getX()), int(center.getY()) + diameter + 5) #draws the next ball a diamter and 5 pixels down from the previous

    def masterPlay(self, mainList, window):
        '''draws the master list, so the user can easily compare the guesses to it'''
        center = Point(954 , 56)    #on the right side of the window

        for item in mainList:                               #draws the 4 balls in the master list
            ball = Circle(center, (item.getDiameter())//2)
            ball.draw(window)
            ball.setFill(item.getColor())                   #sets the color to the color of the ball
            diameter = item.getDiameter()
            center = Point(int(center.getX()), int(center.getY()) + diameter + 5)   #draws the next ball a diamter and 5 pixels down from the previous

    def feedbackPlay(self, mainList, feedback, count, window):                      
        '''draws the feedback given'''
        diameter = mainList[0].getDiameter()
        center = Point((28 + diameter//8 + (diameter + 20) * count), 260 + diameter//2)
            
        for item in feedback:                                           #draws each feedback ball
            ball = Circle(center, item.getDiameter()//2)
            ball.draw(window)
            ball.setFill(item.getColor())                               #sets the color to the color of the ball
            diameter = item.getDiameter()
            center = Point(int(center.getX()) + diameter + 2, int(center.getY()))   #draws the next ball a diameter and 2 pixels to the right of the previous

class listrow():        #makes a class for each play which contains the guess and the feedback.
    def __init__(self, guess, feedback):
        self.guess = guess
        self.feedback = feedback

    def getFeedback(self):
        return self.feedback

    def getPlay(self):
        return self.guess




def spellcheck(guess, colorlist):               #makes sure that the user enters the right spelling 
    if guess == "":                             #allows the user to quit
        return True
    for r in guess:
        if r not in colorlist:                  #if the entered word is misspelled or a different color, it returns false
            return False
    return True                                 #returns true otherwise

def spellcheckFB(feedback):                     #makes sure that the user enters the right spelling
    if feedback == "":                          #allows the user to quit
        return True
    feedbacklist = ["white", "black"]           
    for s in feedback:
        if s not in feedbacklist:               #if the entered word is misspelled or a different color, it returns false
            return False
    return True                                 #returns true otherwise

def possibilities(guess, length):
    if length == 1:
        return guess
    else:
        result = []
        for first in guess:
            for rest in possibilities(guess, length-1):
                
                result.append(first + ", " + rest)
    
    for u in guess:
        i = 0
        while i < len(result): 
            if result[i].count(u) > 1:
                result.remove(result[i])
            else:
                i += 1
    return result

def goodPossibilities(result, listguess, count):
    for x in range(count):
        if "black" not in listguess[x].getFeedback():
            play = listguess[x].getPlay()
            for y in play:
                i = 0
                while i < len(result):
                    index = play.index(y)
                    z = result[i]
                    aa = z.split(", ")
                    if y == aa[index]:
                        result.remove(z)
                    else:
                        i += 1
    return result

            
def repeat(guess, listguess, count):
    '''checks to see if the guess has already been played'''
    for i in range(count):
        if guess == listguess[i].getPlay():
            return True
    return False

def noRepeat(guess, listguess, count):
    '''shuffles a guess if it has been played'''
    if repeat(guess, listguess, count) == False:
        return guess
    else:
        random.shuffle(guess)
        random.shuffle(guess)
        noRepeat(guess, listguess, count)
    return guess 


def replay(colorlist, window):                                              #allows user to replay
    playagain = input("Do you want to play again? Y or N: ")
    if playagain == "Y":
        window.close()
        gameplay(colorlist)
    else:
        return print("Thanks for playing! See you soon.")

#when a row object is created, it takes the name of the next index in the list, and replaces the string at that index with the new object
listguess = ["guess1", "guess2", "guess3", "guess4", "guess5", "guess6", "guess7", "guess8", "guess9", "guess10"]

def humanmastermind(colorlist, count, guess, masterlist, listguess, window):
    '''runs when the human plays as mastermind. The computer has 10 guesses to guess the right answer. 
    The first play has already been guessed and passed in as a parameter.'''
    feedback = []                               #creates an empty feedback list to be used as a parameter
    guessCompare = guess.copy()                 #creates a copy of guess that is used for processing


    for g in range(4):                          #turns each item in guess into a graphics object
        guess[g] = Mainball(guess[g])
    play = Column(guess, feedback)              #saves each guess
    play.columnPlay(guess, count, window)       #draws the balls in the window
    
    print("Computer has", 10 - count, "guesses left.")  #prints the number of guesses left. 
    strfeedback = input("Input feedback: ")             #gets the feedback on the correctness of the guess from the human
    feedback = strfeedback.split(', ')                  #turns the feedback into a list
    feedbackCompare = feedback.copy()

    while spellcheckFB(feedback) == False:          #spellchecks the feedback
        if strfeedback == "":
            return
        strfeedback = input("Oops! Make sure the feedback is spelled correctly. Input feedback: ")             
        feedback = strfeedback.split(', ') 

    listguess[count - 1] = listrow(guessCompare, feedbackCompare)        #makes a row object for processing after each guess


    play.changeFeedback(feedback)                                       #updates the curernt guess with its feedback
    for f in range(len(feedback)):                                      #turns each feedback ball into an object
        feedback[f] = Feedbackball(feedback[f])
   
    play.feedbackPlay(guess, feedback, count, window)                   #draws the feedback balls

   
    
    
    if feedbackCompare == [""]:                    #allows the user to exit by pressing enter.
        return 
    elif feedbackCompare == ["black", "black", "black", "black"]: #if the computer guesses correctly and gets all blacks, it wins.
        print("Computer wins!")
        return replay(colorlist, window)            #allows user to replay
    else:
        if count == 10:                     #if the computer guess incorrectly all ten times then the humnan wins.
            print("You win!")
            return replay(colorlist, window)        #allows user to replay
        if len(feedbackCompare) == 1:
            switch = []                     #creates an empty list to store all colors not guessed. 
            for i in colorlist:             #stores the colors in the list
                if i not in guessCompare:
                    switch.append(i)
            guessCompare = list(guessCompare)             #turns guessCompare into a list
            guessCompare.pop(3)                    #takes out the last value in the list
            guessCompare.pop(2)
            guessCompare.pop(1)                    #takes out the second last value in the list
            switch = random.sample(switch, 3)
            if feedbackCompare == ['black']:
                guessCompare = guessCompare + switch
            else:
                guessCompare = switch + guessCompare         #combines what's left of guessCompare and switch
        elif len(feedbackCompare) == 2: 
            '''sequence of steps when the computer guessed two colors correctly but not necessarily in place.'''
            switch = []                     #creates an empty list to store all colors not guessed. with 6 colors to guess, this will only be 2 items long
            for i in colorlist:             #stores the colors in the list
                if i not in guessCompare:
                    switch.append(i)
            guessCompare = list(guessCompare)             #turns guessCompare into a list
            guessCompare.pop(3)                    #takes out the last value in the list
            guessCompare.pop(2)                    #takes out the second last value in the list
            switch = random.sample(switch, 2)
            if feedbackCompare[0] == 'black' and feedbackCompare[1] == 'black':
                guessCompare = guessCompare + switch
            else:
                guessCompare = switch + guessCompare          #combines what's left of guessCompare and switch

            if count > 1:                   #so that it still works on the first run through
                '''if both feedback values are white or if of the previous two guesses, each had two items of feedback, then shuffle'''
                if feedbackCompare.count('white') == 2 or (len(listguess[count - 1].getFeedback()) == 2 and len(listguess[count - 2].getFeedback()) == 2): 
                    random.shuffle(guessCompare)
                    random.shuffle(guessCompare)
                
                elif len(listguess[count - 2].getFeedback()) == 3: #if the feedback went from three values to two values, then shuffle
                    random.shuffle(guessCompare)
                    random.shuffle(guessCompare)
            
            
        elif len(feedbackCompare) == 3:
            '''sequence of steps when computer has guessed three correct colors.'''
            test = 0
            for i in colorlist:
                guessCompare = list(guessCompare)
                if i not in guessCompare and test == 0:        #replaces the last item in guess with the first color in colorlist that is not already in guessCompare.
                    guessCompare.pop(3)
                    guessCompare.append(i)
                    test += 1
            if feedbackCompare.count('white') == 3:            #if it gets three whites then it shuffles the whole list.
                #guess = positioncheck(guess, listguess, count) 
                random.shuffle(guessCompare)
                random.shuffle(guessCompare)
            elif 0 < feedbackCompare.count('white') < 3:           #otherwise if it has less than three whites but more than 1 (1 black or more), it swaps the last two items.
                guessCompare[2], guessCompare[3] = guessCompare[3], guessCompare[2]
                                                            #if it has three blacks, it just swaps the last colour out and does nothing.

        elif len(feedbackCompare) == 4:
            '''sequence of steps when computer guess all colors correctly'''
            guessCompare = list(guessCompare)
            result = possibilities(guessCompare, 4)
            strgoodResults = goodPossibilities(result, listguess, count)
            
            list1 = []
            list2 = []
            for item in strgoodResults:
                list1 = item.split(", ")
                list2.append(list1)
            
            goodResults = list2
            print(goodResults)
            listguessCompare = random.sample(goodResults, 1)
            guessCompare = listguessCompare[0]
            print(guessCompare)
            
            
            # if feedbackCompare.count('white') == 4:            #if it has four whites it shuffles them
            #     random.shuffle(guessCompare)
            #     random.shuffle(guessCompare)
            # else:           # if there are 1 or 2 black it swaps the last two
            #     guessCompare[2], guessCompare[3] = guessCompare[3], guessCompare[2]
            # if count > 1: 
            #     secpreviousfeedback = listguess[count - 2].getFeedback()        #sets the feedback for the second to last guess as secpreviousfeedback
            #     previousfeedback = listguess[count - 1].getFeedback()           #sets the feedback for the last guess as previousfeedback
            #     if secpreviousfeedback.count("black") > previousfeedback.count("black"):    #if the number of blacks decreases it shuffles again.
            #         random.shuffle(guessCompare)
            #         random.shuffle(guessCompare)
            
        else:                               #if there's no feedback it picks four new colors from the unguessed colors
            switch = []                     #creates an empty list to store all colors not guessed
            for i in colorlist:             #stores the colors in the list
                if i not in guess:
                    switch.append(i)
            guessCompare = random.sample(switch, 4) 
     
        currentguess = noRepeat(guessCompare, listguess, count)                       #this makes sure that the current guess hasn't already been played
        currentguess = list(currentguess)
        return humanmastermind(colorlist, count + 1, currentguess, masterlist, listguess, window) #repeats the play, and will continue repeating until count is 10 or the computer wins


def humancodebreaker(masterlist, colorlist, count, window):                     
    '''runs when the human plays as codebreaker. The user has 10 guesses to guess the right answer.'''
    print("You can guess from the following colors: ", colorlist)
    strguess = (input("What's your guess? Please input four colors: "))         #takes in the users guess and turns it into a list
    guess = strguess.split(', ')
    
    while spellcheck(guess, colorlist) == False:                        #spellchecks the guess
        if strguess == "":
            return
        print("Oops! Make sure to input the correct spelling: ", colorlist)
        strguess = (input("What's your guess? Please input four colors: "))
        guess = strguess.split(', ')

    guessCompare = guess.copy()                                 #creates a copy of the guess for processing
    feedback = []                                               #creates an empty feeback list to be used as a parameter
    
    for g in range(4):                                          #turns each ball into an object
        guess[g] = Mainball(guess[g])
    play = Column(guess, feedback)                              #saves the guess
    play.columnPlay(guess, count, window)                       #draws each of the four balls guessed   
     
    for j in range(4):                                          #determines the feedback 
        for k in guess:
            if masterlist[j] == k.getColor() and j != k.getPosition():          #if the feedback is white it creates a white feedback object
                feedback.append(Feedbackball("white"))
            elif masterlist[j] == k.getColor() and j == k.getPosition():        #if the feedback is black it creates a black feedback object
                feedback.append(Feedbackball("black"))
    
    random.shuffle(feedback)                        #shuffles the feedback so the user can't associate it with the guess
    play.changeFeedback(feedback)                   #updates the feedback for the current guess
    play.feedbackPlay(guess, feedback, count, window)       #draws the feedback ball
    if guessCompare == masterlist:                          #tells the user they won if they guessed correctly
        print("You win!")                                                 
        return replay(colorlist, window)                                    #allows user to replay

    print("You have", 10 - count, "guesses left.")                  #determines the number of guesses left
    if count == 10 and guessCompare != masterlist:                  #if the user doesn't guess correctly in 10 guesses they lose
        print("You lose. :(")                                       
        return replay(colorlist, window)                            #allows user to replay
        

    return humancodebreaker(masterlist, colorlist, count + 1, window)               ##repeats the play, and will continue repeating until count is 10 or the user wins.


def gameplay(colorlist):   
    '''Starting point of the game. Let's the user choose between mastermind or codebreaker'''                 
    window = GraphWin("MASTERMIND", 1000, 500)        #creates a window

    human = input("Would you like to be 'mastermind' or 'codebreaker'? ")       #takes in whether the human wants to be mastermind or codebreaker
    if human == "mastermind":               #if the human is mastermind this is how the game proceeds.
        masterlist = []                     #creates an empty list to store the colors
        while len(masterlist) != 4:
            strmasterlist = input("What are your colors? ")     #takes in the masterlist
            if strmasterlist == "":             #allows the user to quit
                return print("See you next time!")
            masterlist = strmasterlist.split(', ')  
        for q in range(4):                      #turns each ball into an object
            masterlist[q] = Mainball(masterlist[q])
        masterrow = Column(masterlist, [])          #stores the masterlist
        masterrow.masterPlay(masterlist, window)        #draws the masterlist
        currentguess = random.sample(colorlist, 4)      #computer guesses randomly
        return humanmastermind(colorlist, 1, currentguess, masterlist, listguess, window)              #runs the mastermind sequence for the rest of the game


    elif human == "codebreaker":                #if the human is codebreaker this is how the game proceeds.
        mL = random.sample(colorlist, 4)        #randomly generates a masterlist
        return humancodebreaker(mL, colorlist, 1, window)   #runs the codebreaker sequence for the rest of the game
    elif human == "":                           #allows the user to quit
        return print("See you next time!")
    else:                                       #spellcheck. if the user didn't enter 'mastermind', 'codebreaker', or nothing, they are prompted again
        return gameplay(colorlist)
    
def main():
    '''sets the colors for the game and prints the intro and rules for the first time playing.'''
    testlist = ["red", "blue", "yellow", "green", "magenta", "cyan"]
    print()
    print("Hello, welcome to Mastermind! This is a game that will test the limits of your intelligence. Can you beat the genius computer?? Find out if you dare...")
    input("Press Enter to continue ")
    print("The rules of the game are: If you choose to be codebreaker, you will have 10 chances to guess the masterlist the computer has chosen.")
    print("This list will contain four colors chosen out of the following list:", testlist, ".")
    print("For each color you guess correctly but in the wrong position, you will receive a white feedback.")
    print("For each color you guess in the correct position, you will receive a black feedback.")
    print("The feedback will be presented in a random order.")
    print()
    print("If you choose to be mastermind, you will input four colors from", testlist, "and the computer will have 10 chances to guess correctly.")
    print("After each guess, give the computer feedback according to the same rules as above in a comma separated list.")
    print("Only give feedback for correct colors.")
    print("For example: white, white, black would be three correct colors with one in the right position.") 
    print()

    gameplay(testlist)  #runs gameplay to start the game

if __name__ == "__main__":
    main()

