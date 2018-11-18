import flask
import flask_restful
import ebaysdk
import json
import fileinput


# expect dictionary that takes in title, price, itemId, country
# input_dict = {
#   "title" : "ball",
#   "price" : { price_no_shipping : 8.40 , price_with_shipping : 9.30 } # change this here 
#   "itemId" : 102,
#   "country" : "America"

# example file:
# >
# itemId,102
# title,ball
# price_no_shipping,7.50
# price_with_shipping,9.30
# country,America
# >
# itemId,430
# title,harry potter
# price_no_shipping,3.20
# price_with_shipping,3.40
# country,Japan

class List:
    def add(input_dict):
        f = open('watch_list.txt', 'a+')

        index = 5
        for key in input_dict:
            if index % 5 == 0:
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

    def print_dict():
        try:
            f = fileinput.input('watch_list.txt')
            inner_param_dict_name = 'price'
            watch_list = dict()
            counter = 0
            # watch_list[inner_param_dict_name] = dict()

            for line in f:
                if line.startswith('>'):
                    counter += 1
                    watch_list['item' + str(counter)] = dict()
                    list_input = line[1:].strip().split(',')
                    watch_list['item' + str(counter)][list_input[0]] = list_input[1]
                else:
                    list_input = line.strip().split(',')
                    watch_list['item' + str(counter)][list_input[0]] = list_input[1]
            f.close()
            print(watch_list)

        except IOError as e:
            print('File does not exist, no items in the watchlist. \n')

# example of print dict:
# {'item1': {'itemId': '102', 'title': 'ball', 'price_no_shipping': '7.50', 'price_with_shipping': '8.23', 'country': 'America'}, 'item2': {'itemId': '798', 'title': 'basket', 'price_no_shipping': '2.50', 'price_with_shipping': '5.32', 'country': 'Japan'}}
# example = {"itemId" : "102", "title" : "ball", "price" : {"price_no_shipping" : "7.50", "price_with_shipping" : "8.23"}, "country" : "America"}
# example2 = {"itemId" : "798", "title" : "basket", "price" : {"price_no_shipping" : "2.50", "price_with_shipping" : "5.32"}, "country" : "Japan"}

# testing
# List.add(example)
# List.add(example2)
# List.delete("102")
# List.print_dict()
