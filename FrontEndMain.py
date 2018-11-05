from tkinter import *
import tkinter as tk
import webbrowser


def callback(event):
    webbrowser.open_new(r"https://www.ebay.com/help/home")

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="Hadrian's Search")
       label.place(relx=.5, rely=.45, anchor="center")
       T = tk.Text(self, height=1, width=30)
       T.place(relx=.5, rely=.5, anchor="center")
       T.insert(END, "Search\n")

class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="Watchlist")
       label.place(relx=.5, rely=.45, anchor="center")
       ##Top box, Goes bottom,Top,left,right line
       canvas = Canvas(self, width=550, height=620)
       canvas.create_line(100, 320, 550, 320)
       canvas.create_line(100, 170, 550, 170)
       canvas.create_line(100, 170, 100, 320)
       canvas.create_line(550, 170, 550, 320)
       ##Mid box, Goes Right,left,bottom line
       canvas.create_line(550, 320, 550, 470)
       canvas.create_line(100, 320, 100, 470)
       canvas.create_line(100, 470, 550, 470)
       ##Mid box, Goes Right,left,bottom line
       canvas.create_line(550, 470, 550, 620)
       canvas.create_line(100, 470, 100, 620)
       canvas.create_line(100, 620, 550, 620)
       canvas.place(relx=.5, rely=.3, anchor="center")


class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="Ignore List")
       label.place(relx=.5, rely=.45, anchor="center")
       ##Top box, Goes bottom,Top,left,right line
       canvas = Canvas(self, width=550, height=620)
       canvas.create_line(100, 320, 550, 320)
       canvas.create_line(100, 170, 550, 170)
       canvas.create_line(100, 170, 100, 320)
       canvas.create_line(550, 170, 550, 320)
       ##Mid box, Goes Right,left,bottom line
       canvas.create_line(550, 320, 550, 470)
       canvas.create_line(100, 320, 100, 470)
       canvas.create_line(100, 470, 550, 470)
       ##Mid box, Goes Right,left,bottom line
       canvas.create_line(550, 470, 550, 620)
       canvas.create_line(100, 470, 100, 620)
       canvas.create_line(100, 620, 550, 620)
       canvas.place(relx=.5, rely=.3, anchor="center")


class Page4(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="About")
       label.pack(side="top", fill="both", expand=True)
       T2 = tk.Text(self, height=3, width=50)
       T2.place(relx=.5, rely=.5, anchor="center")
       T2.insert(END, "This is the About page where a brief explanation\n of everyone who has worked on this project and\n what they did will be explained.")

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)
        p4 = Page4(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Hadrian's Search", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Watchlist", command=p2.lift)
        b3 = tk.Button(buttonframe, text="Ignore List", command=p3.lift)
        b4 = tk.Button(buttonframe, text="Help")
        b5 = tk.Button(buttonframe, text="About", command=p4.lift)

        b1.grid(row=0, column=0)
        b2.grid(row=0, column=4)
        b3.grid(row=0, column=5)
        b4.grid(row=0, column=6)
        b5.grid(row=0, column=7)

        p1.show()

        b4.bind("<Button-1>", callback)

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    root.mainloop()
