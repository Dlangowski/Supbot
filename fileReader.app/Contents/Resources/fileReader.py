import sys
import os
if sys.version_info[0] == 2:
    from Tkinter import *
else:
    from tkinter import *

def resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    elif __file__:
        application_path = os.path.dirname(__file__)
    return os.path.join(application_path, relative_path)

class App(Frame): #a frame is a type of frame in tkinter, this inherits eveyrthing the frame does

    def __init__(self, master):

        Frame.__init__(self, master)
        self.pack() #pack places things in sequental order
        self.master.title("NAMELESS BOTS, SUPBOT V1.0 BETA")
        self.master.config(menu=Menu(self.master))
        Label(master, text="Hello", justify='left').pack(pady=2)

if __name__ == "__main__":
    root = Tk()
    app = App(root)
    app.pack()
    app.mainloop()

