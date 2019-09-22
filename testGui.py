from tkinter import *


class Application(Frame):
    def say_hi(self):
        print("hi there, everyone!")

    def toEat(self):
        print("Let us go to eat!!")

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack({"side": "left"})

        self.toeatNo = Button(self)
        self.toeatNo["text"] = "toeatNo",
        self.toeatNo["command"] = self.toEat
        self.toeatNo.pack({"side": "right"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()


root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()