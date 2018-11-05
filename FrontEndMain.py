from tkinter import *
import tkinter as tk
import webbrowser


def callback(event):
    webbrowser.open_new(r"https://www.ebay.com/help/home")

class Page(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = Label(self, text="Hadrian's Search")
       label.place(relx=.5, rely=.45, anchor="center")
       T = Text(self, height=1, width=30)
       T.place(relx=.5, rely=.5, anchor="center")
       T.insert(END, "Search\n")

class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       #Top box, Goes Top,Bottom,left,right line
       canvas = Canvas(self, height = root.winfo_screenheight(),width = root.winfo_screenwidth(), scrollregion=(0, 0, 1400, 1400))
       canvas.create_line(50, 50, 1300, 50)
       canvas.create_line(50, 250, 1300, 250)
       canvas.create_line(50, 250, 50, 50)
       canvas.create_line(1300, 50, 1300, 250)
       #Mid box, Goes Bottom,left,right line
       canvas.create_line(50, 450, 1300, 450)
       canvas.create_line(50, 450, 50, 250)
       canvas.create_line(1300, 450, 1300, 250)
       #Mid box, Goes Bottom,left,right line
       canvas.create_line(50, 650, 1300, 650)
       canvas.create_line(50, 650, 50, 450)
       canvas.create_line(1300, 650, 1300, 450)
       #Mid box, Goes Bottom,left,right line
       canvas.create_line(50, 850, 1300, 850)
       canvas.create_line(50, 850, 50, 650)
       canvas.create_line(1300, 850, 1300, 650)
       #Mid box, Goes Bottom,left,right line
       canvas.create_line(50, 1050, 1300, 1050)
       canvas.create_line(50, 1050, 50, 850)
       canvas.create_line(1300, 1050, 1300, 850)
       #Mid box, Goes Bottom,left,right line
       canvas.create_line(50, 1250, 1300, 1250)
       canvas.create_line(50, 1250, 50, 850)
       canvas.create_line(1300, 1250, 1300, 1050)
       canvas.place(relx=.5, rely=.5, anchor="center")
       label = Label(self, text="Watchlist")
       label.pack(side="top", fill="both", expand=True)
       label.place(relx=.5, rely=.01, anchor="center")
       scrollbar = Scrollbar(self)
       scrollbar.pack(side=RIGHT, fill=Y)
       scrollbar.config(command=canvas.yview)


class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       #Top box, Goes Top,Bottom,left,right line
       canvas = Canvas(self, height = root.winfo_screenheight(),width = root.winfo_screenwidth(), scrollregion=(0, 0, 1400, 1400))
       canvas.create_line(50, 50, 1300, 50)
       canvas.create_line(50, 250, 1300, 250)
       canvas.create_line(50, 250, 50, 50)
       canvas.create_line(1300, 50, 1300, 250)
       #Mid box, Goes Bottom,left,right line
       canvas.create_line(50, 450, 1300, 450)
       canvas.create_line(50, 450, 50, 250)
       canvas.create_line(1300, 450, 1300, 250)
       ##Mid box, Goes Bottom,left,right line
       canvas.create_line(50, 650, 1300, 650)
       canvas.create_line(50, 650, 50, 450)
       canvas.create_line(1300, 650, 1300, 450)
       #Mid box, Goes Bottom,left,right line
       canvas.create_line(50, 850, 1300, 850)
       canvas.create_line(50, 850, 50, 650)
       canvas.create_line(1300, 850, 1300, 650)
       #Mid box, Goes Bottom,left,right line
       canvas.create_line(50, 1050, 1300, 1050)
       canvas.create_line(50, 1050, 50, 850)
       canvas.create_line(1300, 1050, 1300, 850)
       #Mid box, Goes Bottom,left,right line
       canvas.create_line(50, 1250, 1300, 1250)
       canvas.create_line(50, 1250, 50, 850)
       canvas.create_line(1300, 1250, 1300, 1050)
       canvas.place(relx=.5, rely=.5, anchor="center")
       label = Label(self, text="Ignore List")
       label.pack(side="top", fill="both", expand=True)
       label.place(relx=.5, rely=.01, anchor="center")
       scrollbar = Scrollbar(self)
       scrollbar.pack(side=RIGHT, fill=Y)
       scrollbar.config(command=canvas.yview)


class Page4(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = Label(self, text="About")
       label.pack(side="top", fill="both", expand=True)
       label.place(relx=.5, rely=.005, anchor="center")
       T2 = Text(self, height=3, width=50)
       T2.place(relx=.5, rely=.5, anchor="center")
       T2.insert(END, "This is the About page where a brief explanation\n of everyone who has worked on this project and\n what they did will be explained.")

class MainView(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)
        p4 = Page4(self)

        buttonframe = Frame(self)
        container = Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = Button(buttonframe, text="Hadrian's Search", command=p1.lift)
        b2 = Button(buttonframe, text="Watchlist", command=p2.lift)
        b3 = Button(buttonframe, text="Ignore List", command=p3.lift)
        b4 = Button(buttonframe, text="Help")
        b5 = Button(buttonframe, text="About", command=p4.lift)

        b1.grid(row=0, column=0)
        b2.grid(row=0, column=4)
        b3.grid(row=0, column=5)
        b4.grid(row=0, column=6)
        b5.grid(row=0, column=7)

        p1.show()

        b4.bind("<Button-1>", callback)

if __name__ == "__main__":
    root = Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    root.mainloop()
