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
       def search(self):
           subprocess.call([""], shell=True)

       searchButton = Button(self, text="Search", command=search)
       searchButton.place(relx=.5, rely=.55, anchor="center")

       label = Label(self, text="Hadrian's Search")
       label.place(relx=.5, rely=.45, anchor="center")
       search1 = StringVar()
       mEntry = Entry(self, width=30,textvariable=search1)
       mEntry.place(relx=.5, rely=.5, anchor="center")

class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       #Top box, Goes Top,Bottom,left,right line
       canvas = Canvas(self, height = root.winfo_screenheight(),width = root.winfo_screenwidth(), scrollregion=(0, 0, 1400, 1400))
       canvas.create_line(50, 50, 1300, 50)
       canvas.create_line(50, 250, 1300, 250)
       canvas.create_line(50, 250, 50, 50)
       canvas.create_line(1300, 50, 1300, 250)
       #Little Box Goes Top,Bottom,left,right line
       canvas.create_line(60, 60, 260, 60)
       canvas.create_line(60, 240, 260, 240)
       canvas.create_line(60, 240, 60, 60)
       canvas.create_line(260, 60, 260, 240)
       #Mid box, Goes Bottom,left,right line
       canvas.create_line(50, 450, 1300, 450)
       canvas.create_line(50, 450, 50, 250)
       canvas.create_line(1300, 450, 1300, 250)
       #Little Box Goes Top,Bottom,left,right line
       canvas.create_line(60, 260, 260, 260)
       canvas.create_line(60, 440, 260, 440)
       canvas.create_line(60, 260, 60, 440)
       canvas.create_line(260, 260, 260, 440)
       #Mid box, Goes Bottom,left,right line
       canvas.create_line(50, 650, 1300, 650)
       canvas.create_line(50, 650, 50, 450)
       canvas.create_line(1300, 650, 1300, 450)
       #Little Box Goes Top,Bottom,left,right line
       canvas.create_line(60, 460, 260, 460)
       canvas.create_line(60, 640, 260, 640)
       canvas.create_line(60, 460, 60, 640)
       canvas.create_line(260, 460, 260, 640)
       #Mid box, Goes Bottom,left,right line
       canvas.create_line(50, 850, 1300, 850)
       canvas.create_line(50, 850, 50, 650)
       canvas.create_line(1300, 850, 1300, 650)
       #Little Box Goes Top,Bottom,left,right line
       canvas.create_line(60, 660, 260, 660)
       canvas.create_line(60, 840, 260, 840)
       canvas.create_line(60, 660, 60, 840)
       canvas.create_line(260, 660, 260, 840)
       #Mid box, Goes Bottom,left,right line
       canvas.create_line(50, 1050, 1300, 1050)
       canvas.create_line(50, 1050, 50, 850)
       canvas.create_line(1300, 1050, 1300, 850)
       #Little Box Goes Top,Bottom,left,right line
       canvas.create_line(60, 860, 260, 860)
       canvas.create_line(60, 1040, 260, 1040)
       canvas.create_line(60, 860, 60, 1040)
       canvas.create_line(260, 860, 260, 1040)
       #Mid box, Goes Bottom,left,right line
       canvas.create_line(50, 1250, 1300, 1250)
       canvas.create_line(50, 1250, 50, 850)
       canvas.create_line(1300, 1250, 1300, 1050)
       #Little Box Goes Top,Bottom,left,right line
       canvas.create_line(60, 1060, 260, 1060)
       canvas.create_line(60, 1240, 260, 1240)
       canvas.create_line(60, 1060, 60, 1240)
       canvas.create_line(260, 1060, 260, 1240)

       canvas.place(relx=.5, rely=.5, anchor="center")
       label = Label(self, text="Watchlist")
       label.place(relx=.5, rely=.00)
       #Item Names
       itemName1= Label(canvas, text="Item Name Here")
       canvas.create_window(320, 70, window=itemName1)
       itemName2= Label(canvas, text="Item Name Here")
       canvas.create_window(320, 270, window=itemName2)
       itemName3= Label(canvas, text="Item Name Here")
       canvas.create_window(320, 470, window=itemName3)
       itemName4= Label(canvas, text="Item Name Here")
       canvas.create_window(320, 670, window=itemName4)
       itemName5= Label(canvas, text="Item Name Here")
       canvas.create_window(320, 870, window=itemName5)
       itemName6= Label(canvas, text="Item Name Here")
       canvas.create_window(320, 1070, window=itemName6)

       scrollbar = Scrollbar(self)
       scrollbar.pack(side=RIGHT, fill=Y, expand=False)
       scrollbar.config(command=canvas.yview)
       canvas.config(yscrollcommand = scrollbar.set)

class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       #Top box, Goes Top,Bottom,left,right line
       canvas = Canvas(self, height = root.winfo_screenheight(),width = root.winfo_screenwidth(), scrollregion=(0, 0, 1400, 1400))
       canvas.create_line(50, 50, 1300, 50)
       canvas.create_line(50, 250, 1300, 250)
       canvas.create_line(50, 250, 50, 50)
       canvas.create_line(1300, 50, 1300, 250)
       #Little Box Goes Top,Bottom,left,right line
       canvas.create_line(60, 60, 260, 60)
       canvas.create_line(60, 240, 260, 240)
       canvas.create_line(60, 240, 60, 60)
       canvas.create_line(260, 60, 260, 240)
       #Mid box, Goes Bottom,left,right line
       canvas.create_line(50, 450, 1300, 450)
       canvas.create_line(50, 450, 50, 250)
       canvas.create_line(1300, 450, 1300, 250)
       #Little Box Goes Top,Bottom,left,right line
       canvas.create_line(60, 260, 260, 260)
       canvas.create_line(60, 440, 260, 440)
       canvas.create_line(60, 260, 60, 440)
       canvas.create_line(260, 260, 260, 440)
       #Mid box, Goes Bottom,left,right line
       canvas.create_line(50, 650, 1300, 650)
       canvas.create_line(50, 650, 50, 450)
       canvas.create_line(1300, 650, 1300, 450)
       #Little Box Goes Top,Bottom,left,right line
       canvas.create_line(60, 460, 260, 460)
       canvas.create_line(60, 640, 260, 640)
       canvas.create_line(60, 460, 60, 640)
       canvas.create_line(260, 460, 260, 640)
       #Mid box, Goes Bottom,left,right line
       canvas.create_line(50, 850, 1300, 850)
       canvas.create_line(50, 850, 50, 650)
       canvas.create_line(1300, 850, 1300, 650)
       #Little Box Goes Top,Bottom,left,right line
       canvas.create_line(60, 660, 260, 660)
       canvas.create_line(60, 840, 260, 840)
       canvas.create_line(60, 660, 60, 840)
       canvas.create_line(260, 660, 260, 840)
       #Mid box, Goes Bottom,left,right line
       canvas.create_line(50, 1050, 1300, 1050)
       canvas.create_line(50, 1050, 50, 850)
       canvas.create_line(1300, 1050, 1300, 850)
       #Little Box Goes Top,Bottom,left,right line
       canvas.create_line(60, 860, 260, 860)
       canvas.create_line(60, 1040, 260, 1040)
       canvas.create_line(60, 860, 60, 1040)
       canvas.create_line(260, 860, 260, 1040)
       #Mid box, Goes Bottom,left,right line
       canvas.create_line(50, 1250, 1300, 1250)
       canvas.create_line(50, 1250, 50, 850)
       canvas.create_line(1300, 1250, 1300, 1050)
       #Little Box Goes Top,Bottom,left,right line
       canvas.create_line(60, 1060, 260, 1060)
       canvas.create_line(60, 1240, 260, 1240)
       canvas.create_line(60, 1060, 60, 1240)
       canvas.create_line(260, 1060, 260, 1240)

       canvas.place(relx=.5, rely=.5, anchor="center")
       label = Label(self, text="Ignore List")
       label.place(relx=.5, rely=.00)
       #Item Names
       itemName1= Label(canvas, text="Item Name Here")
       canvas.create_window(320, 70, window=itemName1)
       itemName2= Label(canvas, text="Item Name Here")
       canvas.create_window(320, 270, window=itemName2)
       itemName3= Label(canvas, text="Item Name Here")
       canvas.create_window(320, 470, window=itemName3)
       itemName4= Label(canvas, text="Item Name Here")
       canvas.create_window(320, 670, window=itemName4)
       itemName5= Label(canvas, text="Item Name Here")
       canvas.create_window(320, 870, window=itemName5)
       itemName6= Label(canvas, text="Item Name Here")
       canvas.create_window(320, 1070, window=itemName6)

       scrollbar = Scrollbar(self)
       scrollbar.pack(side=RIGHT, fill=Y, expand=False)
       scrollbar.config(command=canvas.yview)
       canvas.config(yscrollcommand = scrollbar.set)

class Page4(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = Label(self, text="About")
       label.place(relx=.5, rely=.00)
       T2 = Text(self, height=3, width=50)
       T2.place(relx=.5, rely=.5, anchor="center")
       T2.insert(END, "This is the About page where a brief explanation\n of everyone who has worked on this project and\n what they did will be explained.")

class Page5(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       #Top box, Goes Top,Bottom,left,right line
       canvas = Canvas(self, height = root.winfo_screenheight(),width = root.winfo_screenwidth(), scrollregion=(0, 0, 1400, 1400))
       canvas.create_line(50, 50, 1300, 50)
       canvas.create_line(50, 250, 1300, 250)
       canvas.create_line(50, 250, 50, 50)
       canvas.create_line(1300, 50, 1300, 250)
       #Little Box Goes Top,Bottom,left,right line
       canvas.create_line(60, 60, 260, 60)
       canvas.create_line(60, 240, 260, 240)
       canvas.create_line(60, 240, 60, 60)
       canvas.create_line(260, 60, 260, 240)
       #Mid box, Goes Bottom,left,right line
       canvas.create_line(50, 450, 1300, 450)
       canvas.create_line(50, 450, 50, 250)
       canvas.create_line(1300, 450, 1300, 250)
       #Little Box Goes Top,Bottom,left,right line
       canvas.create_line(60, 260, 260, 260)
       canvas.create_line(60, 440, 260, 440)
       canvas.create_line(60, 260, 60, 440)
       canvas.create_line(260, 260, 260, 440)
       #Mid box, Goes Bottom,left,right line
       canvas.create_line(50, 650, 1300, 650)
       canvas.create_line(50, 650, 50, 450)
       canvas.create_line(1300, 650, 1300, 450)
       #Little Box Goes Top,Bottom,left,right line
       canvas.create_line(60, 460, 260, 460)
       canvas.create_line(60, 640, 260, 640)
       canvas.create_line(60, 460, 60, 640)
       canvas.create_line(260, 460, 260, 640)
       #Mid box, Goes Bottom,left,right line
       canvas.create_line(50, 850, 1300, 850)
       canvas.create_line(50, 850, 50, 650)
       canvas.create_line(1300, 850, 1300, 650)
       #Little Box Goes Top,Bottom,left,right line
       canvas.create_line(60, 660, 260, 660)
       canvas.create_line(60, 840, 260, 840)
       canvas.create_line(60, 660, 60, 840)
       canvas.create_line(260, 660, 260, 840)
       #Mid box, Goes Bottom,left,right line
       canvas.create_line(50, 1050, 1300, 1050)
       canvas.create_line(50, 1050, 50, 850)
       canvas.create_line(1300, 1050, 1300, 850)
       #Little Box Goes Top,Bottom,left,right line
       canvas.create_line(60, 860, 260, 860)
       canvas.create_line(60, 1040, 260, 1040)
       canvas.create_line(60, 860, 60, 1040)
       canvas.create_line(260, 860, 260, 1040)
       #Mid box, Goes Bottom,left,right line
       canvas.create_line(50, 1250, 1300, 1250)
       canvas.create_line(50, 1250, 50, 850)
       canvas.create_line(1300, 1250, 1300, 1050)
       #Little Box Goes Top,Bottom,left,right line
       canvas.create_line(60, 1060, 260, 1060)
       canvas.create_line(60, 1240, 260, 1240)
       canvas.create_line(60, 1060, 60, 1240)
       canvas.create_line(260, 1060, 260, 1240)

       canvas.place(relx=.5, rely=.5, anchor="center")
       label = Label(self, text="Search List")
       label.place(relx=.5, rely=.00)
       #Item Names
       itemName1= Label(canvas, text="Item Name Here")
       canvas.create_window(320, 70, window=itemName1)
       itemName2= Label(canvas, text="Item Name Here")
       canvas.create_window(320, 270, window=itemName2)
       itemName3= Label(canvas, text="Item Name Here")
       canvas.create_window(320, 470, window=itemName3)
       itemName4= Label(canvas, text="Item Name Here")
       canvas.create_window(320, 670, window=itemName4)
       itemName5= Label(canvas, text="Item Name Here")
       canvas.create_window(320, 870, window=itemName5)
       itemName6= Label(canvas, text="Item Name Here")
       canvas.create_window(320, 1070, window=itemName6)

       scrollbar = Scrollbar(self)
       scrollbar.pack(side=RIGHT, fill=Y, expand=False)
       scrollbar.config(command=canvas.yview)
       canvas.config(yscrollcommand = scrollbar.set)

class MainView(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)
        p4 = Page4(self)
        p5 = Page5(self)

        buttonframe = Frame(self)
        container = Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p5.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = Button(buttonframe, text="New Search", command=p1.lift)
        b2 = Button(buttonframe, text="Watchlist", command=p2.lift)
        b3 = Button(buttonframe, text="Ignore List", command=p3.lift)
        b4 = Button(buttonframe, text="Help")
        b5 = Button(buttonframe, text="About", command=p4.lift)
        b6 = Button(buttonframe, text="Search List", command=p5.lift)

        b1.grid(row=0, column=0)
        b2.grid(row=0, column=4)
        b3.grid(row=0, column=5)
        b4.grid(row=0, column=6)
        b5.grid(row=0, column=7)
        b6.grid(row=0, column=9)

        p1.show()

        b4.bind("<Button-1>", callback)

if __name__ == "__main__":
    root = Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    root.mainloop()
