import fileinput

class LocalFile:
    def init_file(self,file_name):
        f = open(file_name, 'a+')
        f.close()

    def add(self,input_dict,file_name):
        if input_dict.get('itemId') in open(file_name).read():
            return False
 
        f = open(file_name, 'a+')
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
                    f.write(str(key) + ',' + str(input_dict[key]) + '\n')
        f.close()
        return True

    def delete(self,itemId,file_name):
        watch_list = self.dump_dict(file_name)

        try:
            f = fileinput.input(file_name, inplace=True)

            for line in f:
                if "itemId," + itemId in line:
                    for _ in range(6):
                        next(f, None)
                else:
                    print(line, end='\r')
            f.close()
        except IOError as e:
            print('File does not exist, cannot delete item. \n')

    def check_item_exist(self,itemId,file_name):
        res = self.dump_dict(file_name)
        if itemId in res:
            return True
        else: return False

    def dump_dict(self,file_name):
        try:
            f = fileinput.input(file_name)
            watch_list = dict()
            inner_dict = dict()
            
            item_counter = 1
            line_counter = 0
            itemName = "item" + str(item_counter)
            for line in f:
                if line.startswith('>'):   
                    list_input = line[1:].strip().split(',')
                    inner_dict[list_input[0]] = list_input[1] 
                    line_counter = line_counter + 1
                elif line != '\n':
                    list_input = line.strip().split(',')
                    inner_dict[list_input[0]] = list_input[1]
                    line_counter = line_counter + 1

                if line_counter % 7 == 0:
                    watch_list[itemName] = inner_dict 
                    inner_dict = {}
                    item_counter = item_counter + 1
                    itemName = "item" + str(item_counter)

            f.close()

            return watch_list
        except IOError as e:
            return False

#debugging
#lf = LocalFile()
#print(lf.dump_dict())
#print(" ")
#lf.delete("273547574855")
#print(lf.dump_dict())

#{'item1': {'itemId': '273547574855', 'title': 'Toys For Boys Kids Children Soccer Hover Ball for 3 4 5 6 7 8 9 10 Years Old Age', 'price_no_shipping': '10.99', 'price_shipping': 'Worldwide', 'country': 'US', 'image_url': 'http://thumbs4.ebaystatic.com/m/m8h89jcoptNACQ2ZpztZn1Q/140.jpg', 'list_type': '1'}, 'item2': {'itemId': '182482406482', 'title': 'Small Dog Clothes Pet Winter Plaid Sweater Puppy Clothing Warm Apparel Coat', 'price_no_shipping': '13.1', 'price_shipping': 'Worldwide', 'country': 'US', 'image_url': 'http://thumbs3.ebaystatic.com/pict/1824824064824040_3.jpg', 'list_type': '1'}}
