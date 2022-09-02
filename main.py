from tkinter import *
import pandas
import random
from decimal import Decimal

cps_count = 0
wrong_input = 0
right_input = 0
running = True

data = pandas.read_csv("sampletxt.csv", on_bad_lines='skip')
l = random.choice(data["Sampletext"])

def start(event):
    sampletext.config(text=l)
    window.unbind("<Button-1>")
    txt.config(state="normal")
    count_down(60)

def check(event):
    input = txt.get(1.0, "end-1c")

    if not sampletext.cget('text').startswith(input):
        txt.config(fg="red")
    else:
        txt.config(fg="green")

def count_down(count):
    global cps_count
    input = txt.get(1.0, "end-1c")
    space_removed = input.replace(" ", "")
    for word in space_removed:
        cps_count += len(word)

    try:
        formatted_cps_count = "{:.2f}".format(cps_count / (60 - count))

    except ZeroDivisionError:
        formatted_cps_count = Decimal('0.00')


    if  sampletext.cget('text') == input or count == 0:
        count = 0
        timer_label.config(text=f'Timer:\n{count}')
        txt.config(state='disabled')
        wrong_words()
        sampletext.config(
            text=f'Your score is {formatted_cps_count}CPS\nWrong Characters:{wrong_input}\nRight Characters:{right_input}')


    elif count > 0:
        window.after(1000, count_down, count - 1)
        timer_label.config(text=f'Timer:\n{count}')
        speed_label.config(text=f'Speed:\n{formatted_cps_count} CPS')


def wrong_words():
    global right_input
    global wrong_input
    global l
    user_input = txt.get(1.0, "end-1c")
    print(user_input)
    string1_words = user_input.split()
    print(string1_words)
    string2_words = (l.split())

    try:
        for i in range(len(string1_words)):
            if string1_words[i] == string2_words[i]:
                right_input += 1
            elif string1_words[i] != string2_words[i]:
                wrong_input += 1
    except IndexError:
        pass

def restart():
    global running
    global cps_count, wrong_input, right_input, string, l
    running = True
    window.destroy()
    cps_count = 0
    wrong_input = 0
    right_input = 0
    l = random.choice(data["Sampletext"])

def quit():
    window.destroy()


while running:
    running = False
    window = Tk()
    window.title("Typing Speed Test")
    window.resizable(width=False, height=False)
    window.minsize(width=820, height=600)
    window.config(pady=10)

    title = Label(text="Typing Speed Test", font=("Ariel", 24, "bold"), fg="blue")
    title.grid(row=0, column=1, columnspan=3)

    timer_label = Label(text="Timer:\n00 Secs", font=("Helvetica", 24))
    timer_label.grid(row=1, column=0, padx=15, pady=15)

    speed_label = Label(text="Speed: \n0.00 CPS", font=("Helvetica", 24))
    speed_label.grid(row=2, column=0, padx=20, pady=20)

    sampletext = Label(text="Click the text box to start typing", font=("Ariel", 15, "bold"), fg="black", wraplength=500, justify="center", height=10)
    sampletext.grid(row=1, column=1, columnspan=3, padx=20, pady=20)

    txt = Text(window, height=5, width=50, wrap=WORD, font=("Ariel", 10))
    txt.grid(row=2, column=1, padx=10, pady=10, columnspan=3)
    txt.config(state="disabled")
    txt.bind("<KeyPress>", check)
    window.bind("<Button-1>", start)

    reset_button = Button(window, text="Reset", font=("Ariel", 10, "bold"), command=restart)
    reset_button.grid(row=4, column=2, padx=10, pady=10, sticky="W")

    quit = Button(window, text="Quit", font=("Ariel", 10, "bold"), command=quit)
    quit.grid(row=4, column=3, padx=10, pady=10, sticky="W")



    window.mainloop()




