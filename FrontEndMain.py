from tkinter import *
import webbrowser
import requests
import json
import array as arr
import os
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
        label = Label(self, text="About")
        label.place(relx=.5, rely=.00)
        T2 = Text(self, height=3, width=50)
        T2.place(relx=.5, rely=.5, anchor="center")
        T2.insert(END, "This is the About page where a brief explanation\n of everyone who has worked on this project and\n what they did will be explained.")

k = 0
path = os.getcwd()
watch_path = os.path.join(path, "watch_list.txt")
num_lines = sum(1 for line in open(watch_path))
n = (num_lines/5)
i=0
pageNum=1
class Page2(Page):
    print(int(n))
    def updateWList(self):
        sleep(1) # Need this to slow the changes down
        global pageNum
        global i
        item = self.mEntry.get()
        root.update_idletasks()
        try:
            json_data = requests.get("http://127.0.0.1:5000/search?search_param="+item+"&items_per_page=6&page_number="+str(pageNum)).json()
            print(json_data)
            firstPrice = json_data['0']['price']
            firstTitle = json_data['0']['title']
            firstID = json_data['0']['itemId']
            firstShipping = json_data['0']['shippingCost']['shipToLocations']
            firstCountry = json_data['0']['country']
            firstImage = json_data['0']['image_url']
            secondPrice = json_data['1']['price']
            secondTitle = json_data['1']['title']
            secondID = json_data['1']['itemId']
            secondShipping = json_data['1']['shippingCost']['shipToLocations']
            secondCountry = json_data['1']['country']
            secondImage = json_data['1']['image_url']
            thirdPrice = json_data['2']['price']
            thirdTitle = json_data['2']['title']
            thirdID = json_data['2']['itemId']
            thirdShipping = json_data['2']['shippingCost']['shipToLocations']
            thirdCountry = json_data['2']['country']
            thirdImage = json_data['2']['image_url']
            fourthPrice = json_data['3']['price']
            fourthTitle = json_data['3']['title']
            fourthID = json_data['3']['itemId']
            fourthShipping = json_data['3']['shippingCost']['shipToLocations']
            fourthCountry = json_data['3']['country']
            fourthImage = json_data['3']['image_url']
            fifthPrice = json_data['4']['price']
            fifthTitle = json_data['4']['title']
            fifthID = json_data['4']['itemId']
            fifthShipping = json_data['4']['shippingCost']['shipToLocations']
            fifthCountry = json_data['4']['country']
            fifthImage = json_data['4']['image_url']
            sixthPrice = json_data['5']['price']
            sixthTitle = json_data['5']['title']
            sixthID = json_data['5']['itemId']
            sixthShipping = json_data['5']['shippingCost']['shipToLocations']
            sixthCountry = json_data['5']['country']
            sixthImage = json_data['5']['image_url']
        except:
            print("Connection refused")

        #Put delete stuff here
        if(self.var1.get()):
            data1 = {
            'title': firstTitle,
            'price': firstPrice,
            'shipping': firstShipping,
            'itemId': firstID,
            'country': firstCountry,
            'image_url': firstImage
            }
            ignoreItems[int(i)] = data1
            print(ignoreItems[int(i)])
            i=i+1
        if(self.var2.get()):
            data2 = {
            'title': secondTitle,
            'price': secondPrice,
            'shipping': secondShipping,
            'itemId': secondID,
            'country': secondCountry,
            'image_url': secondImage
            }
            ignoreItems[int(i)] = data2
            print(ignoreItems[int(i)])
            i=i+1
        if(self.var3.get()):
            data3 = {
            'title': thirdTitle,
            'price': thirdPrice,
            'shipping': thirdShipping,
            'itemId': thirdID,
            'country': thirdCountry,
            'image_url': thirdImage
            }
            ignoreItems[int(i)] = data3
            print(ignoreItems[int(i)])
            i=i+1
        if(self.var4.get()):
            data4 = {
            'title': fourthTitle,
            'price': fourthPrice,
            'shipping': fourthShipping,
            'itemId': fourthID,
            'country': fourthCountry,
            'image_url': fourthImage
            }
            ignoreItems[int(i)] = data4
            print(ignoreItems[int(i)])
            i=i+1
        if(self.var5.get()):
            data5 = {
            'title': fifthTitle,
            'price': fifthPrice,
            'shipping': fifthShipping,
            'itemId': fifthID,
            'country': fifthCountry,
            'image_url': fifthImage
            }
            ignoreItems[int(i)] = data5
            print(ignoreItems[int(i)])
            i=i+1
        if(self.var6.get()):
            data6 = {
            'title': sixthTitle,
            'price': sixthPrice,
            'shipping': sixthShipping,
            'itemId': sixthID,
            'country': sixthCountry,
            'image_url': sixthImage
            }
            ignoreItems[int(i)] = data6
            print(ignoreItems[int(i)])
            i=i+1
    def wListNext(self):
        global n
        self.labelChange.set("Watchlist")
        rget = requests.get("http://127.0.0.2:5000/order66").json()
        print(n)
        print(rget)
        if(int(n) >= 7):
            if(int(n)==7):
                self.priceOf1.set(rget['item1']['price_no_shipping'])
                self.titleOf1.set(rget['item1']['title'])
                self.priceOf2.set("")
                self.titleOf2.set("")
                self.priceOf3.set("")
                self.titleOf3.set("")
                self.priceOf4.set("")
                self.titleOf4.set("")
                self.priceOf5.set("")
                self.titleOf5.set("")
                self.priceOf6.set("")
                self.titleOf6.set("")
            if(int(n)==8):
                self.priceOf1.set(rget['item1']['price_no_shipping'])
                self.titleOf1.set(rget['item1']['title'])
                self.priceOf2.set(rget['item2']['price_no_shipping'])
                self.titleOf2.set(rget['item2']['title'])
                self.priceOf3.set("")
                self.titleOf3.set("")
                self.priceOf4.set("")
                self.titleOf4.set("")
                self.priceOf5.set("")
                self.titleOf5.set("")
                self.priceOf6.set("")
                self.titleOf6.set("")
            if(int(n)==9):
                self.priceOf1.set(rget['item1']['price_no_shipping'])
                self.titleOf1.set(rget['item1']['title'])
                self.priceOf2.set(rget['item2']['price_no_shipping'])
                self.titleOf2.set(rget['item2']['title'])
                self.priceOf3.set(rget['item3']['price_no_shipping'])
                self.titleOf3.set(rget['item3']['title'])
                self.priceOf4.set("")
                self.titleOf4.set("")
                self.priceOf5.set("")
                self.titleOf5.set("")
                self.priceOf6.set("")
                self.titleOf6.set("")
            if(int(n)==10):
                self.priceOf1.set(rget['item1']['price_no_shipping'])
                self.titleOf1.set(rget['item1']['title'])
                self.priceOf2.set(rget['item2']['price_no_shipping'])
                self.titleOf2.set(rget['item2']['title'])
                self.priceOf3.set(rget['item3']['price_no_shipping'])
                self.titleOf3.set(rget['item3']['title'])
                self.priceOf4.set(rget['item4']['price_no_shipping'])
                self.titleOf4.set(rget['item4']['title'])
                self.priceOf5.set("")
                self.titleOf5.set("")
                self.priceOf6.set("")
                self.titleOf6.set("")
            if(int(n)==11):
                self.priceOf1.set(rget['item1']['price_no_shipping'])
                self.titleOf1.set(rget['item1']['title'])
                self.priceOf2.set(rget['item2']['price_no_shipping'])
                self.titleOf2.set(rget['item2']['title'])
                self.priceOf3.set(rget['item3']['price_no_shipping'])
                self.titleOf3.set(rget['item3']['title'])
                self.priceOf4.set(rget['item4']['price_no_shipping'])
                self.titleOf4.set(rget['item4']['title'])
                self.priceOf5.set(rget['item5']['price_no_shipping'])
                self.titleOf5.set(rget['item5']['title'])
                self.priceOf6.set("")
                self.titleOf6.set("")
            if(int(n)>=12):
                self.priceOf1.set(rget['item1']['price_no_shipping'])
                self.titleOf1.set(rget['item1']['title'])
                self.priceOf2.set(rget['item2']['price_no_shipping'])
                self.titleOf2.set(rget['item2']['title'])
                self.priceOf3.set(rget['item3']['price_no_shipping'])
                self.titleOf3.set(rget['item3']['title'])
                self.priceOf4.set(rget['item4']['price_no_shipping'])
                self.titleOf4.set(rget['item4']['title'])
                self.priceOf5.set(rget['item5']['price_no_shipping'])
                self.titleOf5.set(rget['item5']['title'])
                self.priceOf6.set(rget['item6']['price_no_shipping'])
                self.titleOf6.set(rget['item6']['title'])
    def showWList(self):
        global n
        path = os.getcwd()
        watch_path = os.path.join(path, "watch_list.txt")
        num_lines = sum(1 for line in open(watch_path))
        n = (num_lines/5)
        print(n)
        self.labelChange.set("Watchlist")
        rget = requests.get("http://127.0.0.2:5000/order66").json()
        print(n)
        print(rget)
        #for x in range(1, int(n+1)):
        if(int(n)==1):
            self.priceOf1.set(rget['item1']['price_no_shipping'])
            self.titleOf1.set(rget['item1']['title'])
            self.priceOf2.set("")
            self.titleOf2.set("")
            self.priceOf3.set("")
            self.titleOf3.set("")
            self.priceOf4.set("")
            self.titleOf4.set("")
            self.priceOf5.set("")
            self.titleOf5.set("")
            self.priceOf6.set("")
            self.titleOf6.set("")
        if(int(n)==2):
            self.priceOf1.set(rget['item1']['price_no_shipping'])
            self.titleOf1.set(rget['item1']['title'])
            self.priceOf2.set(rget['item2']['price_no_shipping'])
            self.titleOf2.set(rget['item2']['title'])
            self.priceOf3.set("")
            self.titleOf3.set("")
            self.priceOf4.set("")
            self.titleOf4.set("")
            self.priceOf5.set("")
            self.titleOf5.set("")
            self.priceOf6.set("")
            self.titleOf6.set("")
        if(int(n)==3):
            self.priceOf1.set(rget['item1']['price_no_shipping'])
            self.titleOf1.set(rget['item1']['title'])
            self.priceOf2.set(rget['item2']['price_no_shipping'])
            self.titleOf2.set(rget['item2']['title'])
            self.priceOf3.set(rget['item3']['price_no_shipping'])
            self.titleOf3.set(rget['item3']['title'])
            self.priceOf4.set("")
            self.titleOf4.set("")
            self.priceOf5.set("")
            self.titleOf5.set("")
            self.priceOf6.set("")
            self.titleOf6.set("")
        if(int(n)==4):
            self.priceOf1.set(rget['item1']['price_no_shipping'])
            self.titleOf1.set(rget['item1']['title'])
            self.priceOf2.set(rget['item2']['price_no_shipping'])
            self.titleOf2.set(rget['item2']['title'])
            self.priceOf3.set(rget['item3']['price_no_shipping'])
            self.titleOf3.set(rget['item3']['title'])
            self.priceOf4.set(rget['item4']['price_no_shipping'])
            self.titleOf4.set(rget['item4']['title'])
            self.priceOf5.set("")
            self.titleOf5.set("")
            self.priceOf6.set("")
            self.titleOf6.set("")
        if(int(n)==5):
            self.priceOf1.set(rget['item1']['price_no_shipping'])
            self.titleOf1.set(rget['item1']['title'])
            self.priceOf2.set(rget['item2']['price_no_shipping'])
            self.titleOf2.set(rget['item2']['title'])
            self.priceOf3.set(rget['item3']['price_no_shipping'])
            self.titleOf3.set(rget['item3']['title'])
            self.priceOf4.set(rget['item4']['price_no_shipping'])
            self.titleOf4.set(rget['item4']['title'])
            self.priceOf5.set(rget['item5']['price_no_shipping'])
            self.titleOf5.set(rget['item5']['title'])
            self.priceOf6.set("")
            self.titleOf6.set("")
        if(int(n)>=6):
            self.priceOf1.set(rget['item1']['price_no_shipping'])
            self.titleOf1.set(rget['item1']['title'])
            self.priceOf2.set(rget['item2']['price_no_shipping'])
            self.titleOf2.set(rget['item2']['title'])
            self.priceOf3.set(rget['item3']['price_no_shipping'])
            self.titleOf3.set(rget['item3']['title'])
            self.priceOf4.set(rget['item4']['price_no_shipping'])
            self.titleOf4.set(rget['item4']['title'])
            self.priceOf5.set(rget['item5']['price_no_shipping'])
            self.titleOf5.set(rget['item5']['title'])
            self.priceOf6.set(rget['item6']['price_no_shipping'])
            self.titleOf6.set(rget['item6']['title'])

        self.var1.set(0)
        self.var2.set(0)
        self.var3.set(0)
        self.var4.set(0)
        self.var5.set(0)
        self.var6.set(0)

    def addToWList(self):
        sleep(1) # Need this to slow the changes down
        global pageNum
        global n
        item = self.mEntry.get()
        root.update_idletasks()
        try:
            json_data = requests.get("http://127.0.0.1:5000/search?search_param="+item+"&items_per_page=6&page_number="+str(pageNum)).json()
            firstPrice = json_data['0']['price']
            firstTitle = json_data['0']['title']
            firstID = json_data['0']['itemId']
            firstShipping = json_data['0']['shippingCost']['shipToLocations']
            firstCountry = json_data['0']['country']
            secondPrice = json_data['1']['price']
            secondTitle = json_data['1']['title']
            secondID = json_data['1']['itemId']
            secondShipping = json_data['1']['shippingCost']['shipToLocations']
            secondCountry = json_data['1']['country']
            thirdPrice = json_data['2']['price']
            thirdTitle = json_data['2']['title']
            thirdID = json_data['2']['itemId']
            thirdShipping = json_data['2']['shippingCost']['shipToLocations']
            thirdCountry = json_data['2']['country']
            fourthPrice = json_data['3']['price']
            fourthTitle = json_data['3']['title']
            fourthID = json_data['3']['itemId']
            fourthShipping = json_data['3']['shippingCost']['shipToLocations']
            fourthCountry = json_data['3']['country']
            fifthPrice = json_data['4']['price']
            fifthTitle = json_data['4']['title']
            fifthID = json_data['4']['itemId']
            fifthShipping = json_data['4']['shippingCost']['shipToLocations']
            fifthCountry = json_data['4']['country']
            sixthPrice = json_data['5']['price']
            sixthTitle = json_data['5']['title']
            sixthID = json_data['5']['itemId']
            sixthShipping = json_data['5']['shippingCost']['shipToLocations']
            sixthCountry = json_data['5']['country']
        except:
            print("Connection refused")

        if(self.var1.get()):
            data1 = {
            'title': firstTitle,
            'price': firstPrice,
            'shipping': firstShipping,
            'itemId': firstID,
            'country': firstCountry
            }
            rput1 =requests.put("http://127.0.0.2:5000/order66",data1)
            print(rput1)
            n=n+1
        if(self.var2.get()):
            data2 = {
            'title': secondTitle,
            'price': secondPrice,
            'shipping': secondShipping,
            'itemId': secondID,
            'country': secondCountry
            }
            rput2 =requests.put("http://127.0.0.2:5000/order66",data2)
            print(rput2)
            n=n+1
        if(self.var3.get()):
            data3 = {
            'title': thirdTitle,
            'price': thirdPrice,
            'shipping': thirdShipping,
            'itemId': thirdID,
            'country': thirdCountry
            }
            rput3 =requests.put("http://127.0.0.2:5000/order66",data3)
            print(rput3)
            n=n+1
        if(self.var4.get()):
            data4 = {
            'title': fourthTitle,
            'price': fourthPrice,
            'shipping': fourthShipping,
            'itemId': fourthID,
            'country': fourthCountry
            }
            rput4 =requests.put("http://127.0.0.2:5000/order66",data4)
            print(rput4)
            n=n+1
        if(self.var5.get()):
            data5 = {
            'title': fifthTitle,
            'price': fifthPrice,
            'shipping': fifthShipping,
            'itemId': fifthID,
            'country': fifthCountry
            }
            rput5 =requests.put("http://127.0.0.2:5000/order66",data5)
            print(rput5)
            n=n+1
        if(self.var6.get()):
            data6 = {
            'title': sixthTitle,
            'price': sixthPrice,
            'shipping': sixthShipping,
            'itemId': sixthID,
            'country': sixthCountry
            }
            rput6 =requests.put("http://127.0.0.2:5000/order66",data6)
            print(rput6)
            n=n+1
    def search(self):
        self.labelChange.set("Search")
        sleep(1) # Need this to slow the changes down
        global pageNum
        item = self.mEntry.get()
        root.update_idletasks()
        try:
            json_data = requests.get("http://127.0.0.1:5000/search?search_param="+item+"&items_per_page=6&page_number="+str(pageNum)).json()
            print(json_data)
            firstPrice = json_data['0']['price']
            firstTitle = json_data['0']['title']
            firstImage = json_data['0']['image_url']
            self.priceOf1.set(firstPrice)
            self.titleOf1.set(firstTitle)
            #self.image1 = Image.open(firstImage)
            secondPrice = json_data['1']['price']
            secondTitle = json_data['1']['title']
            secondImage = json_data['1']['image_url']
            self.priceOf2.set(secondPrice)
            self.titleOf2.set(secondTitle)
            thirdPrice = json_data['2']['price']
            thirdTitle = json_data['2']['title']
            thirdImage = json_data['2']['image_url']
            self.priceOf3.set(thirdPrice)
            self.titleOf3.set(thirdTitle)
            fourthPrice = json_data['3']['price']
            fourthTitle = json_data['3']['title']
            fourthImage = json_data['3']['image_url']
            self.priceOf4.set(fourthPrice)
            self.titleOf4.set(fourthTitle)
            fifthPrice = json_data['4']['price']
            fifthTitle = json_data['4']['title']
            fifthImage = json_data['4']['image_url']
            self.priceOf5.set(fifthPrice)
            self.titleOf5.set(fifthTitle)
            sixthPrice = json_data['5']['price']
            sixthTitle = json_data['5']['title']
            firstImage = json_data['5']['image_url']
            self.priceOf6.set(sixthPrice)
            self.titleOf6.set(sixthTitle)
        except:
            print("Connection refused")
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        canvas = Canvas(self, height = root.winfo_screenheight(),width = root.winfo_screenwidth(), scrollregion=(0, 0, 1700, 1700))

        def next():
            global pageNum
            pageNum=pageNum+1
            self.var1.set(0)
            self.var2.set(0)
            self.var3.set(0)
            self.var4.set(0)
            self.var5.set(0)
            self.var6.set(0)
            self.search()

        def prev():
            global pageNum
            pageNum=pageNum-1
            self.var1.set(0)
            self.var2.set(0)
            self.var3.set(0)
            self.var4.set(0)
            self.var5.set(0)
            self.var6.set(0)
            self.search()

        def updateList():
            self.showList()
            self.addToIList()

        label = Label(self, text="Hadrian's Search")
        canvas.create_window(700, 50, window=label)
        #Mid box, Goes Bottom,left,right line
        canvas.create_line(50, 250, 1300, 250)
        canvas.create_line(50, 450, 1300, 450)
        canvas.create_line(50, 450, 50, 250)
        canvas.create_line(1300, 450, 1300, 250)
        #Little Box Goes Top,Bottom,left,right line
        #Need to replace rectangle with create_image
        #self.image1 = PhotoImage()
        #canvas.create_image(160, 160, image=self.image1)
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
        #Search/list label
        self.labelChange=StringVar()
        label2 = Label(canvas, text="Search", textvariable=self.labelChange)
        canvas.create_window(700,200, window=label2)
        #Item Names
        self.titleOf1=StringVar()
        self.titleOf2=StringVar()
        self.titleOf3=StringVar()
        self.titleOf4=StringVar()
        self.titleOf5=StringVar()
        self.titleOf6=StringVar()
        self.itemName1= Label(canvas, text="Item Name Here", textvariable=self.titleOf1)
        canvas.create_window(320, 270, window=self.itemName1)
        itemName2= Label(canvas, text="Item Name Here", textvariable=self.titleOf2)
        canvas.create_window(320, 470, window=itemName2)
        itemName3= Label(canvas, text="Item Name Here", textvariable=self.titleOf3)
        canvas.create_window(320, 670, window=itemName3)
        itemName4= Label(canvas, text="Item Name Here", textvariable=self.titleOf4)
        canvas.create_window(320, 870, window=itemName4)
        itemName5= Label(canvas, text="Item Name Here", textvariable=self.titleOf5)
        canvas.create_window(320, 1070, window=itemName5)
        itemName6= Label(canvas, text="Item Name Here", textvariable=self.titleOf6)
        canvas.create_window(320, 1270, window=itemName6)
        #Price
        self.cat=StringVar()
        self.priceOf1=StringVar()
        self.priceOf2=StringVar()
        self.priceOf3=StringVar()
        self.priceOf4=StringVar()
        self.priceOf5=StringVar()
        self.priceOf6=StringVar()
        price1= Label(canvas, text="Price Here", textvariable=self.priceOf1)
        canvas.create_window(320, 300, window=price1)
        price2= Label(canvas, text="Price Here", textvariable=self.priceOf2)
        canvas.create_window(320, 500, window=price2)
        price3= Label(canvas, text="Price Here", textvariable=self.priceOf3)
        canvas.create_window(320, 700, window=price3)
        price4= Label(canvas, text="Price Here", textvariable=self.priceOf4)
        canvas.create_window(320, 900, window=price4)
        price5= Label(canvas, text="Price Here", textvariable=self.priceOf5)
        canvas.create_window(320, 1100, window=price5)
        price6= Label(canvas, text="Price Here", textvariable=self.priceOf5)
        canvas.create_window(320, 1300, window=price6)
        #WatchList Check box
        self.var1 = IntVar()
        self.var2 = IntVar()
        self.var3 = IntVar()
        self.var4 = IntVar()
        self.var5 = IntVar()
        self.var6 = IntVar()
        box1 = Checkbutton(canvas, text="Watch list", variable=self.var1)
        canvas.create_window(320, 330, window=box1)
        box2 = Checkbutton(canvas, text="Watch list", variable=self.var2)
        canvas.create_window(320, 530, window=box2)
        box3 = Checkbutton(canvas, text="Watch list", variable=self.var3)
        canvas.create_window(320, 730, window=box3)
        box4 = Checkbutton(canvas, text="Watch list", variable=self.var4)
        canvas.create_window(320, 930, window=box4)
        box5 = Checkbutton(canvas, text="Watch list", variable=self.var5)
        canvas.create_window(320, 1130, window=box5)
        box6 = Checkbutton(canvas, text="Watch list", variable=self.var6)
        canvas.create_window(320, 1330, window=box6)
        #Ignore list check box
        box7 = Checkbutton(canvas, text="Ignore list")
        canvas.create_window(320, 350, window=box7)
        box8 = Checkbutton(canvas, text="Ignore list")
        canvas.create_window(320, 550, window=box8)
        box9 = Checkbutton(canvas, text="Ignore list")
        canvas.create_window(320, 750, window=box9)
        box10 = Checkbutton(canvas, text="Ignore list")
        canvas.create_window(320, 950, window=box10)
        box11 = Checkbutton(canvas, text="Ignore list")
        canvas.create_window(320, 1150, window=box11)
        box12 = Checkbutton(canvas, text="Ignore list")
        canvas.create_window(320, 1350, window=box12)
        #Search bar
        search1 = StringVar()
        self.mEntry = Entry(self, width=30)
        canvas.create_window(700, 100, window=self.mEntry)
        searchButton = Button(self, text="Search", command=self.search)
        canvas.create_window(700, 150, window=searchButton)
        #Next Page button
        nextPage = Button(canvas, text="Next Page", command=next)
        canvas.create_window(700, 1500, window=nextPage)
        wListNextPage = Button(canvas, text="Watch List Next Page", command=self.wListNext)
        canvas.create_window(800, 1600, window=wListNextPage)
        #Previous Page button
        prevPage = Button(canvas, text="Previous Page", command=prev)
        canvas.create_window(600, 1500, window=prevPage)
        wListprevPage = Button(canvas, text="Watch List Previous Page", command=self.showWList)
        canvas.create_window(600, 1600, window=wListprevPage)
        #Show Ignore list
        showIgnore = Button(canvas, text="Show Ignore List", command=self.showWList)
        canvas.create_window(800, 1500, window=showIgnore)

        getNum = Button(canvas, text="Update List", command=self.addToWList)
        canvas.create_window(200, 1500, window=getNum)
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

        buttonframe = Frame(self)
        container = Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b3 = Button(buttonframe, text="Help")
        b4 = Button(buttonframe, text="About", command=p1.lift)
        b5 = Button(buttonframe, text="Search List", command=p2.lift)

        b3.grid(row=0, column=5)
        b4.grid(row=0, column=6)
        b5.grid(row=0, column=7)

        p2.show()

        b3.bind("<Button-1>", callback)



root = Tk()
main = MainView(root)
main.pack(side="top", fill="both", expand=True)
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.mainloop()
