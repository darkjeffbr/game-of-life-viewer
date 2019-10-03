from tkinter import *
import random

with open("input.txt") as fp:


    window = Tk()
    window.resizable(False, False)

    for x in range(4):
    
        line = fp.readline()

        cnt = 0

        for y in line:

             print(line)

             bg_colour = "white"
             if(y == "1"):
                 bg_colour = "blue"
	
             Label(window, relief=GROOVE, bg = bg_colour, width=2).grid(row = x*10, column=cnt*10)
             cnt = cnt + 1

        

window.mainloop()
