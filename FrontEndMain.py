from tkinter import *
import tkinter as tk
import webbrowser
import requests
from time import sleep


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
       #Top box, Goes Top,Bottom,left,right line
       canvas = Canvas(self, height = root.winfo_screenheight(),width = root.winfo_screenwidth(), scrollregion=(0, 0, 1400, 1400))
       canvas.create_line(50, 50, 1300, 50)
       canvas.create_line(50, 250, 1300, 250)
       canvas.create_line(50, 250, 50, 50)
       canvas.create_line(1300, 50, 1300, 250)
       #Little Box Goes Top,Bottom,left,right line
       #Need to replace rectangle with create_image
       canvas.create_rectangle(60, 60, 260, 240, fill="blue", outline = 'black')
       #Mid box, Goes Bottom,left,right line
       canvas.create_line(50, 450, 1300, 450)
       canvas.create_line(50, 450, 50, 250)
       canvas.create_line(1300, 450, 1300, 250)
       #Little Box Goes Top,Bottom,left,right line
       #Need to replace rectangle with create_image
       canvas.create_rectangle(60, 260, 260, 440, fill="blue", outline = 'black')
       #Mid box, Goes Bottom,left,right line
       canvas.create_line(50, 650, 1300, 650)
       canvas.create_line(50, 650, 50, 450)
       canvas.create_line(1300, 650, 1300, 450)
       #Little Box Goes Top,Bottom,left,right line
       #Need to replace rectangle with create_image
       canvas.create_rectangle(60, 460, 260, 640, fill="blue", outline = 'black')
       #Mid box, Goes Bottom,left,right line
       canvas.create_line(50, 850, 1300, 850)
       canvas.create_line(50, 850, 50, 650)
       canvas.create_line(1300, 850, 1300, 650)
       #Little Box Goes Top,Bottom,left,right line
       #Need to replace rectangle with create_image
       canvas.create_rectangle(60, 660, 260, 840, fill="blue", outline = 'black')
       #Mid box, Goes Bottom,left,right line
       canvas.create_line(50, 1050, 1300, 1050)
       canvas.create_line(50, 1050, 50, 850)
       canvas.create_line(1300, 1050, 1300, 850)
       #Little Box Goes Top,Bottom,left,right line
       #Need to replace rectangle with create_image
       canvas.create_rectangle(60, 860, 260, 1040, fill="blue", outline = 'black')
       #Mid box, Goes Bottom,left,right line
       canvas.create_line(50, 1250, 1300, 1250)
       canvas.create_line(50, 1250, 50, 850)
       canvas.create_line(1300, 1250, 1300, 1050)
       #Little Box Goes Top,Bottom,left,right line
       #Need to replace rectangle with create_image
       canvas.create_rectangle(60, 1060, 260, 1240, fill="blue", outline = 'black')

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
       #Price
       price1= Label(canvas, text="Price Here")
       canvas.create_window(320, 100, window=price1)
       price2= Label(canvas, text="Price Here")
       canvas.create_window(320, 300, window=price2)
       price3= Label(canvas, text="Price Here")
       canvas.create_window(320, 500, window=price3)
       price4= Label(canvas, text="Price Here")
       canvas.create_window(320, 700, window=price4)
       price5= Label(canvas, text="Price Here")
       canvas.create_window(320, 900, window=price5)
       price6= Label(canvas, text="Price Here")
       canvas.create_window(320, 1100, window=price6)
       #List Check box
       var1 = StringVar()
       box1 = Checkbutton(canvas, text="Watchlist", variable=var1)
       canvas.create_window(320, 130, window=box1)
       box2 = Checkbutton(canvas, text="Watchlist", variable=var1)
       canvas.create_window(320, 330, window=box2)
       box3 = Checkbutton(canvas, text="Watchlist", variable=var1)
       canvas.create_window(320, 530, window=box3)
       box4 = Checkbutton(canvas, text="Watchlist", variable=var1)
       canvas.create_window(320, 730, window=box4)
       box5 = Checkbutton(canvas, text="Watchlist", variable=var1)
       canvas.create_window(320, 930, window=box5)
       box6 = Checkbutton(canvas, text="Watchlist", variable=var1)
       canvas.create_window(320, 1130, window=box6)
       #Next page buttonframe#Next Page button
       nextPage = Button(canvas, text="Next Page")
       canvas.create_window(700, 1300, window=nextPage)
       #Scroll bar
       scrollbar = Scrollbar(self)
       scrollbar.pack(side=RIGHT, fill=Y, expand=False)
       scrollbar.config(command=canvas.yview)
       canvas.config(yscrollcommand = scrollbar.set)

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
       #Need to replace rectangle with create_image
       canvas.create_rectangle(60, 60, 260, 240, fill="blue", outline = 'black')
       #Mid box, Goes Bottom,left,right line
       canvas.create_line(50, 450, 1300, 450)
       canvas.create_line(50, 450, 50, 250)
       canvas.create_line(1300, 450, 1300, 250)
       #Little Box Goes Top,Bottom,left,right line
       #Need to replace rectangle with create_image
       canvas.create_rectangle(60, 260, 260, 440, fill="blue", outline = 'black')
       #Mid box, Goes Bottom,left,right line
       canvas.create_line(50, 650, 1300, 650)
       canvas.create_line(50, 650, 50, 450)
       canvas.create_line(1300, 650, 1300, 450)
       #Little Box Goes Top,Bottom,left,right line
       #Need to replace rectangle with create_image
       canvas.create_rectangle(60, 460, 260, 640, fill="blue", outline = 'black')
       #Mid box, Goes Bottom,left,right line
       canvas.create_line(50, 850, 1300, 850)
       canvas.create_line(50, 850, 50, 650)
       canvas.create_line(1300, 850, 1300, 650)
       #Little Box Goes Top,Bottom,left,right line
       #Need to replace rectangle with create_image
       canvas.create_rectangle(60, 660, 260, 840, fill="blue", outline = 'black')
       #Mid box, Goes Bottom,left,right line
       canvas.create_line(50, 1050, 1300, 1050)
       canvas.create_line(50, 1050, 50, 850)
       canvas.create_line(1300, 1050, 1300, 850)
       #Little Box Goes Top,Bottom,left,right line
       #Need to replace rectangle with create_image
       canvas.create_rectangle(60, 860, 260, 1040, fill="blue", outline = 'black')
       #Mid box, Goes Bottom,left,right line
       canvas.create_line(50, 1250, 1300, 1250)
       canvas.create_line(50, 1250, 50, 850)
       canvas.create_line(1300, 1250, 1300, 1050)
       #Little Box Goes Top,Bottom,left,right line
       #Need to replace rectangle with create_image
       canvas.create_rectangle(60, 1060, 260, 1240, fill="blue", outline = 'black')

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
       #Price
       price1= Label(canvas, text="Price Here")
       canvas.create_window(320, 100, window=price1)
       price2= Label(canvas, text="Price Here")
       canvas.create_window(320, 300, window=price2)
       price3= Label(canvas, text="Price Here")
       canvas.create_window(320, 500, window=price3)
       price4= Label(canvas, text="Price Here")
       canvas.create_window(320, 700, window=price4)
       price5= Label(canvas, text="Price Here")
       canvas.create_window(320, 900, window=price5)
       price6= Label(canvas, text="Price Here")
       canvas.create_window(320, 1100, window=price6)
       #List Check box
       var1 = StringVar()
       box1 = Checkbutton(canvas, text="Ignore list", variable=var1)
       canvas.create_window(320, 130, window=box1)
       box2 = Checkbutton(canvas, text="Ignore list", variable=var1)
       canvas.create_window(320, 330, window=box2)
       box3 = Checkbutton(canvas, text="Ignore list", variable=var1)
       canvas.create_window(320, 530, window=box3)
       box4 = Checkbutton(canvas, text="Ignore list", variable=var1)
       canvas.create_window(320, 730, window=box4)
       box5 = Checkbutton(canvas, text="Ignore list", variable=var1)
       canvas.create_window(320, 930, window=box5)
       box6 = Checkbutton(canvas, text="Ignore list", variable=var1)
       canvas.create_window(320, 1130, window=box6)
       #Next page buttonframe#Next Page button
       nextPage = Button(canvas, text="Next Page")
       canvas.create_window(700, 1300, window=nextPage)
       #Scrollbar
       scrollbar = Scrollbar(self)
       scrollbar.pack(side=RIGHT, fill=Y, expand=False)
       scrollbar.config(command=canvas.yview)
       canvas.config(yscrollcommand = scrollbar.set)

class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = Label(self, text="About")
       label.place(relx=.5, rely=.00)
       T2 = Text(self, height=3, width=50)
       T2.place(relx=.5, rely=.5, anchor="center")
       T2.insert(END, "This is the About page where a brief explanation\n of everyone who has worked on this project and\n what they did will be explained.")

class Page4(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       canvas = Canvas(self, height = root.winfo_screenheight(),width = root.winfo_screenwidth(), scrollregion=(0, 0, 1700, 1700))
       def search():
           sleep(1) # Need this to slow the changes down
           item.set(mEntry.get())
           root.update_idletasks()

       lbl = StringVar()
       label = Label(self, text="Hadrian's Search")
       canvas.create_window(700, 50, window=label)
       search1 = StringVar()
       mEntry = Entry(self, width=30,textvariable=search1)
       canvas.create_window(700, 100, window=mEntry)
       searchButton = Button(self, text="Search", command=search)
       canvas.create_window(700, 150, window=searchButton)
       #Mid box, Goes Bottom,left,right line
       canvas.create_line(50, 250, 1300, 250)
       canvas.create_line(50, 450, 1300, 450)
       canvas.create_line(50, 450, 50, 250)
       canvas.create_line(1300, 450, 1300, 250)
       #Little Box Goes Top,Bottom,left,right line
       #Need to replace rectangle with create_image
       canvas.create_rectangle(60, 260, 260, 440, fill="blue", outline = 'black')
       #Mid box, Goes Bottom,left,right line
       canvas.create_line(50, 650, 1300, 650)
       canvas.create_line(50, 650, 50, 450)
       canvas.create_line(1300, 650, 1300, 450)
       #Little Box Goes Top,Bottom,left,right line
       #Need to replace rectangle with create_image
       canvas.create_rectangle(60, 460, 260, 640, fill="blue", outline = 'black')
       #Mid box, Goes Bottom,left,right line
       canvas.create_line(50, 850, 1300, 850)
       canvas.create_line(50, 850, 50, 650)
       canvas.create_line(1300, 850, 1300, 650)
       #Little Box Goes Top,Bottom,left,right line
       #Need to replace rectangle with create_image
       canvas.create_rectangle(60, 660, 260, 840, fill="blue", outline = 'black')
       #Mid box, Goes Bottom,left,right line
       canvas.create_line(50, 1050, 1300, 1050)
       canvas.create_line(50, 1050, 50, 850)
       canvas.create_line(1300, 1050, 1300, 850)
       #Little Box Goes Top,Bottom,left,right line
       #Need to replace rectangle with create_image
       canvas.create_rectangle(60, 860, 260, 1040, fill="blue", outline = 'black')
       #Mid box, Goes Bottom,left,right line
       canvas.create_line(50, 1250, 1300, 1250)
       canvas.create_line(50, 1250, 50, 850)
       canvas.create_line(1300, 1250, 1300, 1050)
       #Little Box Goes Top,Bottom,left,right line
       #Need to replace rectangle with create_image
       canvas.create_rectangle(60, 1060, 260, 1240, fill="blue", outline = 'black')
       canvas.create_line(50, 1450, 1300, 1450)
       canvas.create_line(50, 1450, 50, 1050)
       canvas.create_line(1300, 1450, 1300, 1250)
       #Little Box Goes Top,Bottom,left,right line
       #Need to replace rectangle with create_image
       canvas.create_rectangle(60, 1260, 260, 1440, fill="blue", outline = 'black')


       canvas.place(relx=.5, rely=.5, anchor="center")
       #Item Names
       item = StringVar()
       itemName1= Label(canvas, text="Item Name Here",textvariable= item)
       canvas.create_window(320, 270, window=itemName1)
       itemName2= Label(canvas, text="Item Name Here")
       canvas.create_window(320, 470, window=itemName2)
       itemName3= Label(canvas, text="Item Name Here")
       canvas.create_window(320, 670, window=itemName3)
       itemName4= Label(canvas, text="Item Name Here")
       canvas.create_window(320, 870, window=itemName4)
       itemName5= Label(canvas, text="Item Name Here")
       canvas.create_window(320, 1070, window=itemName5)
       itemName6= Label(canvas, text="Item Name Here")
       canvas.create_window(320, 1270, window=itemName6)
       #Price
       price1= Label(canvas, text="Price Here")
       canvas.create_window(320, 300, window=price1)
       price2= Label(canvas, text="Price Here")
       canvas.create_window(320, 500, window=price2)
       price3= Label(canvas, text="Price Here")
       canvas.create_window(320, 700, window=price3)
       price4= Label(canvas, text="Price Here")
       canvas.create_window(320, 900, window=price4)
       price5= Label(canvas, text="Price Here")
       canvas.create_window(320, 1100, window=price5)
       price6= Label(canvas, text="Price Here")
       canvas.create_window(320, 1300, window=price6)
       #List Check box
       var1 = StringVar()
       box1 = Checkbutton(canvas, text="Search list", variable=var1)
       canvas.create_window(320, 330, window=box1)
       box2 = Checkbutton(canvas, text="Search list", variable=var1)
       canvas.create_window(320, 530, window=box2)
       box3 = Checkbutton(canvas, text="Search list", variable=var1)
       canvas.create_window(320, 730, window=box3)
       box4 = Checkbutton(canvas, text="Search list", variable=var1)
       canvas.create_window(320, 930, window=box4)
       box5 = Checkbutton(canvas, text="Search list", variable=var1)
       canvas.create_window(320, 1130, window=box5)
       box6 = Checkbutton(canvas, text="Search list", variable=var1)
       canvas.create_window(320, 1330, window=box6)

       #r = requests.get("http://127.0.0.1:5000/search?search_param=ball&items_per_page=2&page_number=3%22")
       #print(r)

       #Next Page button
       nextPage = Button(canvas, text="Next Page")
       canvas.create_window(700, 1500, window=nextPage)
       #Scroll bar
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

        buttonframe = Frame(self)
        container = Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = Button(buttonframe, text="Watchlist", command=p1.lift)
        b2 = Button(buttonframe, text="Ignore List", command=p2.lift)
        b3 = Button(buttonframe, text="Help")
        b4 = Button(buttonframe, text="About", command=p3.lift)
        b5 = Button(buttonframe, text="Search List", command=p4.lift)

        b1.grid(row=0, column=0)
        b2.grid(row=0, column=4)
        b3.grid(row=0, column=5)
        b4.grid(row=0, column=6)
        b5.grid(row=0, column=7)

        p4.show()

        b3.bind("<Button-1>", callback)

if __name__ == "__main__":
    root = Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    root.mainloop()
