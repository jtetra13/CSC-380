import LocalFile

class watchList:
    def __init__(self):
        # creates the path to the persistent file
        self.watch_men = LocalFile.LocalFile()
        self.product_list = self.load_watch_list()

    # this method loads the watchlist from the file into memory.
    def load_watch_list(self):
        self.watch_men.init_file()
        live_watch_list = self.watch_men.dump_dict()
        if live_watch_list is False:
            # the dump dict didn't return any values
            return dict()
        else:
            return live_watch_list

    def add_item(self, item_dict):
            if item_dict['itemId'] in self.product_list:
                return False  # this values already exists
            else:
                try:
                    self.product_list[item_dict['itemId']] = item_dict
                    self.watch_men.add(item_dict)
                    return True
                except:
                    return 444
    def delete_item(self, item_dict):
        tmp_id = item_dict['itemId']
        try:
            if self.check_if_memory_empty() is False:
                del self.product_list[item_dict['itemId']]
                self.watch_men.delete(item_dict['itemId'])
        except:
            return 444  # means it didn;t find the key so exception raised
        if tmp_id in self.product_list:
            return False  # throw custom error
        else:
            return True

    # returns the dict of items in the watch list
    def dump_list(self):
        resp = self.watch_men.dump_dict()
        if resp is not False:
            return resp  # keep it consistent
        else:
            return dict()

    # checks to see if product list is empty
    def check_if_file_empty(self):
        # empty dics eval to false
        resp = self.watch_men.dump_dict()
        if resp is False:
            return True
        else:
            return False
    def check_if_memory_empty(self):
        if self.product_list is False:
            return True
        else:
            return False
