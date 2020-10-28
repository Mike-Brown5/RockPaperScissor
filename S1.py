from tkinter import*
import random

lcScore=0
lpScore=0
mark = {
    "rock":{"rock":0,"paper":-1,"scissors":1},
    "paper":{"rock":1,"paper":0,"scissors":-1},
    "scissors":{"rock":-1,"paper":1,"scissors":0}
    }
def res(user):
    ranNum = random.randint(0,2)
    resI = ["rock","paper","scissors"]
    cChoice = resI[ranNum]
    lChoice.config(text="Player: "+ str(user),fg="red")
    lChoice2.config(text="PC: "+ str(cChoice),fg="blue")
    results=mark[user][cChoice]

    if results ==1:
        global lpScore
        lpScore = lpScore+1
        lScore.config(text="Player: "+str(lpScore))
        result.config(text="You Win",fg="green", font=("",13))
    elif results ==-1:
        global lcScore
        lcScore = lcScore+1
        lScore2.config(text="Player: "+str(lcScore))
        result.config(text="You Lose",fg="red", font=("",13))
    else:
        result.config(text="Draw", font=("",13), fg="orange")
main = Tk()
main.title("Rock,Paper,Scissors")

l1=Label(main,text="Rock, Paper, Scissors", font=("",15))
l1.grid(row=0,sticky=N, pady=8, padx=180)

l2= Label(main,text="Select an option",font=("",10))
l2.grid(row=1,sticky=N)

lScore = Label(main,text="Player : 0",font=("",8))
lScore.grid(row=3,sticky=W)
lScore2 = Label(main,text="PC : 0",font=("",8))
lScore2.grid(row=3,sticky=E)
lChoice = Label(main)
lChoice.grid(row=4,sticky=W)
lChoice2 = Label(main)
lChoice2.grid(row=4,sticky=E)
result=Label(main,bg="white")
result.grid(row=3,sticky=N)
rock=Button(main,text="Rock",width=12,command=lambda:res("rock"),bg="black",fg="white")
rock.grid(row=5,sticky=E)
paper=Button(main,text="Paper",width=12,command=lambda:res("paper"),bg="black",fg="white")
paper.grid(row=5,sticky=N)
scissors=Button(main,text="Scissors",width=12,command=lambda:res("scissors"),bg="black",fg="white")
scissors.grid(row=5,sticky=W)
close=Button(main,text="Close", command=main.destroy, fg="white",bg="red")
close.grid(row=0,sticky=E)

main.mainloop()