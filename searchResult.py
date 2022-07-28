
from posixpath import split
import tkinter as tk
import tkinter.font as fnt

listofNames = open('listofNames.txt', 'a')
listofNames.write('Ali,Amir,Nima,Sara,Hossein,Reza')



def searchNames() :
    for i in listofNames :
        split(",")
        print(i)

win = tk.Tk()
win.title("Search")
win.geometry("300x400")
win.config(bg="#0066ff")



#Entry
userEntry = tk.Entry(justify="center")

userEntry.focus()
userEntry.place(width="200",height="50",x = "50",y = "50")



#Button
userButton = tk.Button(win,text="Search",background="yellow",fg="black",font=fnt.Font(size=20))

userButton.place(width="200",height="50",x = "50",y = "150")



#Label
userLabel = tk.Label(win,text="result",bg="#000099",fg="white",font=fnt.Font(size=20))
userLabel.place(width="200",height="50",x = "50",y = "250")






win.mainloop()


