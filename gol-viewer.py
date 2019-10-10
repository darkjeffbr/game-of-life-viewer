
from tkinter import *
import argparse
import threading
import queue
import time

class Configuration:
    def __init__(self, inputFileName, columns, rows):
        self.inputFileName = inputFileName
        self.columns = columns
        self.rows = rows
    def __str__(self):
        return "file name: " + self.inputFileName + ", columns: " + str(self.columns) + ", rows: " + str(self.rows)

class FileReader(threading.Thread):
    def __init__(self, inputFileName, queue):
        super().__init__()
        self.inputFileName = inputFileName
        self.queue = queue
        self.keepRunning = True
    
    def run(self):
        while(self.keepRunning):
            if(not self.keepRunning):
                break
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

            time.sleep(0.1)
            
    
    def stop(self):
        self.keepRunning = False

class ViewUpdater(threading.Thread):
    def __init__(self, configuration, world, queue):
        super().__init__()
        self.configuration = configuration
        self.world = world
        self.queue = queue
        self.keepRunning = True
    
    def run(self):
        while(self.keepRunning):
            if(not self.keepRunning):
                break

            fileContent = self.queue.get()
            for y in range(self.configuration.rows):
                for x in range(self.configuration.columns):
                    bg_color = "white"
                    if(fileContent[y][x] == "1"):
                        bg_color = "blue"
                    self.world[y][x].config(bg = bg_color)

            
    
    def stop(self):
        self.keepRunning = False

class ViewerWindow:

    def __init__(self, configuration):
        self.setupWindow()
        self.queue = queue.Queue()
        self.configuration = configuration
    
    def setupWindow(self):
        self.window = Tk()
        self.window.title('Game of Life Viewer')
        self.window.resizable(False, False)
        self.window.protocol("WM_DELETE_WINDOW", self.close)

    def createWorld(self):
        self.world = []
        for y in range(self.configuration.rows):
            self.world.append([])
            for x in range(self.configuration.columns):
                cell = self.createCell(x*10, y*10)
                self.world[y].append(cell);

    def updateWorld(self):

        # Start the file reading process
        # this process will write to the queue
        self.fileReader = FileReader(self.configuration.inputFileName, self.queue)
        self.fileReader.start()

        self.viewUpdater = ViewUpdater(self.configuration, self.world, self.queue)
        self.viewUpdater.start()

    def createCell(self, posX, posY):
        try:
            cell = Label(self.window, relief=GROOVE, bg = "white", width=2)
            cell.grid(row = posY, column=posX)
            return cell
        except Exception:
            pass

    def show(self):
        self.createWorld()
        self.updateWorld()
        self.window.mainloop()

    def close(self):
        self.running = False
        self.fileReader.stop()
        self.viewUpdater.stop()
        self.window.destroy()

    

def parseArgumentsAndBuildConfiguration():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f','--file', dest='file_name', default='input.txt', help='File name to read the grid')
    parser.add_argument('-c','--column', dest='columns', default=10, help='Number of columns')
    parser.add_argument('-r','--row', dest='rows', default=10, help='Number of elements per row')
    args = parser.parse_args()

    return Configuration(args.file_name, args.columns, args.rows)

if __name__ == '__main__':
    configuration = parseArgumentsAndBuildConfiguration()
    viewerWindow = ViewerWindow(configuration)
    viewerWindow.show()
