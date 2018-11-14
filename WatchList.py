import List

persity = List.List()

class watchList:
    def __init__(self):
        # constructor for the class essentially
        self.product_list = {}

    def dump_list(self):
        if self.product_list is None:
            return {}
        else:
            
            return self.product_list

    def add_item(self, item_dict):
        self.product_list[item_dict['itemId']] = item_dict
        persity.add(item_dict)
        if item_dict['itemId'] in self.product_list:
            return True
        else:
            False

    def delete_item(self, item_dict):
        tmp_id = item_dict['itemId']
        try:
            del self.product_list[item_dict['itemId']]
        except:
            return 444  # means it didn;t find the key so exception raised
        if tmp_id in self.product_list:
            return False
        else:
            return True

    def print_watch_list(self):
        for i, z in self.product_list.items():
            print(i, z)

    # checks to see if product list is empty
    def check_if_empty(self):
        if self.product_list is None:
            return True
        else:
            return False
