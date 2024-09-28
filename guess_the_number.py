from tkinter import *
from random import randint

root=Tk()
root.title("Guess The number")
root.geometry('450x450')


num_label= Label(root, text="Pick a number \n in between 1 to 20! \n You have only 3 chance!", font=('Arial', 30))
num_label.pack(pady=20)

def guesser():
    global attempts,num
    try:
        guess = int(guess_box.get())
    except ValueError:
        num_label.config(text="Please enter a valid number!")
        return

    if guess == num:
        num_label.config(text="Correct!")
        guess_button.config(state=DISABLED)
    elif guess < num:
        num_label.config(text="Too low guess")
    else:
        num_label.config(text="Too high guess")

    attempts += 1
    if attempts >= 3:
        num_label.config(text=f"The number was: {num}")
        guess_button.config(state=DISABLED)

def rando():
     global num, attempts
     num = randint(1, 20) 
     attempts = 0 
     guess_box.delete(0, END)  
     num_label.config(text="Pick a number \n in between 1 to 20!") 
     guess_button.config(state=NORMAL) 


guess_box = Entry(root, font=("Helvetica", 80),width=2)
guess_box.pack(pady=20)

guess_button= Button(root, text=('Submit'), command= guesser)
guess_button.pack(pady=10)

rand_button= Button(root, text="Restart ", command= rando) 
rand_button.pack(pady=20)

rando()
root.mainloop()






