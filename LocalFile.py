import fileinput

class LocalFile:
    def init_file(self):
        f = open('watch_list.txt', 'a+')
        f.close()
    def add(self,input_dict):
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
                    f.write(str(key) + ',' + str(input_dict[key]) + '\n')
        f.close()

    def delete(self,itemId):
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

    def dump_dict(self):
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
            if watch_list is False:
                return False
            else:
                return watch_list

        except IOError as e:
            print('File does not exist, no items in the watchlist. \n')

