from tkinter import *
import argparse
import threading
import queue
import time

class FileReader:
    def __init__(self, inputFileName, queue):
        self.inputFileName = inputFileName
        self.queue = queue

        self.thread = threading.Thread(target=self.readFile)
        self.thread.start()
        self.keepReading = True
    
    def readFile(self):
        data = []
        with open(self.inputFileName, 'r') as file:
            x = 0
            for line in file:
                line = line.replace('\n', '')
                data.append([])
                for cell in line:
                    data[x].append(cell)
                x = x + 1
            self.queue.put(data)

        time.sleep(0.2)

        if(self.keepReading):
            pass
            #self.readFile()
    
    def stopReading(self):
        self.keepReading = False

class ViewerWindow:
    def __init__(self, inputFileName):
        self.setupWindow()
        self.queue = queue.Queue()
        self.inputFileName = inputFileName

        # Start the file reading process
        # this process will write to the queue each 0.2s
        self.fileReader = FileReader(inputFileName, self.queue)

        self.running = True
    
    def setupWindow(self):
        self.window = Tk()
        self.window.title('Game of Life Viewer')
        self.window.resizable(False, False)
        self.window.protocol("WM_DELETE_WINDOW", self.close)
        

    def refresh(self):
        fileContent = self.queue.get(True)
        print('something read')
        print(fileContent)
        y = 0
        for line in fileContent:
            x = 0
            for cell in line:
                #self.createLabel(cell, x*10, y*10)
                x += 1
            y += 1
        
        print(self.running)

        if(self.running):
            print('calling again')
            self.refresh()
        

    def show(self):
        self.window.mainloop()
        self.refresh()

    def close(self):
        self.running = False
        self.fileReader.stopReading()
        self.window.destroy()        

    def createLabel(self, labelValue, posX, posY):
        try:
            bg_colour = "white"
            if(labelValue == "1"):
                bg_colour = "blue"
            return Label(self.window, relief=GROOVE, bg = bg_colour, width=2).grid(row = posY, column=posX)
        except Exception:
            pass

def parseArgumentsAndGetFileName():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f','--file', dest='file_name', default='input.txt', help='File name to read the grid')
    args = parser.parse_args()
    return args.file_name

if __name__ == '__main__':
    fileName = parseArgumentsAndGetFileName()
    viewerWindow = ViewerWindow(fileName)
    viewerWindow.show()
