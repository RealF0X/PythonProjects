from tkinter import *
from turtle import width
win=Tk()
win.title("Login")
win.geometry('300x300')
win.config(bg="lightblue")
win.resizable(False,False)

#UserName
#UserName Entry
userName = Entry(win ,relief="sunken", bd=3)
userName.place(width=150 , height=50 , x=120 , y=20)
#UserName Label
labelName = Label(win , text="UserName" , relief="raised" , bd=2 , bg="green" )
labelName.place(width=80 , height=50 , x=20 , y=20)


#Password
#Password Entry
userPassword = Entry(win , relief="sunken")
userPassword.place(width=150 , height=50 , x=120 , y=100)
#Password Label
labelName = Label(win , text="Password" , relief="raised" , bd=2 , bg="green" )
labelName.place(width=80 , height=50 , x=20 , y=100)


#Buttons
#Login Button
loginButton = Button(win , text="Login" , bg="Red" , bd=4 , relief="groove")
loginButton.place(width=150 , height=50 , x=120 , y=200)
#Reset Buttton
resetButton = Button(win , text="Reset" , bg="Red" , bd=4 , relief="groove")
resetButton.place(width=80 , height=50 , x=20 , y=200)

win.mainloop()