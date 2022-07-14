from cProfile import label
from dataclasses import replace
from distutils.command.build import build
from tkinter import *
from turtle import color

def sumFunc(x,y) :
    print(x+y)




win = Tk()
win.title("Calculater")
win.geometry("500x500")
win.configure(bg = "grey")
win.resizable(False,False)


#Math Buttons
#Plus Button
buttonPlus = Button(win , text="+" , bd=2, bg="purple" , relief="groove", )
buttonPlus.place(width=80 , height=75 , x=275 , y=305)

#Minus Button
buttonMinus = Button(win , text="-" , bd=2, bg="purple" , relief="groove")
buttonMinus.place(width=80 , height=75 , x=275 , y=225)

#Multiply Button
buttonMultiply = Button(win , text="x" , bd=2, bg="purple" , relief="groove")
buttonMultiply.place(width=80 , height=75 , x=275 , y=145)

#Divide Button
buttonDivided = Button(win , text="/" , bd=2, bg="purple" , relief="groove")
buttonDivided.place(width=80 , height=75 , x=360 , y=145)

#Equal Button
buttonEqual = Button(win , text="=" , bd=2, bg="purple" , relief="groove")
buttonEqual.place(width=80 , height=155 , x=360 , y=225)


#Label For Output
labelOutput = Label(win , bd=4 , relief="sunken")
labelOutput.place(width=420 , height=120 , x=20 , y=5)


#Numbers Buttons
button1 = Button(win , text="1" , bd=2, bg="green" , relief="raised")
button1.place(width=80 , height=75 , x=20 , y=305)

button2 = Button(win , text="2" , bd=2, bg="green" , relief="raised")
button2.place(width=80 , height=75 , x=105 , y=305)

button3 = Button(win , text="3" , bd=2, bg="green" , relief="raised")
button3.place(width=80 , height=75 , x=190 , y=305)


button4 = Button(win , text="4" , bd=2, bg="green" , relief="raised")
button4.place(width=80 , height=75 , x=20 , y=225)


button5 = Button(win , text="5" , bd=2, bg="green" , relief="raised")
button5.place(width=80 , height=75 , x=105 , y=225)


button6 = Button(win , text="6" , bd=2, bg="green" , relief="raised")
button6.place(width=80 , height=75 , x=190 , y=225)

button7 = Button(win , text="7" , bd=2, bg="green" , relief="raised")
button7.place(width=80 , height=75 , x=20 , y=145)


button8 = Button(win , text="8" , bd=2, bg="green" , relief="raised")
button8.place(width=80 , height=75 , x=105 , y=145)


button9 = Button(win , text="9" , bd=2, bg="green" , relief="raised")
button9.place(width=80 , height=75 , x=190 , y=145)


button1 = Button(win , text="0" , bd=2, bg="green" , relief="raised")
button1.place(width=160 , height=80 , x=20 , y=390)












win.mainloop()