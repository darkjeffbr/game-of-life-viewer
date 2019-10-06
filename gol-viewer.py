from tkinter import *
import argparse


def parseArgumentsAndGetFileName():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f','--file', dest='file_name', default='input.txt', help='File name to read the grid')
    args = parser.parse_args()
    return args.file_name

def setupWindow():
    window = Tk()
    window.title = 'Game of Life Viewer'
    window.resizable(False, False)
    return window

def readFileAsMatrix(file_name):
    data = []
    with open(file_name, 'r') as file:
#        data = file.read().replace('\n', '')
        x = 0
        for line in file:
            y = 0
            for cell in line:
                data[x][y] = cell
                y = y + 1
            x = x + 1
    return data




file_name = parseArgumentsAndGetFileName()

file_content = readFileAsMatrix(file_name)


for y in file_content:
    print(y)
#print(file_content)

"""
with open("input.txt") as fp:

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

"""
        
window = setupWindow()
window.mainloop()
