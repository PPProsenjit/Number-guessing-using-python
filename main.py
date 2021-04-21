from tkinter import *
import random
attempts = 10
answer = random.randint(1,99)

def check_answer():
    global attempts
    global text

    attempts -= 1

    guess = int(Entry_windows.get())

    if answer == guess:
        text.set("you are win! Congratulation! "+"\n"+"Your guessing performance "+str((attempts*100)/10)+"% ")

        btn_check.pack_forget()

    elif attempts == 0:
        text.set("You are out of attempts!"+"\n"+"Your guessing performance 0% .batter luck! Try again to improve!")
        btn_check.pack_forget()

    elif guess < answer:
        text.set("Incorrect you have "+ str(attempts) +" attempts remaining - go Higher !!")

    elif guess > answer:
        text.set("Incorrect you have "+ str(attempts) +" attempts remaining - go Lower !!")
    return

root = Tk()

root.title("Guess the Number")

root.geometry("500x150")
label = Label(root, text="Guess the number between  1 to 99")
label.pack()

Entry_windows = Entry(root, width=40, borderwidth=4)
Entry_windows.pack()

btn_check = Button(root, text="check", command=check_answer)
btn_check.pack()

btn_quit = Button(root, text="Quit", command=root.destroy)
btn_quit.pack()

text = StringVar()
text.set("You have 10 attempt remaining! Good luck!")

guess_attempts = Label(root,textvariable=text)
guess_attempts.pack()

root.mainloop()