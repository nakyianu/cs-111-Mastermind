#mastermindtxt.py
from graphics import *
import random

'''Rules: '''
'''class Mainball():
    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.diameter = 52

class Feedbackball():
    def __init__(self, color):
        self.color = color
        self.diameter = 13

class Row():
    def __init__(self, mainList, feedback):
        self.mainList = mainList
        self.feedback = feedback

    def rowPlay(self, mainList, feedback, window):
        count = 1
        center = Point(56, 56)

        for item in mainList: 
            ball = Circle(center, item.diameter/2)
            ball.draw(window)
            ball.setFill(item.color)
            count += 1
            center = Point(int(center.getX()) + item.diameter, int(center.getY()) + item.diameter)

        center = Point(50+mainList[0].diameter/8, 50+mainList[0].diameter/2)
            
        for item in feedback:
            ball = Circle(center, item.diameter/2)
            ball.draw(window)
            ball.setFill(item.color)
            center = Point(int(center.getX()) + item.diameter, int(center.getY()) + item.diameter)

red = color_rgb(255, 0, 0)
green = color_rgb(0, 255, 0)
blue = color_rgb(0, 0, 255)
yellow = color_rgb(255, 255, 0)
magenta = color_rgb(255, 0, 255)
cyan = color_rgb(0, 255, 255)
white = color_rgb(255, 255, 255)
black = color_rgb(0, 0, 0)
window = GraphWin("Test Run", 620, 620)

redball = Mainball(red, 1)
cyanball = Mainball(cyan, 2)
magentaball = Mainball(magenta, 3)
blueball = Mainball(blue, 4)
whiteball = Feedbackball(white)
blackball = Feedbackball(black)

mainlist = [redball, cyanball, magentaball, blueball]
feedbacklist = [whiteball, whiteball, blackball, blackball]

row1 = Row(mainlist, feedbacklist)
row1.rowPlay(mainlist, feedbacklist, window)
input()'''

class row():        #makes a class for each play which contains the guess and the feedback.
    def __init__(self, guess, feedback):
        self.guess = guess
        self.feedback = feedback

    def getFeedback(self):
        return self.feedback

    def getPlay(self):
        return self.guess




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

#when a row object is created, it takes the name of the next index in the list, and replaces the string at that index with the new object
listguess = ["guess1", "guess2", "guess3", "guess4", "guess5", "guess6", "guess7", "guess8", "guess9", "guess10"]

def replay(colorlist):                                              #allows user to replay
    playagain = input("Do you want to play again? Y or N: ")
    if playagain == "Y":
        play(colorlist)
    else:
        return print("Thanks for playing! See you soon.")

def humanmastermind(colorlist, count, guess, masterlist, listguess):
    '''runs when the human plays as mastermind. The computer has 10 guesses to guess the right answer. 
    The first play has already been guessed and passed in as a parameter.'''
    
    print("Masterlist: ", masterlist)                   #prints masterlist so the human doesn't need to remember it
    print("Computer guess: ", guess)                    #prints the computer guess
    print("Computer has", 10 - count, "guesses left.")  #prints the number of guesses left. 
    strfeedback = input("Input feedback: ")             #gets the feedback on the correctness of the guess from the human
    feedback = strfeedback.split(', ')                  #turns the feedback into a list

    listguess[count - 1] = row(guess, feedback)         #makes a row object after each guess

    if feedback == [""]:                    #allows the user to exit by pressing enter.
        return 
    elif feedback == ["black", "black", "black", "black"]: #if the computer guesses correctly and gets all blacks, it wins.
        print("Computer wins!")
        return replay(colorlist)            #allows user to replay
    else:
        if count == 10:                     #if the computer guess incorrectly all ten times then the humnan wins.
            print("You win!")
            return replay(colorlist)        #allows user to replay
        if len(feedback) == 2: 
            '''sequence of steps when the computer guessed two colors correctly but not necessarily in place.'''
            switch = []                     #creates an empty list to store all colors not guessed. with 6 colors to guess, this will only be 2 items long
            for i in colorlist:             #stores the colors in the list
                if i not in guess:
                    switch.append(i)
            guess = list(guess)             #turns guess into a list
            guess.pop(3)                    #takes out the last value in the list
            guess.pop(2)                    #takes out the second last value in the list
            guess = guess + switch          #combines what's left of guess and switch

            if count > 1:                   #so that it still works on the first run through
                '''if both feedback values are white or if of the previous two guesses, each had two items of feedback, then shuffle'''
                if feedback.count('white') == 2 or (len(listguess[count - 1].getFeedback()) == 2 and len(listguess[count - 2].getFeedback()) == 2): 
                    random.shuffle(guess)
                    random.shuffle(guess)
                
                elif len(listguess[count - 2].getFeedback()) == 3: #if the feedback went from three values to two values, then shuffle
                    random.shuffle(guess)
                    random.shuffle(guess)
            
            
        elif len(feedback) == 3:
            '''sequence of steps when computer has guessed three correct colors.'''
            test = 0
            for i in colorlist:
                guess = list(guess)
                if i not in guess and test == 0:        #replaces the last item in guess with the first color in colorlist that is not already in guess.
                    guess.pop(3)
                    guess.append(i)
                    test += 1
            if feedback.count('white') == 3:            #if it gets three whites then it shuffles the whole list.
                random.shuffle(guess)
                random.shuffle(guess)
            elif 0 < feedback.count('white') < 3:           #otherwise if it has less than three whites but more than 1 (1 black or more), it swaps the last two items.
                guess[2], guess[3] = guess[3], guess[2]
                                                            #if it has three blacks, it just swaps the last colour out and does nothing.

        elif len(feedback) == 4:
            '''sequence of steps when computer guess all colors correctly'''
            guess = list(guess)
            if feedback.count('white') == 4:            #if it has four whites it shuffles them
                random.shuffle(guess)
                random.shuffle(guess)
            else:           # if there are 1 or 2 black it swaps the last two
                guess[2], guess[3] = guess[3], guess[2]
            if count > 1: 
                secpreviousfeedback = listguess[count - 2].getFeedback()        #sets the feedback for the second to last guess as secpreviousfeedback
                previousfeedback = listguess[count - 1].getFeedback()           #sets the feedback for the last guess as previousfeedback
                if secpreviousfeedback.count("black") > previousfeedback.count("black"):    #if the number of blacks decreases it shuffles again.
                    random.shuffle(guess)
                    random.shuffle(guess)
            
        else:                               #if there's no feedback it picks four new colors from the unguessed colors
            switch = []                     #creates an empty list to store all colors not guessed
            for i in colorlist:             #stores the colors in the list
                if i not in guess:
                    switch.append(i)
            guess = random.sample(switch, 4) 
     
        currentguess = noRepeat(guess, listguess, count)                       #this makes sure that the current guess hasn't already been played
        return humanmastermind(colorlist, count + 1, currentguess, masterlist, listguess) #repeats the play, and will continue repeating until count is 10

def humancodebreaker(masterlist, colorlist, count):
    print("You can guess from the following colors: ", colorlist)
    strguess = (input("What's your guess? Please input four colors: "))
    guess = strguess.split(', ')
    feedback = []
    print("You guessed:", guess)
    
    if guess == "":
        return
    elif guess == masterlist:
        print("You win!")                                                 #allows user to replay
        return replay(colorlist)
    else:
        for j in range(4):
            if masterlist[j] in guess and masterlist[j] != guess[j]:
                feedback.append("white")
            elif masterlist[j] == guess[j]:
                feedback.append("black")
        
        random.shuffle(feedback)
        print("Your feedback is: ", feedback)
        print("You have", 10 - count, "guesses left.")
        if count == 10 and guess != masterlist:
            print("You lose. :(")                                       #allows user to replay
            return replay(colorlist)
            

        return humancodebreaker(masterlist, colorlist, count + 1)


def play(colorlist):
    

    human = input("Would you like to be 'mastermind' or 'codebreaker'? ")
    if human == "mastermind":
        masterlist = []
        while len(masterlist) != 4:
            strmasterlist = input("What are your colors? ")
            if strmasterlist == "":
                return print("See you next time!")
            masterlist = strmasterlist.split(', ')
        currentguess = random.sample(colorlist, 4)
        return humanmastermind(colorlist, 1, currentguess, masterlist, listguess)


    elif human == "codebreaker":
        mL = random.sample(colorlist, 4)
        return humancodebreaker(mL, colorlist, 1)
    elif human == "":
        return print("See you next time!")
    else:
        return play(colorlist)
    
def main():
   
    testlist = ["red", "blue", "yellow", "green", "magenta", "orange"]
    print()
    print("Hello, welcome to Mastermind! This is a game that will test the limits of your intelligence. Can you beat the genius computer?? Find out if you dare...")
    print()
    print("The rules of the game are: If you choose to be codebreaker, you will have 10 chances to guess the masterlist the computer has chosen.")
    print("This list will contain four colors chosen out of the following list: ", testlist, ".")
    print("For each color you guess correctly but in the wrong position, you will receive a white feedback.")
    print("For each color you guess in the correct position, you will receive a black feedback.")
    print("The feedback will be presented in a random order.")
    print()
    print("If you choose to be mastermind, you will input four colors from ", testlist, " and the computer will have 10 chances to guess correctly.")
    print("After each guess, give the computer feedback according to the same rules as above in a comma separated list.")
    print("Only give feedback for correct colors.")
    print("For example: white, white, black")
    print()

    play(testlist)

if __name__ == "__main__":
    main()