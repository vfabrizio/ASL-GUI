from tkinter import *
import random
from PIL import Image, ImageTk
from DataProcessing import *
import inspect

class ASLGame(Frame):
    global canvasWidth
    canvasWidth = 150
    global canvasHeight
    canvasHeight = 600
    global scale
    scale = 80
    
    def __init__(self):
        Frame.__init__(self)
        self.master.title("ASL Game")
        self.master.minsize(width=500,height=500)
        self.grid()

        self.__dataPane = Frame(self)
        self.__dataPane.grid(row=0, column=0)
        
        self.__mode1Frame = Frame(self)
        self.__mode2Frame = Frame(self)
##        self.__mode3Frame = Frame(self)

        self.__dp = DataProcessing()
        self.__whole = self.__dp.getWholeSignDict()
        self.__NumLtr = self.__dp.getNumLtrDict()

        self.__homeButton = Button(self.__dataPane, text="Home",\
                                   command=self.__home)
        self.__welcome = Label(self.__dataPane, text="Choose a mode")
        self.__mode1Button = Button(self.__dataPane, text="Mode 1",\
                                    command=self.__mode1)
        self.__mode2Button = Button(self.__dataPane, text="Mode 2",\
                                    command=self.__mode2)
##        self.__mode3Button = Button(self.__dataPane, text="Mode 3",\
##                                    command=self.__mode3)

        self.__homeButton.grid(row=1, column=1)
        self.__welcome.grid(row=2, column=2)
        self.__mode1Button.grid(row=3, column=1)
        self.__mode2Button.grid(row=3, column=2)
        #self.__mode3Button.grid(row=3, column=3)

        mainloop()

    def __home(self):
        self.__canvas.destroy()
        self.__mode1Frame.grid_forget()
        self.__mode2Frame.grid_forget()
        #self.__mode3Frame.grid_forget()
        self.__dataPane.grid()
        if len(self.__partial) == 0:
            self.__finished.grid_forget()
        self.__dp.resetPartialSignDict()

    def __mode1(self):
        self.__dataPane.grid_forget()
        self.__mode1Frame.grid(row=0,column=0)

        self.__options = self.__dp.generateChoices()
        self.__partial = self.__dp.getPartialSignDict()

        #print(self.__options)

        self.__choice1 = self.__options[0]
        self.__choice2 = self.__options[1]
        self.__choice3 = self.__options[2]
        self.__choice4 = self.__options[3]

        self.__img1 = self.__whole[self.__choice1]
        self.__img2 = self.__whole[self.__choice2]
        self.__img3 = self.__whole[self.__choice3]
        self.__img4 = self.__whole[self.__choice4]
        
        self.__homeButton = Button(self.__mode1Frame, text="Home",\
                                   command=self.__home)
        self.__question = Label(self.__mode1Frame,\
                            text="Choose the hand that corresponds to the letter")
        self.__homeButton.grid(row=0, column=0)
        self.__question.grid(row=1, column=1)
        
        self.__canvas = Canvas(width=canvasWidth, height=canvasHeight)
        self.__canvas.grid(row=2,column=0)

        self.__letter = Label(self.__canvas, text=self.__NumLtr[self.__dp.getAnswer()], font=(None, 48))
        self.__letter.grid(row=1,column=0)

        self.__var = IntVar()
        
        self.__photo = ImageTk.PhotoImage(self.__img1)
        self.__rb1 = Radiobutton(self.__canvas, image=self.__photo,\
                                 variable=self.__var, value=self.__choice1)
        self.__rb1.grid(row=1,column=1)

        self.__photo2 = ImageTk.PhotoImage(self.__img2)
        self.__rb2 = Radiobutton(self.__canvas, image=self.__photo2,\
                                 variable=self.__var, value=self.__choice2)
        self.__rb2.grid(row=2,column=1)

        self.__photo3 = ImageTk.PhotoImage(self.__img3)
        self.__rb3 = Radiobutton(self.__canvas, image=self.__photo3,\
                                 variable=self.__var, value=self.__choice3)
        self.__rb3.grid(row=1,column=2)

        self.__photo4 = ImageTk.PhotoImage(self.__img4)
        self.__rb4 = Radiobutton(self.__canvas, image=self.__photo4,\
                                 variable=self.__var, value=self.__choice4)
        self.__rb4.grid(row=2,column=2)

        currentMode = "mode1"
        
        self.__submit = Button(self.__canvas, text="Submit",\
                               command= lambda: self.__answer(currentMode))
        self.__submit.grid(row=3,column=0)

        
    def __mode2(self):
        self.__dataPane.grid_forget()
        self.__mode2Frame.grid(row=0,column=0)

        self.__options = self.__dp.generateChoices()
        self.__partial = self.__dp.getPartialSignDict()

        self.__homeButton = Button(self.__mode2Frame, text="Home",\
                                   command=self.__home)
        self.__question = Label(self.__mode2Frame,\
                            text="Choose the letter that corresponds to the hand")
        self.__homeButton.grid(row=0, column=0)
        self.__question.grid(row=1, column=1)
        
        self.__canvas = Canvas(width=canvasWidth, height=canvasHeight)
        self.__canvas.grid(row=2,column=0)

        self.__hand = ImageTk.PhotoImage(self.__whole[self.__dp.getAnswer()])
        self.__handLabel = Label(self.__canvas, image=self.__hand)
        self.__handLabel.grid(row=0,column=0)

        self.__var = IntVar()

        self.__rb1 = Radiobutton(self.__canvas, text=self.__NumLtr[self.__options[0]],\
                                 variable=self.__var, value=self.__options[0])
        self.__rb1.grid(row=0,column=2)

        self.__rb2 = Radiobutton(self.__canvas, text=self.__NumLtr[self.__options[1]],\
                                 variable=self.__var, value=self.__options[1])
        self.__rb2.grid(row=1,column=2)

        self.__rb3 = Radiobutton(self.__canvas, text=self.__NumLtr[self.__options[2]],\
                                 variable=self.__var, value=self.__options[2])
        self.__rb3.grid(row=0,column=3)

        self.__rb4 = Radiobutton(self.__canvas, text=self.__NumLtr[self.__options[3]],\
                                 variable=self.__var, value=self.__options[3])
        self.__rb4.grid(row=1,column=3)

        currentMode = "mode2"
        
        self.__submit = Button(self.__canvas, text="Submit",\
                               command=lambda:self.__answer(currentMode))
        self.__submit.grid(row=3,column=0)

##    def __mode3(self):
##        self.__dataPane.grid_forget()
##        self.__mode3Frame.grid(row=0,column=0)
##        
##        self.__homeButton = Button(self.__mode3Frame, text="Home",\
##                                   command=self.__home)
##        self.__placeHolder = Label(self.__mode3Frame,\
##                                   text="Timed mode: Soon to come", font=(None, 20))
##
##        #set up as place holders until mode3 calls answer and loop
##        self.__canvas = Canvas(width=canvasWidth, height=canvasHeight)
##        self.__finished = Label(self.__mode3Frame)
##
##        self.__homeButton.grid(row=0, column=0)
##        self.__placeHolder.grid(row=1, column=1)

    def __answer(self, currentMode):
        answer = self.__dp.getAnswer()
        selection = self.__var.get()
        if selection == answer:
            printAnswer = Label(self.__canvas, text="Correct!")
        else:
            if currentMode == "mode1":
                self.__picAnswer = ImageTk.PhotoImage(self.__whole[answer])
                printAnswer = Label(self.__canvas, image=self.__picAnswer)
            elif currentMode == "mode2":
                printAnswer = Label(self.__canvas, text="Correct answer is: " + self.__NumLtr[self.__dp.getAnswer()])
        #print(answer)
        printAnswer.grid(row=3,column=1)
        self.__nextButton = Button(self.__canvas, text="Next",\
                                   command=lambda:self.__loop(currentMode))
        self.__nextButton.grid(row=3,column=2)
        

    def __loop(self, currentMode):
        self.__canvas.grid_forget()
        if len(self.__partial) != 0:
            if currentMode == "mode1":
                self.__mode1()
                self.__var.set(-1)
                self.__finished = Label(self.__mode1Frame)
                self.__finished.grid(row=5,column=5)
            elif currentMode == "mode2":
                self.__mode2()
                self.__var.set(-1)
                self.__finished = Label(self.__mode2Frame)
                self.__finished.grid(row=5,column=5)
                
        else:
            if currentMode == "mode1":
                self.__dp.resetPartialSignDict()
                self.__finished = Label(self.__mode1Frame, text="YOU FINISHED! CONGRATS")
                self.__finished.grid(row=3,column=1)
            if currentMode == "mode2":
                self.__dp.resetPartialSignDict()
                self.__finished = Label(self.__mode2Frame, text="YOU FINISHED! CONGRATS")
                self.__finished.grid(row=3,column=1)

def main():
    ASLGame()

main()
        
