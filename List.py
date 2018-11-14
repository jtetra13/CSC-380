import flask
import flask_restful
import ebaysdk
import json
import fileinput


# expect dictionary that takes in title, price, itemId, country
# input_dict = {
#	"title" : "ball",
#	"price" : { price_no_shipping : 8.40 , price_with_shipping : 9.30 } # change this here 
#	"itemId" : 102,
#	"country" : "America"

# example file:
# >
# itemId,102
# title,ball
# price,7.50
# country,America
# >
# itemId,430
# title,harry potter
# price,3.20 ... 

class List:
    def add(input_dict):
        f = open('watch_list.txt', 'a+')

        index = 4
        for key in input_dict:
            if index % 4 == 0:
                f.write('>' + key + ',' + input_dict[key] + '\n')
                index += 1
            else:
                if isinstance(input_dict[key], dict):
                    for key2, value2 in input_dict[key].items():
                        f.write(key2 + ',' + value2 + '\n')
                else:
                    f.write(key + ',' + input_dict[key] + '\n')
        f.close()

    def delete(itemId):
        try:
            f = fileinput.input('watch_list.txt', inplace=True)

            for line in f:
                if "itemId," + itemId in line:
                    for _ in range(4):
                        next(f, None)
                else:
                    print(line, end='\r')
            f.close()
        except IOError as e:
            print('File does not exist, cannot delete item. \n')

# hardcode for testing
# example = {"itemId" : "102", "title" : "ball", "price" : {"price_no_shipping" : "7.50", "price_with_shipping" : "8.23"}, "country" : "America"}
# example2 = {"itemId" : "798", "title" : "basket", "price" : {"price_no_shipping" : "2.50", "price_with_shipping" : "5.32"}, "country" : "Japan"}

# testing
# List.add(example)
# List.add(example2)
# List.delete("102")
