import requests
from tkinter import *
import json
import os
top = Tk()  
top.geometry("500x500")
top.title('Please share your response')
#usernameLabel = Label(top, text="User Id")
#username = StringVar()
#usernameEntry = Entry(top, textvariable=username)
#usernameLabel.place(relx = 0.3, rely = 0.2,anchor = CENTER)
#usernameEntry.place(relx = 0.5, rely = 0.2,anchor = CENTER)
def good():
    user=28  #temporary
    myobj = {'mood': 'good','user':user}
    myobj = json.dumps(myobj)
    newurl ='http://127.0.0.1:8000/blog/howday/'
    r = requests.post(newurl,data={'res':myobj})
    #print(os.getlogin())
def bad():
    user=28  #temporary
    myobj = {'mood': 'bad','user':user}
    myobj = json.dumps(myobj)
    newurl ='http://127.0.0.1:8000/blog/howday/'
    r = requests.post(newurl,data={'res':myobj})
    #print(os.getlogin())  this will give the name of the logined user so we will set the name of user comp according to the DB
    
l = Label(top, text = "How was your day")
l.config(font=("Courier", 24))
l.place(relx = 0.5, rely = 0.3,anchor = CENTER) 
b1 = Button(top,text = "GOOD",bg="green",command =good,activeforeground = "green",activebackground = "darkgreen",pady=10,height="4",width="10")  
b2 = Button(top,text = "BAD",bg="red",command =bad,activeforeground = "red",activebackground = "darkred",pady=10,height="4",width="10")  
b1.place(relx = 0.4, rely = 0.5, anchor = CENTER)  
b2.place(relx = 0.6, rely = 0.5, anchor = CENTER)
top.mainloop()
