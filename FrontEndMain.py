from tkinter import *
import webbrowser
import requests
import json
import array as arr
import urllib.request
import os
from PIL import Image, ImageTk

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
        T2 = Label(self, text="This is the About page for this project")
        T2.place(relx=.5, rely=.5, anchor="center")

k = 0
#path = os.getcwd()
#watch_path = os.path.join(path, "watch_list.txt")
#num_lines = sum(1 for line in open(watch_path))
### SEAN COMMENT OUT ABOVE 2 LINES AND UNCOMMENT BELOW TO WORK FOR YOU
watch_path = '/Users/Sean/Desktop/CSC-380-master/watch_list.txt'
num_lines = sum(1 for line in open(watch_path))
if(os.stat(watch_path).st_size != 0):
    n = (num_lines/7)
    print("Number of lines in watchlist: " + str(num_lines))
    print("Number of items in watchlist: " + str(n))
else:
    n = 0
    print("Number of lines in watchlist: " + str(num_lines))
    print("Number of items in watchlist: " + str(n))
i=0
pageNum=1
class Page2(Page):
    def callPic(self, event):
        webbrowser.open_new(event.widget.cget("text"))
    def wListNext(self):
        global n
        num_lines = sum(1 for line in open('/Users/Sean/Desktop/CSC-380-master/watch_list.txt'))
        n = (num_lines/7)
        self.labelChange.set("Watchlist")
        rget = requests.get("http://127.0.0.1:5000/order66?list_type=1").json()
        print("Number of items in watchlist: " + str(n))
        print("Watchlist dict: " + json.dumps(rget))
        print(n)
        print(rget)
        if(int(n) >= 7):
            if(int(n)==7):
                self.priceOf1.set(rget['item7']['price_no_shipping'])
                self.titleOf1.set(rget['item7']['title'])
                self.pic1.set(rget['item7']['image_url'])
                self.priceOf2.set("")
                self.titleOf2.set("")
                self.pic2.set("")
                self.priceOf3.set("")
                self.titleOf3.set("")
                self.pic3.set("")
                self.priceOf4.set("")
                self.titleOf4.set("")
                self.pic4.set("")
                self.priceOf5.set("")
                self.titleOf5.set("")
                self.pic5.set("")
                self.priceOf6.set("")
                self.titleOf6.set("")
                self.pic6.set("")
            if(int(n)==8):
                self.priceOf1.set(rget['item7']['price_no_shipping'])
                self.titleOf1.set(rget['item7']['title'])
                self.pic1.set(rget['item7']['image_url'])
                self.priceOf2.set(rget['item8']['price_no_shipping'])
                self.titleOf2.set(rget['item8']['title'])
                self.pic2.set(rget['item8']['image_url'])
                self.priceOf3.set("")
                self.titleOf3.set("")
                self.pic3.set("")
                self.priceOf4.set("")
                self.titleOf4.set("")
                self.pic4.set("")
                self.priceOf5.set("")
                self.titleOf5.set("")
                self.pic5.set("")
                self.priceOf6.set("")
                self.titleOf6.set("")
                self.pic6.set("")
            if(int(n)==9):
                self.priceOf1.set(rget['item7']['price_no_shipping'])
                self.titleOf1.set(rget['item7']['title'])
                self.pic1.set(rget['item7']['image_url'])
                self.priceOf2.set(rget['item8']['price_no_shipping'])
                self.titleOf2.set(rget['item8']['title'])
                self.pic2.set(rget['item8']['image_url'])
                self.priceOf3.set(rget['item9']['price_no_shipping'])
                self.titleOf3.set(rget['item9']['title'])
                self.pic3.set(rget['item9']['image_url'])
                self.priceOf4.set("")
                self.titleOf4.set("")
                self.pic4.set("")
                self.priceOf5.set("")
                self.titleOf5.set("")
                self.pic5.set("")
                self.priceOf6.set("")
                self.titleOf6.set("")
                self.pic6.set("")
            if(int(n)==10):
                self.priceOf1.set(rget['item7']['price_no_shipping'])
                self.titleOf1.set(rget['item7']['title'])
                self.pic1.set(rget['item7']['image_url'])
                self.priceOf2.set(rget['item8']['price_no_shipping'])
                self.titleOf2.set(rget['item8']['title'])
                self.pic2.set(rget['item8']['image_url'])
                self.priceOf3.set(rget['item9']['price_no_shipping'])
                self.titleOf3.set(rget['item9']['title'])
                self.pic3.set(rget['item9']['image_url'])
                self.priceOf4.set(rget['item10']['price_no_shipping'])
                self.titleOf4.set(rget['item10']['title'])
                self.pic4.set(rget['item10']['image_url'])
                self.priceOf5.set("")
                self.titleOf5.set("")
                self.pic5.set("")
                self.priceOf6.set("")
                self.titleOf6.set("")
                self.pic6.set("")
            if(int(n)==11):
                self.priceOf1.set(rget['item7']['price_no_shipping'])
                self.titleOf1.set(rget['item7']['title'])
                self.pic1.set(rget['item7']['image_url'])
                self.priceOf2.set(rget['item8']['price_no_shipping'])
                self.titleOf2.set(rget['item8']['title'])
                self.pic2.set(rget['item8']['image_url'])
                self.priceOf3.set(rget['item9']['price_no_shipping'])
                self.titleOf3.set(rget['item9']['title'])
                self.pic3.set(rget['item9']['image_url'])
                self.priceOf4.set(rget['item10']['price_no_shipping'])
                self.titleOf4.set(rget['item10']['title'])
                self.pic4.set(rget['item10']['image_url'])
                self.priceOf5.set(rget['item11']['price_no_shipping'])
                self.titleOf5.set(rget['item11']['title'])
                self.pic5.set(rget['item11']['image_url'])
                self.priceOf6.set("")
                self.titleOf6.set("")
                self.pic6.set("")
            if(int(n)>=12):
                self.priceOf1.set(rget['item7']['price_no_shipping'])
                self.titleOf1.set(rget['item7']['title'])
                self.pic1.set(rget['item7']['image_url'])
                self.priceOf2.set(rget['item8']['price_no_shipping'])
                self.titleOf2.set(rget['item8']['title'])
                self.pic2.set(rget['item8']['image_url'])
                self.priceOf3.set(rget['item9']['price_no_shipping'])
                self.titleOf3.set(rget['item9']['title'])
                self.pic3.set(rget['item9']['image_url'])
                self.priceOf4.set(rget['item10']['price_no_shipping'])
                self.titleOf4.set(rget['item10']['title'])
                self.pic4.set(rget['item10']['image_url'])
                self.priceOf5.set(rget['item11']['price_no_shipping'])
                self.titleOf5.set(rget['item11']['title'])
                self.pic5.set(rget['item11']['image_url'])
                self.priceOf6.set(rget['item12']['price_no_shipping'])
                self.titleOf6.set(rget['item12']['title'])
                self.pic6.set(rget['item12']['image_url'])
    def iListNext(self):
        global p
        print(p)
        num_lines = sum(1 for line in open('/Users/Sean/Desktop/CSC-380-master/ignore_list.txt'))
        p = (num_lines/7)
        self.labelChange.set("Ignore List")
        rget = requests.get("http://127.0.0.1:5000/order66?list_type=2").json()
        print("Number of items in ignore list: " + str(n))
        print("ignore list dict: " + json.dumps(rget))
        print(p)
        print(rget)
        if(int(p) >= 7):
            if(int(p)==7):
                self.priceOf1.set(rget['item7']['price_no_shipping'])
                self.titleOf1.set(rget['item7']['title'])
                self.pic1.set(rget['item7']['image_url'])
                self.priceOf2.set("")
                self.titleOf2.set("")
                self.pic2.set("")
                self.priceOf3.set("")
                self.titleOf3.set("")
                self.pic3.set("")
                self.priceOf4.set("")
                self.titleOf4.set("")
                self.pic4.set("")
                self.priceOf5.set("")
                self.titleOf5.set("")
                self.pic5.set("")
                self.priceOf6.set("")
                self.titleOf6.set("")
                self.pic6.set("")
            if(int(p)==8):
                self.priceOf1.set(rget['item7']['price_no_shipping'])
                self.titleOf1.set(rget['item7']['title'])
                self.pic1.set(rget['item7']['image_url'])
                self.priceOf2.set(rget['item8']['price_no_shipping'])
                self.titleOf2.set(rget['item8']['title'])
                self.pic2.set(rget['item8']['image_url'])
                self.priceOf3.set("")
                self.titleOf3.set("")
                self.pic3.set("")
                self.priceOf4.set("")
                self.titleOf4.set("")
                self.pic4.set("")
                self.priceOf5.set("")
                self.titleOf5.set("")
                self.pic5.set("")
                self.priceOf6.set("")
                self.titleOf6.set("")
                self.pic6.set("")
            if(int(p)==9):
                self.priceOf1.set(rget['item7']['price_no_shipping'])
                self.titleOf1.set(rget['item7']['title'])
                self.pic1.set(rget['item7']['image_url'])
                self.priceOf2.set(rget['item8']['price_no_shipping'])
                self.titleOf2.set(rget['item8']['title'])
                self.pic2.set(rget['item8']['image_url'])
                self.priceOf3.set(rget['item9']['price_no_shipping'])
                self.titleOf3.set(rget['item9']['title'])
                self.pic3.set(rget['item9']['image_url'])
                self.priceOf4.set("")
                self.titleOf4.set("")
                self.pic4.set("")
                self.priceOf5.set("")
                self.titleOf5.set("")
                self.pic5.set("")
                self.priceOf6.set("")
                self.titleOf6.set("")
                self.pic6.set("")
            if(int(p)==10):
                self.priceOf1.set(rget['item7']['price_no_shipping'])
                self.titleOf1.set(rget['item7']['title'])
                self.pic1.set(rget['item7']['image_url'])
                self.priceOf2.set(rget['item8']['price_no_shipping'])
                self.titleOf2.set(rget['item8']['title'])
                self.pic2.set(rget['item8']['image_url'])
                self.priceOf3.set(rget['item9']['price_no_shipping'])
                self.titleOf3.set(rget['item9']['title'])
                self.pic3.set(rget['item9']['image_url'])
                self.priceOf4.set(rget['item10']['price_no_shipping'])
                self.titleOf4.set(rget['item10']['title'])
                self.pic4.set(rget['item10']['image_url'])
                self.priceOf5.set("")
                self.titleOf5.set("")
                self.pic5.set("")
                self.priceOf6.set("")
                self.titleOf6.set("")
                self.pic6.set("")
            if(int(p)==11):
                self.priceOf1.set(rget['item7']['price_no_shipping'])
                self.titleOf1.set(rget['item7']['title'])
                self.pic1.set(rget['item7']['image_url'])
                self.priceOf2.set(rget['item8']['price_no_shipping'])
                self.titleOf2.set(rget['item8']['title'])
                self.pic2.set(rget['item8']['image_url'])
                self.priceOf3.set(rget['item9']['price_no_shipping'])
                self.titleOf3.set(rget['item9']['title'])
                self.pic3.set(rget['item9']['image_url'])
                self.priceOf4.set(rget['item10']['price_no_shipping'])
                self.titleOf4.set(rget['item10']['title'])
                self.pic4.set(rget['item10']['image_url'])
                self.priceOf5.set(rget['item11']['price_no_shipping'])
                self.titleOf5.set(rget['item11']['title'])
                self.pic5.set(rget['item11']['image_url'])
                self.priceOf6.set("")
                self.titleOf6.set("")
                self.pic6.set("")
            if(int(p)>=12):
                self.priceOf1.set(rget['item7']['price_no_shipping'])
                self.titleOf1.set(rget['item7']['title'])
                self.pic1.set(rget['item7']['image_url'])
                self.priceOf2.set(rget['item8']['price_no_shipping'])
                self.titleOf2.set(rget['item8']['title'])
                self.pic2.set(rget['item8']['image_url'])
                self.priceOf3.set(rget['item9']['price_no_shipping'])
                self.titleOf3.set(rget['item9']['title'])
                self.pic3.set(rget['item9']['image_url'])
                self.priceOf4.set(rget['item10']['price_no_shipping'])
                self.titleOf4.set(rget['item10']['title'])
                self.pic4.set(rget['item10']['image_url'])
                self.priceOf5.set(rget['item11']['price_no_shipping'])
                self.titleOf5.set(rget['item11']['title'])
                self.pic5.set(rget['item11']['image_url'])
                self.priceOf6.set(rget['item12']['price_no_shipping'])
                self.titleOf6.set(rget['item12']['title'])
                self.pic6.set(rget['item12']['image_url'])
    def deleteFromWList(self):
        global n
        num_lines = sum(1 for line in open('/Users/Sean/Desktop/CSC-380-master/watch_list.txt'))
        n = (num_lines/7)
        json_data = requests.get("http://127.0.0.2:5000/order66?list_type=1").json()
        print(json_data)
        if(n==1):
            firstPrice = json_data['item1']['price_no_shipping']
            firstTitle = json_data['item1']['title']
            firstID = json_data['item1']['itemId']
            firstShipping = json_data['item1']['price_shipping']
            firstCountry = json_data['item1']['country']
            firstImage = json_data['item1']['image_url']
        if(n==2):
            firstPrice = json_data['item1']['price_no_shipping']
            firstTitle = json_data['item1']['title']
            firstID = json_data['item1']['itemId']
            firstShipping = json_data['item1']['price_shipping']
            firstCountry = json_data['item1']['country']
            firstImage = json_data['item1']['image_url']
            secondPrice = json_data['item2']['price_no_shipping']
            secondTitle = json_data['item2']['title']
            secondID = json_data['item2']['itemId']
            secondShipping = json_data['item2']['price_shipping']
            secondCountry = json_data['item2']['country']
            secondImage = json_data['item2']['image_url']
        if(n==3):
            firstPrice = json_data['item1']['price_no_shipping']
            firstTitle = json_data['item1']['title']
            firstID = json_data['item1']['itemId']
            firstShipping = json_data['item1']['price_shipping']
            firstCountry = json_data['item1']['country']
            firstImage = json_data['item1']['image_url']
            secondPrice = json_data['item2']['price_no_shipping']
            secondTitle = json_data['item2']['title']
            secondID = json_data['item2']['itemId']
            secondShipping = json_data['item2']['price_shipping']
            secondCountry = json_data['item2']['country']
            secondImage = json_data['item2']['image_url']
            thirdPrice = json_data['item3']['price_no_shipping']
            thirdTitle = json_data['item3']['title']
            thirdID = json_data['item3']['itemId']
            thirdShipping = json_data['item3']['price_shipping']
            thirdCountry = json_data['item3']['country']
            thirdImage = json_data['item3']['image_url']
        if(n==4):
            firstPrice = json_data['item1']['price_no_shipping']
            firstTitle = json_data['item1']['title']
            firstID = json_data['item1']['itemId']
            firstShipping = json_data['item1']['price_shipping']
            firstCountry = json_data['item1']['country']
            firstImage = json_data['item1']['image_url']
            secondPrice = json_data['item2']['price_no_shipping']
            secondTitle = json_data['item2']['title']
            secondID = json_data['item2']['itemId']
            secondShipping = json_data['item2']['price_shipping']
            secondCountry = json_data['item2']['country']
            secondImage = json_data['item2']['image_url']
            #secondList = json_data['1']['list_type']
            thirdPrice = json_data['item3']['price_no_shipping']
            thirdTitle = json_data['item3']['title']
            thirdID = json_data['item3']['itemId']
            thirdShipping = json_data['item3']['price_shipping']
            thirdCountry = json_data['item3']['country']
            thirdImage = json_data['item3']['image_url']
            #thirdList = json_data['2']['list_type']
            fourthPrice = json_data['item4']['price_no_shipping']
            fourthTitle = json_data['item4']['title']
            fourthID = json_data['item4']['itemId']
            fourthShipping = json_data['item4']['price_shipping']
            fourthCountry = json_data['item4']['country']
            fourthImage = json_data['item4']['image_url']
        if(n==5):
            secondPrice = json_data['item2']['price_no_shipping']
            secondTitle = json_data['item2']['title']
            secondID = json_data['item2']['itemId']
            secondShipping = json_data['item2']['price_shipping']
            secondCountry = json_data['item2']['country']
            secondImage = json_data['item2']['image_url']
            #secondList = json_data['1']['list_type']
            thirdPrice = json_data['item3']['price_no_shipping']
            thirdTitle = json_data['item3']['title']
            thirdID = json_data['item3']['itemId']
            thirdShipping = json_data['item3']['price_shipping']
            thirdCountry = json_data['item3']['country']
            thirdImage = json_data['item3']['image_url']
            #thirdList = json_data['2']['list_type']
            fourthPrice = json_data['item4']['price_no_shipping']
            fourthTitle = json_data['item4']['title']
            fourthID = json_data['item4']['itemId']
            fourthShipping = json_data['item4']['price_shipping']
            fourthCountry = json_data['item4']['country']
            fourthImage = json_data['item4']['image_url']
            fifthPrice = json_data['item5']['price_no_shipping']
            fifthTitle = json_data['item5']['title']
            fifthID = json_data['item5']['itemId']
            fifthShipping = json_data['item5']['price_shipping']
            fifthCountry = json_data['item5']['country']
            fifthImage = json_data['item5']['image_url']
        if(n>=6):
            firstPrice = json_data['item1']['price_no_shipping']
            firstTitle = json_data['item1']['title']
            firstID = json_data['item1']['itemId']
            firstShipping = json_data['item1']['price_shipping']
            firstCountry = json_data['item1']['country']
            firstImage = json_data['item1']['image_url']
            #firstList = json_data['0']['list_type']
            secondPrice = json_data['item2']['price_no_shipping']
            secondTitle = json_data['item2']['title']
            secondID = json_data['item2']['itemId']
            secondShipping = json_data['item2']['price_shipping']
            secondCountry = json_data['item2']['country']
            secondImage = json_data['item2']['image_url']
            #secondList = json_data['1']['list_type']
            thirdPrice = json_data['item3']['price_no_shipping']
            thirdTitle = json_data['item3']['title']
            thirdID = json_data['item3']['itemId']
            thirdShipping = json_data['item3']['price_shipping']
            thirdCountry = json_data['item3']['country']
            thirdImage = json_data['item3']['image_url']
            #thirdList = json_data['2']['list_type']
            fourthPrice = json_data['item4']['price_no_shipping']
            fourthTitle = json_data['item4']['title']
            fourthID = json_data['item4']['itemId']
            fourthShipping = json_data['item4']['price_shipping']
            fourthCountry = json_data['item4']['country']
            fourthImage = json_data['item4']['image_url']
            #fourthList = json_data['3']['list_type']
            fifthPrice = json_data['item5']['price_no_shipping']
            fifthTitle = json_data['item5']['title']
            fifthID = json_data['item5']['itemId']
            fifthShipping = json_data['item5']['price_shipping']
            fifthCountry = json_data['item5']['country']
            fifthImage = json_data['item5']['image_url']
            #fifthList = json_data['4']['list_type']
            sixthPrice = json_data['item6']['price_shipping']
            sixthTitle = json_data['item6']['title']
            sixthID = json_data['item6']['itemId']
            sixthShipping = json_data['item6']['price_shipping']
            sixthCountry = json_data['item6']['country']
            sixthImage = json_data['item6']['image_url']
            #sixthList = json_data['5']['list_type']
        if(self.var1.get()):
            data1 = {
            'itemId': firstID,
            'title': firstTitle,
            'price': firstPrice,
            'shipping': firstShipping,
            'country': firstCountry,
            'image_url': firstImage,
            'list_type': str(1)
            }
            print(1)
            rdelete1 = requests.delete("http://127.0.0.2:5000/order66?itemId="+firstID+
            "&title="+firstTitle+"&price="+firstPrice+"&shipping="+firstShipping+"&country="
            +firstCountry+"&image_url="+firstImage+"&list_type="+str(1))
        if(self.var2.get()):
            data2 = {
            'itemId': secondID,
            'title': secondTitle,
            'price': secondPrice,
            'shipping': secondShipping,
            'country': secondCountry,
            'image_url': secondImage,
            'list_type': str(1)
            }
            print(2)
            rdelete2 =requests.delete("http://127.0.0.2:5000/order66?itemId="+secondID+
            "&title="+secondTitle+"&price="+secondPrice+"&shipping="+secondShipping+"&country="
            +secondCountry+"&image_url="+secondImage+"&list_type="+str(1))
        if(self.var3.get()):
            data3 = {
            'itemId': thirdID,
            'title': thirdTitle,
            'price': thirdPrice,
            'shipping': thirdShipping,
            'country': thirdCountry,
            'image_url': thirdImage,
            'list_type': str(1)
            }
            print(3)
            rdelete3 =requests.delete("http://127.0.0.2:5000/order66?itemId="+thirdID+
            "&title="+thirdTitle+"&price="+thirdPrice+"&shipping="+thirdShipping+"&country="
            +thirdCountry+"&image_url="+thirdImage+"&list_type="+str(1))
            print(rdelete3)
        if(self.var4.get()):
            data4 = {
            'itemId': fourthID,
            'title': fourthTitle,
            'price': fourthPrice,
            'shipping': fourthShipping,
            'country': fourthCountry,
            'image_url': fourthImage,
            'list_type': str(1)
            }
            print(4)
            rdelete4 =requests.delete("http://127.0.0.2:5000/order66?itemId="+fourthID+
            "&title="+fourthTitle+"&price="+fourthPrice+"&shipping="+fourthShipping+"&country="
            +fourthCountry+"&image_url="+fourthImage+"&list_type="+str(1))
        if(self.var5.get()):
            data5 = {
            'itemId': fifthID,
            'title': fifthTitle,
            'price': fifthPrice,
            'shipping': fifthShipping,
            'country': fifthCountry,
            'image_url': fifthImage,
            'list_type': str(1)
            }
            print(5)
            rdelete5 =requests.delete("http://127.0.0.2:5000/order66?itemId="+fifthID+
            "&title="+fifthTitle+"&price="+fifthPrice+"&shipping="+fifthShipping+"&country="
            +fifthCountry+"&image_url="+fifthImage+"&list_type="+str(1))
        if(self.var6.get()):
            data6 = {
            'itemId': sixthID,
            'title': sixthTitle,
            'price': sixthPrice,
            'shipping': sixthShipping,
            'country': sixthCountry,
            'image_url': sixthImage,
            'list_type': str(1)
            }
            print(6)
            rdelete6 =requests.delete("http://127.0.0.2:5000/order66?itemId="+sixthID+
            "&title="+sixthTitle+"&price="+sixthPrice+"&shipping="+sixthShipping+"&country="
            +sixthCountry+"&image_url="+sixthImage+"&list_type="+str(1))
    def deleteFromIList(self):
        global p
        num_lines = sum(1 for line in open('/Users/Sean/Desktop/CSC-380-master/ignore_list.txt'))
        p = (num_lines/7)
        print(p)
        json_data = requests.get("http://127.0.0.2:5000/order66?list_type=2").json()
        print(json_data)
        if(p==1):
            firstPrice = json_data['item1']['price_no_shipping']
            firstTitle = json_data['item1']['title']
            firstID = json_data['item1']['itemId']
            firstShipping = json_data['item1']['price_shipping']
            firstCountry = json_data['item1']['country']
            firstImage = json_data['item1']['image_url']
        if(p==2):
            firstPrice = json_data['item1']['price_no_shipping']
            firstTitle = json_data['item1']['title']
            firstID = json_data['item1']['itemId']
            firstShipping = json_data['item1']['price_shipping']
            firstCountry = json_data['item1']['country']
            firstImage = json_data['item1']['image_url']
            secondPrice = json_data['item2']['price_no_shipping']
            secondTitle = json_data['item2']['title']
            secondID = json_data['item2']['itemId']
            secondShipping = json_data['item2']['price_shipping']
            secondCountry = json_data['item2']['country']
            secondImage = json_data['item2']['image_url']
        if(p==3):
            firstPrice = json_data['item1']['price_no_shipping']
            firstTitle = json_data['item1']['title']
            firstID = json_data['item1']['itemId']
            firstShipping = json_data['item1']['price_shipping']
            firstCountry = json_data['item1']['country']
            firstImage = json_data['item1']['image_url']
            secondPrice = json_data['item2']['price_no_shipping']
            secondTitle = json_data['item2']['title']
            secondID = json_data['item2']['itemId']
            secondShipping = json_data['item2']['price_shipping']
            secondCountry = json_data['item2']['country']
            secondImage = json_data['item2']['image_url']
            thirdPrice = json_data['item3']['price_no_shipping']
            thirdTitle = json_data['item3']['title']
            thirdID = json_data['item3']['itemId']
            thirdShipping = json_data['item3']['price_shipping']
            thirdCountry = json_data['item3']['country']
            thirdImage = json_data['item3']['image_url']
        if(p==4):
            firstPrice = json_data['item1']['price_no_shipping']
            firstTitle = json_data['item1']['title']
            firstID = json_data['item1']['itemId']
            firstShipping = json_data['item1']['price_shipping']
            firstCountry = json_data['item1']['country']
            firstImage = json_data['item1']['image_url']
            secondPrice = json_data['item2']['price_no_shipping']
            secondTitle = json_data['item2']['title']
            secondID = json_data['item2']['itemId']
            secondShipping = json_data['item2']['price_shipping']
            secondCountry = json_data['item2']['country']
            secondImage = json_data['item2']['image_url']
            #secondList = json_data['1']['list_type']
            thirdPrice = json_data['item3']['price_no_shipping']
            thirdTitle = json_data['item3']['title']
            thirdID = json_data['item3']['itemId']
            thirdShipping = json_data['item3']['price_shipping']
            thirdCountry = json_data['item3']['country']
            thirdImage = json_data['item3']['image_url']
            #thirdList = json_data['2']['list_type']
            fourthPrice = json_data['item4']['price_no_shipping']
            fourthTitle = json_data['item4']['title']
            fourthID = json_data['item4']['itemId']
            fourthShipping = json_data['item4']['price_shipping']
            fourthCountry = json_data['item4']['country']
            fourthImage = json_data['item4']['image_url']
        if(p==5):
            secondPrice = json_data['item2']['price_no_shipping']
            secondTitle = json_data['item2']['title']
            secondID = json_data['item2']['itemId']
            secondShipping = json_data['item2']['price_shipping']
            secondCountry = json_data['item2']['country']
            secondImage = json_data['item2']['image_url']
            #secondList = json_data['1']['list_type']
            thirdPrice = json_data['item3']['price_no_shipping']
            thirdTitle = json_data['item3']['title']
            thirdID = json_data['item3']['itemId']
            thirdShipping = json_data['item3']['price_shipping']
            thirdCountry = json_data['item3']['country']
            thirdImage = json_data['item3']['image_url']
            #thirdList = json_data['2']['list_type']
            fourthPrice = json_data['item4']['price_no_shipping']
            fourthTitle = json_data['item4']['title']
            fourthID = json_data['item4']['itemId']
            fourthShipping = json_data['item4']['price_shipping']
            fourthCountry = json_data['item4']['country']
            fourthImage = json_data['item4']['image_url']
            fifthPrice = json_data['item5']['price_no_shipping']
            fifthTitle = json_data['item5']['title']
            fifthID = json_data['item5']['itemId']
            fifthShipping = json_data['item5']['price_shipping']
            fifthCountry = json_data['item5']['country']
            fifthImage = json_data['item5']['image_url']
        if(p>=6):
            firstPrice = json_data['item1']['price_no_shipping']
            firstTitle = json_data['item1']['title']
            firstID = json_data['item1']['itemId']
            firstShipping = json_data['item1']['price_shipping']
            firstCountry = json_data['item1']['country']
            firstImage = json_data['item1']['image_url']
            #firstList = json_data['0']['list_type']
            secondPrice = json_data['item2']['price_no_shipping']
            secondTitle = json_data['item2']['title']
            secondID = json_data['item2']['itemId']
            secondShipping = json_data['item2']['price_shipping']
            secondCountry = json_data['item2']['country']
            secondImage = json_data['item2']['image_url']
            #secondList = json_data['1']['list_type']
            thirdPrice = json_data['item3']['price_no_shipping']
            thirdTitle = json_data['item3']['title']
            thirdID = json_data['item3']['itemId']
            thirdShipping = json_data['item3']['price_shipping']
            thirdCountry = json_data['item3']['country']
            thirdImage = json_data['item3']['image_url']
            #thirdList = json_data['2']['list_type']
            fourthPrice = json_data['item4']['price_no_shipping']
            fourthTitle = json_data['item4']['title']
            fourthID = json_data['item4']['itemId']
            fourthShipping = json_data['item4']['price_shipping']
            fourthCountry = json_data['item4']['country']
            fourthImage = json_data['item4']['image_url']
            #fourthList = json_data['3']['list_type']
            fifthPrice = json_data['item5']['price_no_shipping']
            fifthTitle = json_data['item5']['title']
            fifthID = json_data['item5']['itemId']
            fifthShipping = json_data['item5']['price_shipping']
            fifthCountry = json_data['item5']['country']
            fifthImage = json_data['item5']['image_url']
            #fifthList = json_data['4']['list_type']
            sixthPrice = json_data['item6']['price_shipping']
            sixthTitle = json_data['item6']['title']
            sixthID = json_data['item6']['itemId']
            sixthShipping = json_data['item6']['price_shipping']
            sixthCountry = json_data['item6']['country']
            sixthImage = json_data['item6']['image_url']
            #sixthList = json_data['5']['list_type']
        if(self.var1.get()):
            data1 = {
            'itemId': firstID,
            'title': firstTitle,
            'price': firstPrice,
            'shipping': firstShipping,
            'country': firstCountry,
            'image_url': firstImage,
            'list_type': str(2)
            }
            print(1)
            rdelete1 = requests.delete("http://127.0.0.2:5000/order66?itemId="+firstID+
            "&title="+firstTitle+"&price="+firstPrice+"&shipping="+firstShipping+"&country="
            +firstCountry+"&image_url="+firstImage+"&list_type="+str(2))
        if(self.var2.get()):
            data2 = {
            'itemId': secondID,
            'title': secondTitle,
            'price': secondPrice,
            'shipping': secondShipping,
            'country': secondCountry,
            'image_url': secondImage,
            'list_type': str(2)
            }
            print(2)
            rdelete2 =requests.delete("http://127.0.0.2:5000/order66?itemId="+secondID+
            "&title="+secondTitle+"&price="+secondPrice+"&shipping="+secondShipping+"&country="
            +secondCountry+"&image_url="+secondImage+"&list_type="+str(2))
        if(self.var3.get()):
            data3 = {
            'itemId': thirdID,
            'title': thirdTitle,
            'price': thirdPrice,
            'shipping': thirdShipping,
            'country': thirdCountry,
            'image_url': thirdImage,
            'list_type': str(2)
            }
            print(3)
            rdelete3 =requests.delete("http://127.0.0.2:5000/order66?itemId="+thirdID+
            "&title="+thirdTitle+"&price="+thirdPrice+"&shipping="+thirdShipping+"&country="
            +thirdCountry+"&image_url="+thirdImage+"&list_type="+str(2))
            print(rdelete3)
        if(self.var4.get()):
            data4 = {
            'itemId': fourthID,
            'title': fourthTitle,
            'price': fourthPrice,
            'shipping': fourthShipping,
            'country': fourthCountry,
            'image_url': fourthImage,
            'list_type': str(2)
            }
            print(4)
            rdelete4 =requests.delete("http://127.0.0.2:5000/order66?itemId="+fourthID+
            "&title="+fourthTitle+"&price="+fourthPrice+"&shipping="+fourthShipping+"&country="
            +fourthCountry+"&image_url="+fourthImage+"&list_type="+str(2))
        if(self.var5.get()):
            data5 = {
            'itemId': fifthID,
            'title': fifthTitle,
            'price': fifthPrice,
            'shipping': fifthShipping,
            'country': fifthCountry,
            'image_url': fifthImage,
            'list_type': str(2)
            }
            print(5)
            rdelete5 =requests.delete("http://127.0.0.2:5000/order66?itemId="+fifthID+
            "&title="+fifthTitle+"&price="+fifthPrice+"&shipping="+fifthShipping+"&country="
            +fifthCountry+"&image_url="+fifthImage+"&list_type="+str(2))
        if(self.var6.get()):
            data6 = {
            'itemId': sixthID,
            'title': sixthTitle,
            'price': sixthPrice,
            'shipping': sixthShipping,
            'country': sixthCountry,
            'image_url': sixthImage,
            'list_type': str(2)
            }
            print(6)
            rdelete6 =requests.delete("http://127.0.0.2:5000/order66?itemId="+sixthID+
            "&title="+sixthTitle+"&price="+sixthPrice+"&shipping="+sixthShipping+"&country="
            +sixthCountry+"&image_url="+sixthImage+"&list_type="+str(2))
    def showWList(self):
        global n
        num_lines = sum(1 for line in open('/Users/Sean/Desktop/CSC-380-master/watch_list.txt'))
        n = (num_lines/7)
        self.labelChange.set("Watchlist")
        self.listName1.set("Delete From List")
        self.listName2.set("Delete From List")
        self.listName3.set("Delete From List")
        self.listName4.set("Delete From List")
        self.listName5.set("Delete From List")
        self.listName6.set("Delete From List")
        self.listName7.set("")
        self.listName8.set("")
        self.listName9.set("")
        self.listName10.set("")
        self.listName11.set("")
        self.listName12.set("")
        rget = requests.get("http://127.0.0.2:5000/order66?list_type=1").json()
        print(n)
        print(rget)
        if(int(n)==0):
            self.priceOf1.set("")
            self.titleOf1.set("")
            self.pic1.set("")
            self.priceOf2.set("")
            self.titleOf2.set("")
            self.pic2.set("")
            self.priceOf3.set("")
            self.titleOf3.set("")
            self.pic3.set("")
            self.priceOf4.set("")
            self.titleOf4.set("")
            self.pic4.set("")
            self.priceOf5.set("")
            self.titleOf5.set("")
            self.pic5.set("")
            self.priceOf6.set("")
            self.titleOf6.set("")
            self.pic6.set("")
        if(int(n)==1):
            self.priceOf1.set(rget['item1']['price_no_shipping'])
            self.titleOf1.set(rget['item1']['title'])
            self.pic1.set(rget['item1']['image_url'])
            self.priceOf2.set("")
            self.titleOf2.set("")
            self.pic2.set("")
            self.priceOf3.set("")
            self.titleOf3.set("")
            self.pic3.set("")
            self.priceOf4.set("")
            self.titleOf4.set("")
            self.pic4.set("")
            self.priceOf5.set("")
            self.titleOf5.set("")
            self.pic5.set("")
            self.priceOf6.set("")
            self.titleOf6.set("")
            self.pic6.set("")
        if(int(n)==2):
            self.priceOf1.set(rget['item1']['price_no_shipping'])
            self.titleOf1.set(rget['item1']['title'])
            self.pic1.set(rget['item1']['image_url'])
            self.priceOf2.set(rget['item2']['price_no_shipping'])
            self.titleOf2.set(rget['item2']['title'])
            self.pic2.set(rget['item2']['image_url'])
            self.priceOf3.set("")
            self.titleOf3.set("")
            self.pic3.set("")
            self.priceOf4.set("")
            self.titleOf4.set("")
            self.pic4.set("")
            self.priceOf5.set("")
            self.titleOf5.set("")
            self.pic5.set("")
            self.priceOf6.set("")
            self.titleOf6.set("")
            self.pic6.set("")
        if(int(n)==3):
            self.priceOf1.set(rget['item1']['price_no_shipping'])
            self.titleOf1.set(rget['item1']['title'])
            self.pic1.set(rget['item1']['image_url'])
            self.priceOf2.set(rget['item2']['price_no_shipping'])
            self.titleOf2.set(rget['item2']['title'])
            self.pic2.set(rget['item2']['image_url'])
            self.priceOf3.set(rget['item3']['price_no_shipping'])
            self.titleOf3.set(rget['item3']['title'])
            self.pic3.set(rget['item3']['image_url'])
            self.priceOf4.set("")
            self.titleOf4.set("")
            self.pic4.set("")
            self.priceOf5.set("")
            self.titleOf5.set("")
            self.pic5.set("")
            self.priceOf6.set("")
            self.titleOf6.set("")
            self.pic6.set("")
        if(int(n)==4):
            self.priceOf1.set(rget['item1']['price_no_shipping'])
            self.titleOf1.set(rget['item1']['title'])
            self.pic1.set(rget['item1']['image_url'])
            self.priceOf2.set(rget['item2']['price_no_shipping'])
            self.titleOf2.set(rget['item2']['title'])
            self.pic2.set(rget['item2']['image_url'])
            self.priceOf3.set(rget['item3']['price_no_shipping'])
            self.titleOf3.set(rget['item3']['title'])
            self.pic3.set(rget['item3']['image_url'])
            self.priceOf4.set(rget['item4']['price_no_shipping'])
            self.titleOf4.set(rget['item4']['title'])
            self.pic4.set(rget['item4']['image_url'])
            self.priceOf5.set("")
            self.titleOf5.set("")
            self.pic5.set("")
            self.priceOf6.set("")
            self.titleOf6.set("")
            self.pic6.set("")
        if(int(n)==5):
            self.priceOf1.set(rget['item1']['price_no_shipping'])
            self.titleOf1.set(rget['item1']['title'])
            self.pic1.set(rget['item1']['image_url'])
            self.priceOf2.set(rget['item2']['price_no_shipping'])
            self.titleOf2.set(rget['item2']['title'])
            self.pic2.set(rget['item2']['image_url'])
            self.priceOf3.set(rget['item3']['price_no_shipping'])
            self.titleOf3.set(rget['item3']['title'])
            self.pic3.set(rget['item3']['image_url'])
            self.priceOf4.set(rget['item4']['price_no_shipping'])
            self.titleOf4.set(rget['item4']['title'])
            self.pic4.set(rget['item4']['image_url'])
            self.priceOf5.set(rget['item5']['price_no_shipping'])
            self.titleOf5.set(rget['item5']['title'])
            self.pic5.set(rget['item5']['image_url'])
            self.priceOf6.set("")
            self.titleOf6.set("")
            self.pic6.set("")
        if(int(n)>=6):
            self.priceOf1.set(rget['item1']['price_no_shipping'])
            self.titleOf1.set(rget['item1']['title'])
            self.pic1.set(rget['item1']['image_url'])
            self.priceOf2.set(rget['item2']['price_no_shipping'])
            self.titleOf2.set(rget['item2']['title'])
            self.pic2.set(rget['item2']['image_url'])
            self.priceOf3.set(rget['item3']['price_no_shipping'])
            self.titleOf3.set(rget['item3']['title'])
            self.pic3.set(rget['item3']['image_url'])
            self.priceOf4.set(rget['item4']['price_no_shipping'])
            self.titleOf4.set(rget['item4']['title'])
            self.pic4.set(rget['item4']['image_url'])
            self.priceOf5.set(rget['item5']['price_no_shipping'])
            self.titleOf5.set(rget['item5']['title'])
            self.pic5.set(rget['item5']['image_url'])
            self.priceOf6.set(rget['item6']['price_no_shipping'])
            self.titleOf6.set(rget['item6']['title'])
            self.pic6.set(rget['item6']['image_url'])
        self.var1.set(0)
        self.var2.set(0)
        self.var3.set(0)
        self.var4.set(0)
        self.var5.set(0)
        self.var6.set(0)

    def showIList(self):
        global p
        num_lines = sum(1 for line in open('/Users/Sean/Desktop/CSC-380-master/ignore_list.txt'))
        p = (num_lines/7)
        self.labelChange.set("Ignore list")
        self.listName1.set("Delete From List")
        self.listName2.set("Delete From List")
        self.listName3.set("Delete From List")
        self.listName4.set("Delete From List")
        self.listName5.set("Delete From List")
        self.listName6.set("Delete From List")
        self.listName7.set("")
        self.listName8.set("")
        self.listName9.set("")
        self.listName10.set("")
        self.listName11.set("")
        self.listName12.set("")
        rget = requests.get("http://127.0.0.2:5000/order66?list_type=2").json()
        print(p)
        print(rget)
        if(int(p)==0):
            self.priceOf1.set("")
            self.titleOf1.set("")
            self.pic1.set("")
            self.priceOf2.set("")
            self.titleOf2.set("")
            self.pic2.set("")
            self.priceOf3.set("")
            self.titleOf3.set("")
            self.pic3.set("")
            self.priceOf4.set("")
            self.titleOf4.set("")
            self.pic4.set("")
            self.priceOf5.set("")
            self.titleOf5.set("")
            self.pic5.set("")
            self.priceOf6.set("")
            self.titleOf6.set("")
            self.pic6.set("")
        if(int(p)==1):
            self.priceOf1.set(rget['item1']['price_no_shipping'])
            self.titleOf1.set(rget['item1']['title'])
            self.pic1.set(rget['item1']['image_url'])
            self.priceOf2.set("")
            self.titleOf2.set("")
            self.pic2.set("")
            self.priceOf3.set("")
            self.titleOf3.set("")
            self.pic3.set("")
            self.priceOf4.set("")
            self.titleOf4.set("")
            self.pic4.set("")
            self.priceOf5.set("")
            self.titleOf5.set("")
            self.pic5.set("")
            self.priceOf6.set("")
            self.titleOf6.set("")
            self.pic6.set("")
        if(int(p)==2):
            self.priceOf1.set(rget['item1']['price_no_shipping'])
            self.titleOf1.set(rget['item1']['title'])
            self.pic1.set(rget['item1']['image_url'])
            self.priceOf2.set(rget['item2']['price_no_shipping'])
            self.titleOf2.set(rget['item2']['title'])
            self.pic2.set(rget['item2']['image_url'])
            self.priceOf3.set("")
            self.titleOf3.set("")
            self.pic3.set("")
            self.priceOf4.set("")
            self.titleOf4.set("")
            self.pic4.set("")
            self.priceOf5.set("")
            self.titleOf5.set("")
            self.pic5.set("")
            self.priceOf6.set("")
            self.titleOf6.set("")
            self.pic6.set("")
        if(int(p)==3):
            self.priceOf1.set(rget['item1']['price_no_shipping'])
            self.titleOf1.set(rget['item1']['title'])
            self.pic1.set(rget['item1']['image_url'])
            self.priceOf2.set(rget['item2']['price_no_shipping'])
            self.titleOf2.set(rget['item2']['title'])
            self.pic2.set(rget['item2']['image_url'])
            self.priceOf3.set(rget['item3']['price_no_shipping'])
            self.titleOf3.set(rget['item3']['title'])
            self.pic3.set(rget['item3']['image_url'])
            self.priceOf4.set("")
            self.titleOf4.set("")
            self.pic4.set("")
            self.priceOf5.set("")
            self.titleOf5.set("")
            self.pic5.set("")
            self.priceOf6.set("")
            self.titleOf6.set("")
            self.pic6.set("")
        if(int(p)==4):
            self.priceOf1.set(rget['item1']['price_no_shipping'])
            self.titleOf1.set(rget['item1']['title'])
            self.pic1.set(rget['item1']['image_url'])
            self.priceOf2.set(rget['item2']['price_no_shipping'])
            self.titleOf2.set(rget['item2']['title'])
            self.pic2.set(rget['item2']['image_url'])
            self.priceOf3.set(rget['item3']['price_no_shipping'])
            self.titleOf3.set(rget['item3']['title'])
            self.pic3.set(rget['item3']['image_url'])
            self.priceOf4.set(rget['item4']['price_no_shipping'])
            self.titleOf4.set(rget['item4']['title'])
            self.pic4.set(rget['item4']['image_url'])
            self.priceOf5.set("")
            self.titleOf5.set("")
            self.pic5.set("")
            self.priceOf6.set("")
            self.titleOf6.set("")
            self.pic6.set("")
        if(int(p)==5):
            self.priceOf1.set(rget['item1']['price_no_shipping'])
            self.titleOf1.set(rget['item1']['title'])
            self.pic1.set(rget['item1']['image_url'])
            self.priceOf2.set(rget['item2']['price_no_shipping'])
            self.titleOf2.set(rget['item2']['title'])
            self.pic2.set(rget['item2']['image_url'])
            self.priceOf3.set(rget['item3']['price_no_shipping'])
            self.titleOf3.set(rget['item3']['title'])
            self.pic3.set(rget['item3']['image_url'])
            self.priceOf4.set(rget['item4']['price_no_shipping'])
            self.titleOf4.set(rget['item4']['title'])
            self.pic4.set(rget['item4']['image_url'])
            self.priceOf5.set(rget['item5']['price_no_shipping'])
            self.titleOf5.set(rget['item5']['title'])
            self.pic5.set(rget['item5']['image_url'])
            self.priceOf6.set("")
            self.titleOf6.set("")
            self.pic6.set("")
        if(int(p)>=6):
            self.priceOf1.set(rget['item1']['price_no_shipping'])
            self.titleOf1.set(rget['item1']['title'])
            self.pic1.set(rget['item1']['image_url'])
            self.priceOf2.set(rget['item2']['price_no_shipping'])
            self.titleOf2.set(rget['item2']['title'])
            self.pic2.set(rget['item2']['image_url'])
            self.priceOf3.set(rget['item3']['price_no_shipping'])
            self.titleOf3.set(rget['item3']['title'])
            self.pic3.set(rget['item3']['image_url'])
            self.priceOf4.set(rget['item4']['price_no_shipping'])
            self.titleOf4.set(rget['item4']['title'])
            self.pic4.set(rget['item4']['image_url'])
            self.priceOf5.set(rget['item5']['price_no_shipping'])
            self.titleOf5.set(rget['item5']['title'])
            self.pic5.set(rget['item5']['image_url'])
            self.priceOf6.set(rget['item6']['price_no_shipping'])
            self.titleOf6.set(rget['item6']['title'])
            self.pic6.set(rget['item6']['image_url'])
        self.var1.set(0)
        self.var2.set(0)
        self.var3.set(0)
        self.var4.set(0)
        self.var5.set(0)
        self.var6.set(0)

    def addToWList(self):
        global pageNum
        global n
        item = self.mEntry.get()
        root.update_idletasks()
        json_data = requests.get("http://127.0.0.1:5000/search?search_param="+item+"&items_per_page=25&page_number="+str(pageNum)).json()
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

        if(self.var1.get()):
            data1 = {
            'itemId': firstID,
            'title': firstTitle,
            'price': firstPrice,
            'shipping': firstShipping,
            'country': firstCountry,
            'image_url': firstImage,
            'list_type': 1
            }
            rput1 =requests.put("http://127.0.0.2:5000/order66",data1)
            print(rput1)
        if(self.var2.get()):
            data2 = {
            'itemId': secondID,
            'title': secondTitle,
            'price': secondPrice,
            'shipping': secondShipping,
            'country': secondCountry,
            'image_url': secondImage,
            'list_type': 1
            }
            rput2 =requests.put("http://127.0.0.2:5000/order66",data2)
            print(rput2)
        if(self.var3.get()):
            data3 = {
            'itemId': thirdID,
            'title': thirdTitle,
            'price': thirdPrice,
            'shipping': thirdShipping,
            'country': thirdCountry,
            'image_url': thirdImage,
            'list_type': 1
            }
            rput3 =requests.put("http://127.0.0.2:5000/order66",data3)
            print(rput3)
        if(self.var4.get()):
            data4 = {
            'itemId': fourthID,
            'title': fourthTitle,
            'price': fourthPrice,
            'shipping': fourthShipping,
            'country': fourthCountry,
            'image_url': fourthImage,
            'list_type': 1
            }
            rput4 =requests.put("http://127.0.0.2:5000/order66",data4)
            print(rput4)
        if(self.var5.get()):
            data5 = {
            'itemId': fifthID,
            'title': fifthTitle,
            'price': fifthPrice,
            'shipping': fifthShipping,
            'country': fifthCountry,
            'image_url': fifthImage,
            'list_type': 1
            }
            rput5 =requests.put("http://127.0.0.2:5000/order66",data5)
            print(rput5)
        if(self.var6.get()):
            data6 = {
            'itemId': sixthID,
            'title': sixthTitle,
            'price': sixthPrice,
            'shipping': sixthShipping,
            'country': sixthCountry,
            'image_url': sixthImage,
            'list_type': 1
            }
            rput6 =requests.put("http://127.0.0.2:5000/order66",data6)
            print(rput6)
        if(self.var7.get()):
            data7 = {
            'itemId': firstID,
            'title': firstTitle,
            'price': firstPrice,
            'shipping': firstShipping,
            'country': firstCountry,
            'image_url': firstImage,
            'list_type': 2
            }
            print(7)
            rput7 =requests.put("http://127.0.0.2:5000/order66",data7)
            print(rput7)
        if(self.var8.get()):
            data8 = {
            'itemId': secondID,
            'title': secondTitle,
            'price': secondPrice,
            'shipping': secondShipping,
            'country': secondCountry,
            'image_url': secondImage,
            'list_type': 2
            }
            rput8 =requests.put("http://127.0.0.2:5000/order66",data8)
            print(rput8)
        if(self.var9.get()):
            data9 = {
            'itemId': thirdID,
            'title': thirdTitle,
            'price': thirdPrice,
            'shipping': thirdShipping,
            'country': thirdCountry,
            'image_url': thirdImage,
            'list_type': 2
            }
            rput9 =requests.put("http://127.0.0.2:5000/order66",data9)
            print(rput9)
        if(self.var10.get()):
            data10 = {
            'itemId': fourthID,
            'title': fourthTitle,
            'price': fourthPrice,
            'shipping': fourthShipping,
            'country': fourthCountry,
            'image_url': fourthImage,
            'list_type': 2
            }
            rput10 =requests.put("http://127.0.0.2:5000/order66",data10)
            print(rput10)
        if(self.var11.get()):
            data11 = {
            'itemId': fifthID,
            'title': fifthTitle,
            'price': fifthPrice,
            'shipping': fifthShipping,
            'country': fifthCountry,
            'image_url': fifthImage,
            'list_type': 2
            }
            rput11 =requests.put("http://127.0.0.2:5000/order66",data11)
            print(rput11)
        if(self.var12.get()):
            data12 = {
            'itemId': sixthID,
            'title': sixthTitle,
            'price': sixthPrice,
            'shipping': sixthShipping,
            'country': sixthCountry,
            'image_url': sixthImage,
            'list_type': 2
            }
            rput12 =requests.put("http://127.0.0.2:5000/order66",data12)
            print(rput12)
        self.var1.set(0)
        self.var2.set(0)
        self.var3.set(0)
        self.var4.set(0)
        self.var5.set(0)
        self.var6.set(0)
        self.var7.set(0)
        self.var8.set(0)
        self.var9.set(0)
        self.var10.set(0)
        self.var11.set(0)
        self.var12.set(0)
    def search(self):
        self.labelChange.set("Search")
        self.listName1.set("Watch List")
        self.listName2.set("Watch List")
        self.listName3.set("Watch List")
        self.listName4.set("Watch List")
        self.listName5.set("Watch List")
        self.listName6.set("Watch List")
        self.listName7.set("Ignore List")
        self.listName8.set("Ignore List")
        self.listName9.set("Ignore List")
        self.listName10.set("Ignore List")
        self.listName11.set("Ignore List")
        self.listName12.set("Ignore List")
        self.var1.set(0)
        self.var2.set(0)
        self.var3.set(0)
        self.var4.set(0)
        self.var5.set(0)
        self.var6.set(0)
        global pageNum
        print(pageNum)
        item = self.mEntry.get()
        root.update_idletasks()
        json_data = requests.get("http://127.0.0.1:5000/search?search_param="+item+"&items_per_page=25&page_number="+str(pageNum)).json()
        print(json_data)
        firstPrice = json_data['0']['price']
        firstTitle = json_data['0']['title']
        firstImage = json_data['0']['image_url']
        firstShippingCost = json_data['0']['shippingCost']['shippingServiceCost']['value']
        self.priceOf1.set(firstPrice)
        self.titleOf1.set(firstTitle)
        self.pic1.set(firstImage)
        self.sCost1.set(firstShippingCost)
        secondPrice = json_data['1']['price']
        secondTitle = json_data['1']['title']
        secondImage = json_data['1']['image_url']
        secondShippingCost = json_data['1']['shippingCost']['shippingServiceCost']['value']
        self.priceOf2.set(secondPrice)
        self.titleOf2.set(secondTitle)
        self.pic2.set(secondImage)
        self.sCost2.set(secondShippingCost)
        thirdPrice = json_data['2']['price']
        thirdTitle = json_data['2']['title']
        thirdImage = json_data['2']['image_url']
        thirdShippingCost = json_data['2']['shippingCost']['shippingServiceCost']['value']
        self.priceOf3.set(thirdPrice)
        self.titleOf3.set(thirdTitle)
        self.pic3.set(thirdImage)
        self.sCost3.set(thirdShippingCost)
        fourthPrice = json_data['3']['price']
        fourthTitle = json_data['3']['title']
        fourthImage = json_data['3']['image_url']
        fourthShippingCost = json_data['3']['shippingCost']['shippingServiceCost']['value']
        self.priceOf4.set(fourthPrice)
        self.titleOf4.set(fourthTitle)
        self.pic4.set(fourthImage)
        self.sCost4.set(fourthShippingCost)
        fifthPrice = json_data['4']['price']
        fifthTitle = json_data['4']['title']
        fifthImage = json_data['4']['image_url']
        fifthShippingCost = json_data['4']['shippingCost']['shippingServiceCost']['value']
        self.priceOf5.set(fifthPrice)
        self.titleOf5.set(fifthTitle)
        self.pic5.set(fifthImage)
        self.sCost5.set(fifthShippingCost)
        sixthPrice = json_data['5']['price']
        sixthTitle = json_data['5']['title']
        sixthImage = json_data['5']['image_url']
        sixthShippingCost = json_data['5']['shippingCost']['shippingServiceCost']['value']
        self.priceOf6.set(sixthPrice)
        self.titleOf6.set(sixthTitle)
        self.pic6.set(sixthImage)
        self.sCost6.set(sixthShippingCost)

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

        label = Label(self, text="Hadrian's Search")
        canvas.create_window(700, 50, window=label)
        #Mid box, Goes Bottom,left,right line
        canvas.create_line(50, 250, 1300, 250)
        canvas.create_line(50, 450, 1300, 450)
        canvas.create_line(50, 450, 50, 250)
        canvas.create_line(1300, 450, 1300, 250)
        #Little Box Goes Top,Bottom,left,right line
        #Mid box, Goes Bottom,left,right line
        canvas.create_line(50, 650, 1300, 650)
        canvas.create_line(50, 650, 50, 450)
        canvas.create_line(1300, 650, 1300, 450)
        #Little Box Goes Top,Bottom,left,right line
        #Mid box, Goes Bottom,left,right line
        canvas.create_line(50, 850, 1300, 850)
        canvas.create_line(50, 850, 50, 650)
        canvas.create_line(1300, 850, 1300, 650)
        #Little Box Goes Top,Bottom,left,right line
        #Mid box, Goes Bottom,left,right line
        canvas.create_line(50, 1050, 1300, 1050)
        canvas.create_line(50, 1050, 50, 850)
        canvas.create_line(1300, 1050, 1300, 850)
        #Little Box Goes Top,Bottom,left,right line
        #Mid box, Goes Bottom,left,right line
        canvas.create_line(50, 1250, 1300, 1250)
        canvas.create_line(50, 1250, 50, 850)
        canvas.create_line(1300, 1250, 1300, 1050)
        #Little Box Goes Top,Bottom,left,right line
        canvas.create_line(50, 1450, 1300, 1450)
        canvas.create_line(50, 1450, 50, 1050)
        canvas.create_line(1300, 1450, 1300, 1250)
        #Little Box Goes Top,Bottom,left,right line
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
        #Price:
        priceTitle1= Label(canvas, text="Price: ")
        canvas.create_window(280, 300, window=priceTitle1)
        priceTitle2= Label(canvas, text="Price: ")
        canvas.create_window(280, 500, window=priceTitle2)
        priceTitle3= Label(canvas, text="Price: ")
        canvas.create_window(280, 700, window=priceTitle3)
        priceTitle4= Label(canvas, text="Price: ")
        canvas.create_window(280, 900, window=priceTitle4)
        priceTitle5= Label(canvas, text="Price: ")
        canvas.create_window(280, 1100, window=priceTitle5)
        priceTitle6= Label(canvas, text="Price: ")
        canvas.create_window(280, 1300, window=priceTitle6)
        #Price
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
        #Shipping Cost:
        shippingTitle1= Label(canvas, text="Shipping Cost: ")
        canvas.create_window(270, 325, window=shippingTitle1)
        shippingTitle2= Label(canvas, text="Shipping Cost: ")
        canvas.create_window(270, 525, window=shippingTitle2)
        shippingTitle3= Label(canvas, text="Shipping Cost: ")
        canvas.create_window(270, 725, window=shippingTitle3)
        shippingTitle4= Label(canvas, text="Shipping Cost: ")
        canvas.create_window(270, 925, window=shippingTitle4)
        shippingTitle5= Label(canvas, text="Shipping Cost: ")
        canvas.create_window(270, 1125, window=shippingTitle5)
        shippingTitle6= Label(canvas, text="Shipping Cost: ")
        canvas.create_window(270, 1325, window=shippingTitle6)
        #ShippingCost
        self.sCost1=StringVar()
        self.sCost2=StringVar()
        self.sCost3=StringVar()
        self.sCost4=StringVar()
        self.sCost5=StringVar()
        self.sCost6=StringVar()
        costofShipping1= Label(canvas, text="Price Here", textvariable=self.sCost1)
        canvas.create_window(320, 325, window=costofShipping1)
        costofShipping2= Label(canvas, text="Price Here", textvariable=self.sCost2)
        canvas.create_window(320, 525, window=costofShipping2)
        costofShipping3= Label(canvas, text="Price Here", textvariable=self.sCost3)
        canvas.create_window(320, 725, window=costofShipping3)
        costofShipping4= Label(canvas, text="Price Here", textvariable=self.sCost4)
        canvas.create_window(320, 925, window=costofShipping4)
        costofShipping5= Label(canvas, text="Price Here", textvariable=self.sCost5)
        canvas.create_window(320, 1125, window=costofShipping5)
        costofShipping6= Label(canvas, text="Price Here", textvariable=self.sCost6)
        canvas.create_window(320, 1325, window=costofShipping6)
        #WatchList Check box
        self.var1 = IntVar()
        self.var2 = IntVar()
        self.var3 = IntVar()
        self.var4 = IntVar()
        self.var5 = IntVar()
        self.var6 = IntVar()
        self.listName1=StringVar()
        self.listName2=StringVar()
        self.listName3=StringVar()
        self.listName4=StringVar()
        self.listName5=StringVar()
        self.listName6=StringVar()
        self.listName1.set("Watch List")
        self.listName2.set("Watch List")
        self.listName3.set("Watch List")
        self.listName4.set("Watch List")
        self.listName5.set("Watch List")
        self.listName6.set("Watch List")
        box1 = Checkbutton(canvas, text="Watch list", variable=self.var1, textvariable=self.listName1)
        canvas.create_window(300, 380, window=box1)
        box2 = Checkbutton(canvas, text="Watch list", variable=self.var2, textvariable=self.listName2)
        canvas.create_window(300, 580, window=box2)
        box3 = Checkbutton(canvas, text="Watch list", variable=self.var3, textvariable=self.listName3)
        canvas.create_window(300, 780, window=box3)
        box4 = Checkbutton(canvas, text="Watch list", variable=self.var4, textvariable=self.listName4)
        canvas.create_window(300, 980, window=box4)
        box5 = Checkbutton(canvas, text="Watch list", variable=self.var5, textvariable=self.listName5)
        canvas.create_window(300, 1180, window=box5)
        box6 = Checkbutton(canvas, text="Watch list", variable=self.var6, textvariable=self.listName6)
        canvas.create_window(300, 1380, window=box6)
        #Ignore list check box
        self.var7 = IntVar()
        self.var8 = IntVar()
        self.var9 = IntVar()
        self.var10 = IntVar()
        self.var11 = IntVar()
        self.var12 = IntVar()
        self.listName7=StringVar()
        self.listName8=StringVar()
        self.listName9=StringVar()
        self.listName10=StringVar()
        self.listName11=StringVar()
        self.listName12=StringVar()
        self.listName7.set("Ignore List")
        self.listName8.set("Ignore List")
        self.listName9.set("Ignore List")
        self.listName10.set("Ignore List")
        self.listName11.set("Ignore List")
        self.listName12.set("Ignore List")
        box7 = Checkbutton(canvas, text="Ignore list", variable=self.var7, textvariable=self.listName7)
        canvas.create_window(300, 400, window=box7)
        box8 = Checkbutton(canvas, text="Ignore list", variable=self.var8, textvariable=self.listName8)
        canvas.create_window(300, 600, window=box8)
        box9 = Checkbutton(canvas, text="Ignore list", variable=self.var9, textvariable=self.listName9)
        canvas.create_window(300, 800, window=box9)
        box10 = Checkbutton(canvas, text="Ignore list", variable=self.var10, textvariable=self.listName10)
        canvas.create_window(300, 1000, window=box10)
        box11 = Checkbutton(canvas, text="Ignore list", variable=self.var11, textvariable=self.listName11)
        canvas.create_window(300, 1200, window=box11)
        box12 = Checkbutton(canvas, text="Ignore list", variable=self.var12, textvariable=self.listName12)
        canvas.create_window(300, 1400, window=box12)
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
        canvas.create_window(800, 1550, window=wListNextPage)
        iListNextPage = Button(canvas, text="Ignore List Next Page", command=self.iListNext)
        canvas.create_window(800, 1600, window=iListNextPage)
        #Previous Page button
        prevPage = Button(canvas, text="Previous Page", command=prev)
        canvas.create_window(600, 1500, window=prevPage)
        wListprevPage = Button(canvas, text="Watch List Previous Page", command=self.showWList)
        canvas.create_window(600, 1550, window=wListprevPage)
        iListprevPage = Button(canvas, text="Ignore List Previous Page", command=self.showIList)
        canvas.create_window(600, 1600, window=iListprevPage)
        #Show Ignore list
        showWatch = Button(canvas, text="Show Watch List", command=self.showWList)
        canvas.create_window(800, 1500, window=showWatch)
        showIgnore = Button(canvas, text="Show Ignore List", command=self.showIList)
        canvas.create_window(900, 1500, window=showIgnore)
        #Delete From List
        deleteFromWatch = Button(canvas, text="Delete From Watch List", command=self.deleteFromWList)
        canvas.create_window(450, 1500, window=deleteFromWatch)

        deleteFromIgnore = Button(canvas, text="Delete From Ignore List", command=self.deleteFromIList)
        canvas.create_window(450, 1550, window=deleteFromIgnore)
        #Picture Button
        self.pic1 = StringVar()
        self.pic2 = StringVar()
        self.pic3 = StringVar()
        self.pic4 = StringVar()
        self.pic5 = StringVar()
        self.pic6 = StringVar()
        self.pic1.set("Show Picture")
        self.pic2.set("Show Picture")
        self.pic3.set("Show Picture")
        self.pic4.set("Show Picture")
        self.pic5.set("Show Picture")
        self.pic6.set("Show Picture")
        showPicture1 = Button(canvas, text="Show Picture", textvariable=str(self.pic1))
        showPicture1.bind("<Button-1>", self.callPic)
        canvas.create_window(300, 350, window=showPicture1)
        showPicture2 = Button(canvas, text="Show Picture", textvariable=str(self.pic2))
        showPicture2.bind("<Button-1>", self.callPic)
        canvas.create_window(300, 550, window=showPicture2)
        showPicture3 = Button(canvas, text="Show Picture", textvariable=str(self.pic3))
        showPicture3.bind("<Button-1>", self.callPic)
        canvas.create_window(300, 750, window=showPicture3)
        showPicture4 = Button(canvas, text="Show Picture", textvariable=str(self.pic4))
        showPicture4.bind("<Button-1>", self.callPic)
        canvas.create_window(300, 950, window=showPicture4)
        showPicture5 = Button(canvas, text="Show Picture", textvariable=str(self.pic5))
        showPicture5.bind("<Button-1>", self.callPic)
        canvas.create_window(300, 1150, window=showPicture5)
        showPicture6 = Button(canvas, text="Show Picture", textvariable=str(self.pic6))
        showPicture6.bind("<Button-1>", self.callPic)
        canvas.create_window(300, 1350, window=showPicture6)
        #Update list
        getNum = Button(canvas, text="Add To List", command=self.addToWList)
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
