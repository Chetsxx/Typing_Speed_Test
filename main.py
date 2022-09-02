from tkinter import *
import csv
import pandas
import keyboard
import random

cps_count = 0
wrong_input = 0
right_input = 0
string = ''

data = pandas.read_csv("sampletxt.csv", on_bad_lines='skip')
l = random.choice(data["Sampletext"])

def start(event):
    sampletext.config(text=l)
    window.unbind("<Button-1>")
    txt.config(state="normal")
    count_down(60)

def check(event):
    global string
    input = txt.get(1.0, "end-1c")
    try:
        string += input[-1]
    except IndexError:
        pass
    if keyboard.is_pressed("backspace"):
        string = string[:-2]

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
        formatted_cps_count = 0


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
        speed_label.config(text=f'Speed: \n{formatted_cps_count}CPS')


def wrong_words():
    global string
    global right_input
    global wrong_input
    global l
    user_input = (string[1:])
    string1_words = (user_input.split())
    string2_words = (l.split())

    for i in range(len(string1_words)):
        if string1_words[i] == string2_words[i]:
            right_input += 1
        elif string1_words[i] != string2_words[i]:
            wrong_input += 1

# def restart():
#     global cps_count, wrong_input, right_input, string, l
#     cps_count = 0
#     wrong_input = 0
#     right_input = 0
#     string = ''
#     l = random.choice(data["Sampletext"])
#



    # if wrong_input == " ":
#     pass
# else:
#     txt.delete(wrong_input)
#     txt.insert('end', wrong_input, 'bad')



        
# game_on = True
# string = ''
#
# while game_on:
#     connect = input("ADD: ")
#     string += connect
#     print(string)



window = Tk()
window.title("Typing Speed Test")
window.minsize(width=800, height=600)
window.config(pady=20)

title = Label(text="Typing Speed Test", font=("Ariel", 24, "bold"), fg="blue")
title.grid(row=0, column=2)

timer_label = Label(text="Timer:\n00 Secs", font=("Helvetica", 24))
timer_label.grid(row=1, column=0, padx=10, pady=10)

speed_label = Label(text="Speed: \n0.00 CPS", font=("Helvetica", 24))
speed_label.grid(row=2, column=0, padx=20, pady=20)

sampletext = Label(text="Click the text box to start typing", font=("Ariel", 15, "bold"), fg="black", wraplength=500, justify="center", height=10)
sampletext.grid(row=1, column=1, columnspan=3, padx=10, pady=10)

txt = Text(window, height=5, width=50, wrap=WORD)
txt.tag_configure('bad', foreground="red")
txt.grid(row=2, column=1, padx=10, pady=10, columnspan=3)
txt.config(state="disabled")
txt.bind("<KeyPress>", check)
window.bind("<Button-1>", start)

reset_button = Button(window, text="Reset")
reset_button.grid(row=4, column=2, padx=10, pady=10, sticky="W")



window.mainloop()



