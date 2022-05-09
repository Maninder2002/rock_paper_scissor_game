from tkinter import*
from PIL import Image,ImageTk
from random import randint


# main Window

window = Tk()
window.title("Rock Paper Scissor ")
window.configure(background="white")

# pictures

User_rock_img = ImageTk.PhotoImage(Image.open("user_rock.png"))
User_paper_img = ImageTk.PhotoImage(Image.open("user_paper.png"))
User_scissor_img = ImageTk.PhotoImage(Image.open("user_scissors.png"))
Computer_rock_img = ImageTk.PhotoImage(Image.open("computer_rock.png"))
Computer_paper_img = ImageTk.PhotoImage(Image.open("Computer_paper.png"))
Computer_scissor_img = ImageTk.PhotoImage(Image.open("Computer_scissors.png"))

# insert picures 
user_label =Label(window,image= User_scissor_img,bg="white")
comp_label =Label(window,image= Computer_scissor_img,bg="white")
comp_label.grid(row=1,column=0)
user_label.grid(row=1,column=4)

# scores 
playerscore = Label(window,text=0,font=100,bg="white",fg="black")
computerscore = Label(window,text=0,font=100,bg="white",fg="black")
computerscore.grid(row=1,column=1)
playerscore.grid(row=1,column=3)

# player indicator 
user_indicator = Label(window,font=50, text="PLAYER",bg="green",fg="white")
computer_indicator = Label(window,font=50, text="COMPUTER",bg="red",fg="white" )
user_indicator.grid(row=0,column=3)
computer_indicator.grid(row=0,column=1)
 
# win loose, tie Message
msg =Label(window,font=50,bg="white",fg="black")
msg.grid(row=3 ,column=2)

#update the message
def updatemessage(x):
    msg['text'] = x 

# update user score 

def updateuserscore():
    score=int(playerscore["text"])
    score+= 1
    playerscore["text"]= str(score)

# update computer score 
def updatecomputerscore():
    score=int(computerscore["text"])
    score+= 1
    computerscore["text"]= str(score)


# check the winner 
def checkwinner(player, computer):
    if player == computer:
        updatemessage("Its a tie!!!")
    elif player == "rock":
        if computer == "paper":
            updatemessage("You loose")
            updatecomputerscore()
        else:
            updatemessage("You Win")
            updateuserscore()
    elif player == "paper":
        if computer == "scissor":
            updatemessage("You loose")
            updatecomputerscore()
        else:
            updatemessage("You Win")
            updateuserscore()
    elif player == "scissor":
        if computer == "rock":
           updatemessage("You loose")
           updatecomputerscore()
        else:
            updatemessage("You Win")
            updateuserscore()
    else:
        pass
    





#update choices 

choices = ["rock","paper","scissor"]
def updatechoices(x):

# computer choices 
    computerchoices =  choices[randint(0,2)]
    if computerchoices =="rock":
        comp_label.configure(image=Computer_rock_img)
    elif computerchoices =="paper":
        comp_label.configure(image=Computer_paper_img)
    else:
        comp_label.configure(image=Computer_scissor_img)    



# user choices 
    if x=="rock":
        user_label.configure(image=User_rock_img)
    elif x=="paper":
        user_label.configure(image=User_paper_img)    
    else:
        user_label.configure(image=User_scissor_img)

    checkwinner(x,computerchoices)


# buttons 
rock=Button(window,width=20,height=2,text="ROCK",bg="red",fg="black",command = lambda:updatechoices("rock")) 
paper=Button(window,width=20,height=2,text="PAPER",bg="Green",fg="black",command = lambda:updatechoices("paper"))
scissors=Button(window,width=20,height=2,text="SCISSORS",bg="BLUE",fg="black",command = lambda:updatechoices("scissor"))
rock.grid(row=2,column=1)
paper.grid(row=2,column=2)
scissors.grid(row=2,column=3)

window.mainloop()
