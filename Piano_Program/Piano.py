import pygame #Importing the pygame module
import sys #Importing the sys module
from tkinter import* #Importing tkinter module

pygame.init() #We start by initializing all the modules of the Pygame library

root = Tk()#We create a frame with a title
 
frame = Frame(root)#We create an additional framework
Frame(root).config(background="black")
frame.pack()#On importe le cadran

root.title('PIANO VIRTUEL')# We give a title to the window

topframe= Frame(root)# we create the frame where the notes will be displayed
topframe.pack(side = TOP)#Locate it in the window
topframe.config(background="black")#The color of the edge of the frame of the black keys is defined

#We create a frame with a window where we can write a partition inside
num1=StringVar()
txtDisplay=Entry(frame,textvariable=num1,bd=20, insertwidth=1, font=30, justify='center', width=1000,) 
txtDisplay.pack(side = TOP)

#### Creation of the 15 black keys ####

# 'Do#'
button22= Button(topframe, padx=7, pady=7, height=5, bd=8, text="Do#", bg="black", fg="white", command=lambda:jouerNote('Do#'))
button22.pack(side=LEFT)
button22=Button(topframe, state=DISABLED, height=6, width=1, padx=0, pady=0, relief=RIDGE)
button22.pack(side=LEFT)
# 'Ré#'
button23= Button(topframe, padx=7, pady=7,height=5,bd=8 , text="Ré#", bg="black", fg="white", command=lambda:jouerNote('Ré#'))
button23.pack(side=LEFT)
button23=Button(topframe, state=DISABLED, height=6, width=5, padx=0, pady=0, relief=RIDGE)
button23.pack(side=LEFT)
# 'Fa#'
button24= Button(topframe, padx=7, pady=7,height=5,bd=8 , text="Fa#", bg="black", fg="white", command=lambda:jouerNote('Fa#'))
button24.pack(side=LEFT)
button24=Button(topframe, state=DISABLED, height=6, width=1, padx=0, pady=0, relief=RIDGE)
button24.pack(side=LEFT)
# 'Sol#'
button25= Button(topframe, padx=7, pady=7,height=5,bd=8 , text="Sol#", bg="black", fg="white", command=lambda:jouerNote('Sol#'))
button25.pack(side=LEFT)
button25=Button(topframe, state=DISABLED, height=6, width=1, padx=0, pady=0, relief=RIDGE)
button25.pack(side=LEFT)
# 'La#'
button26= Button(topframe, padx=7, pady=7,height=5,bd=8 , text="La#", bg="black", fg="white", command=lambda:jouerNote('La#'))
button26.pack(side=LEFT)
button26=Button(topframe, state=DISABLED, height=6, width=5, padx=0, pady=0, relief=RIDGE)
button26.pack(side=LEFT)
# 'Do#2'
button27= Button(topframe, padx=7, pady=7,height=5,bd=8 , text="Do#", bg="black", fg="white", command=lambda:jouerNote('Do#2'))
button27.pack(side=LEFT)
button27=Button(topframe, state=DISABLED, height=6, width=1, padx=0, pady=0, relief=RIDGE)
button27.pack(side=LEFT)
# 'Ré#2'
button28= Button(topframe, padx=7, pady=7,height=5,bd=8 , text="Ré#", bg="black", fg="white", command=lambda:jouerNote('Ré#2'))
button28.pack(side=LEFT)
button28=Button(topframe, state=DISABLED, height=6, width=5, padx=0, pady=0, relief=RIDGE)
button28.pack(side=LEFT)
# 'Fa#2'
button29= Button(topframe, padx=7, pady=7,height=5,bd=8 , text="Fa#", bg="black", fg="white", command=lambda:jouerNote('Fa#2'))
button29.pack(side=LEFT)
button29=Button(topframe, state=DISABLED, height=6, width=1, padx=0, pady=0, relief=RIDGE)
button29.pack(side=LEFT)
# 'Sol#2'
button30= Button(topframe, padx=7, pady=7,height=5,bd=8 , text="Sol#", bg="black", fg="white", command=lambda:jouerNote('Sol#2'))
button30.pack(side=LEFT)
button30=Button(topframe, state=DISABLED, height=6, width=1, padx=0, pady=0, relief=RIDGE)
button30.pack(side=LEFT)
# 'La#2'
button31= Button(topframe, padx=7, pady=7,height=5,bd=8 , text="La#", bg="black", fg="white", command=lambda:jouerNote('La#2'))
button31.pack(side=LEFT)
button31=Button(topframe, state=DISABLED, height=6, width=5, padx=0, pady=0, relief=RIDGE)
button31.pack(side=LEFT)
# 'Do#3'
button32= Button(topframe, padx=7, pady=7,height=5,bd=8 , text="Do#", bg="black", fg="white", command=lambda:jouerNote('Do#3'))
button32.pack(side=LEFT)
button32=Button(topframe, state=DISABLED, height=6, width=1, padx=0, pady=0, relief=RIDGE)
button32.pack(side=LEFT)
# 'Ré#3'
button33= Button(topframe, padx=7, pady=7,height=5,bd=8 , text="Ré#", bg="black", fg="white", command=lambda:jouerNote('Ré#3'))
button33.pack(side=LEFT)
button33=Button(topframe, state=DISABLED, height=6, width=5, padx=0, pady=0, relief=RIDGE)
button33.pack(side=LEFT)
# 'Fa#3'
button34= Button(topframe, padx=7, pady=7,height=5,bd=8 , text="Fa#", bg="black", fg="white", command=lambda:jouerNote('Fa#3'))
button34.pack(side=LEFT)
button34=Button(topframe, state=DISABLED, height=6, width=1, padx=0, pady=0, relief=RIDGE)
button34.pack(side=LEFT)
# 'Sol#3'
button35= Button(topframe, padx=7, pady=7,height=5,bd=8 , text="Sol#", bg="black", fg="white", command=lambda:jouerNote('Sol#3'))
button35.pack(side=LEFT)
button35=Button(topframe, state=DISABLED, height=6, width=1, padx=0, pady=0, relief=RIDGE)
button35.pack(side=LEFT)
# 'La#3'
button36= Button(topframe, padx=7, pady=7,height=5,bd=8 , text="La#", bg="black", fg="white", command=lambda:jouerNote('La#3'))
button36.pack(side=LEFT)
button36=Button(topframe, state=DISABLED, height=6, width=1, padx=0, pady=0, relief=RIDGE)
button36.pack(side=LEFT)


#Creating a frame for the white keys
frame1=Frame(root)
frame1.pack(side=BOTTOM)

#### Creation of the 21 whites notes ####

button1=Button(frame1,padx=12, pady=12, bd=8, height=8, text="Do", fg="black", command=lambda:jouerNote('DO'))
button1.pack(side=LEFT)

button2=Button(frame1,padx=12, pady=12, bd=8, height=8, text="Ré", fg="black", command=lambda:jouerNote('RE'))
button2.pack(side=LEFT)

button3=Button(frame1,padx=12, pady=12, bd=8, height=8, text="Mi", fg="black", command=lambda:jouerNote('MI'))
button3.pack(side=LEFT) 

button4=Button(frame1,padx=12, pady=12, bd=8, height=8, text="Fa", fg="black", command=lambda:jouerNote('FA'))
button4.pack(side=LEFT)

button5=Button(frame1,padx=12, pady=12, bd=8, height=8, text="Sol", fg="black", command=lambda:jouerNote('SOL'))
button5.pack(side=LEFT)           

button6=Button(frame1,padx=12, pady=12, bd=8, height=8, text="La", fg="black", command=lambda:jouerNote('LA'))
button6.pack(side=LEFT)        

button7=Button(frame1,padx=12, pady=12, bd=8, height=8, text="Si", fg="black", command=lambda:jouerNote('SI'))
button7.pack(side=LEFT)     

button8=Button(frame1,padx=12, pady=12, bd=8, height=8, text="Do", fg="black", command=lambda:jouerNote('DO2'))
button8.pack(side=LEFT)

button9=Button(frame1,padx=12, pady=12, bd=8, height=8, text="Ré", fg="black", command=lambda:jouerNote('RE2'))
button9.pack(side=LEFT)

button10=Button(frame1,padx=12, pady=12, bd=8, height=8, text="Mi", fg="black", command=lambda:jouerNote('MI2'))
button10.pack(side=LEFT)

button11=Button(frame1,padx=12, pady=12, bd=8, height=8, text="Fa", fg="black", command=lambda:jouerNote('FA2'))
button11.pack(side=LEFT)

button12=Button(frame1,padx=12, pady=12, bd=8, height=8, text="Sol", fg="black", command=lambda:jouerNote('SOL2'))
button12.pack(side=LEFT)

button13=Button(frame1,padx=12, pady=12, bd=8, height=8, text="La", fg="black", command=lambda:jouerNote('LA2'))
button13.pack(side=LEFT)

button14=Button(frame1,padx=12, pady=12, bd=8, height=8, text="Si", fg="black", command=lambda:jouerNote('SI2'))
button14.pack(side=LEFT)

button15=Button(frame1,padx=12, pady=12, bd=8, height=8, text="Do", fg="black", command=lambda:jouerNote('DO3'))
button15.pack(side=LEFT)

button16=Button(frame1,padx=12, pady=12, bd=8, height=8, text="Ré", fg="black", command=lambda:jouerNote('RE3'))
button16.pack(side=LEFT)

button17=Button(frame1,padx=12, pady=12, bd=8, height=8, text="Mi", fg="black", command=lambda:jouerNote('MI3'))
button17.pack(side=LEFT)

button18=Button(frame1,padx=12, pady=12, bd=8, height=8, text="Fa", fg="black", command=lambda:jouerNote('FA3'))
button18.pack(side=LEFT)

button19=Button(frame1,padx=12, pady=12, bd=8, height=8, text="Sol", fg="black", command=lambda:jouerNote('SOL3'))
button19.pack(side=LEFT)

button20=Button(frame1,padx=12, pady=12, bd=8, height=8, text="La", fg="black", command=lambda:jouerNote('LA3'))
button20.pack(side=LEFT)

button21=Button(frame1,padx=12, pady=12, bd=8, height=8, text="Si", fg="black", command=lambda:jouerNote('SI3'))
button21.pack(side=LEFT)

#Importing note sounds
notes = {
    'DO': pygame.mixer.Sound("../Music_Note/final/Do1.wav"),
     'RE': pygame.mixer.Sound("../Music_Note/final/Re1.wav"),
    'MI': pygame.mixer.Sound("../Music_Note/final/Mi1.wav"),
    'FA': pygame.mixer.Sound("../Music_Note/final/Fa1.wav"),
    'SOL': pygame.mixer.Sound("../Music_Note/final/Sol1.wav"),
    'LA': pygame.mixer.Sound("../Music_Note/final/La1.wav"),
    'SI': pygame.mixer.Sound("../Music_Note/final/Si1.wav"),
    'DO2': pygame.mixer.Sound("../Music_Note/final/Do2.wav"),
    'RE2': pygame.mixer.Sound("../Music_Note/final/Re2.wav"),
    'MI2': pygame.mixer.Sound("../Music_Note/final/Mi2.wav"),
    'FA2': pygame.mixer.Sound("../Music_Note/final/Fa2.wav"),
    'SOL2': pygame.mixer.Sound("../Music_Note/final/Sol2.wav"),
    'LA2': pygame.mixer.Sound("../Music_Note/final/La2.wav"),
    'SI2': pygame.mixer.Sound("../Music_Note/final/Si2.wav"),
    'DO3': pygame.mixer.Sound("../Music_Note/final/Do3.wav"),
    'RE3': pygame.mixer.Sound("../Music_Note/final/Re3.wav"),
    'MI3': pygame.mixer.Sound("../Music_Note/final/Mi3.wav"),
    'FA3': pygame.mixer.Sound("../Music_Note/final/Fa3.wav"),
    'SOL3': pygame.mixer.Sound("../Music_Note/final/Sol3.wav"),
    'LA3': pygame.mixer.Sound("../Music_Note/final/La3.wav"),
    'SI3': pygame.mixer.Sound("../Music_Note/final/Si3.wav"),
    'Do#': pygame.mixer.Sound("../Music_Note/final/Do_1.wav"),
    'Ré#': pygame.mixer.Sound("../Music_Note/final/Re#1.wav"),
    'Fa#': pygame.mixer.Sound("../Music_Note/final/Fa_1.wav"),
    'Sol#': pygame.mixer.Sound("../Music_Note/final/Sol_1.wav"),
    'La#': pygame.mixer.Sound("../Music_Note/final/La_1.wav"),
    'Do#2': pygame.mixer.Sound("../Music_Note/final/Do_2.wav"),
    'Ré#2': pygame.mixer.Sound("../Music_Note/final/Re#2.wav"),
    'Fa#2': pygame.mixer.Sound("../Music_Note/final/Fa_2.wav"),
    'Sol#2': pygame.mixer.Sound("../Music_Note/final/Sol_2.wav"),
    'La#2': pygame.mixer.Sound("../Music_Note/final/La_2.wav"),
    'Do#3': pygame.mixer.Sound("../Music_Note/final/Do_3.wav"),
    'Ré#3': pygame.mixer.Sound("../Music_Note/final/Re#3.wav"),
    'Fa#3': pygame.mixer.Sound("../Music_Note/final/Fa_3.wav"),
    'Sol#3': pygame.mixer.Sound("../Music_Note/final/Sol_3.wav"),
    'La#3': pygame.mixer.Sound("../Music_Note/final/La_3.wav"),
}
#Function that allows to play the note
def jouerNote(note):
    s = notes[note]
    s.play()

root.mainloop()