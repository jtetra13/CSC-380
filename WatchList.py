from LocalFile import LocalFile as Locally


class WatchList(Locally):
    def __init__(self):
        self.list_name = "watch_list.txt"
        super().init_file( self.list_name)

    def add_item(self, item_dict):
        if WatchList.check_item_exist(self, item_dict['itemId'], self.list_name) is not True:
            resp = WatchList.add(self, item_dict, self.list_name)
            if resp is True:
                return True
            else:
                return False
        else:
            return False

    def delete_item(self, item_dict):
        tmp_id = item_dict['itemId']
        if self.check_item_exist(tmp_id,self.list_name) is not True:
            self.delete(item_dict['itemId'],self.list_name)
            if self.check_item_exist(tmp_id,self.list_name) is True:
                return False  # throw custom error
            else:
                return  True
        else:
            return False

    # returns the dict of items in the watch list
    def dump_list(self):
        resp = self.dump_dict(self.list_name)
        if resp is not False:
            return resp  # keep it consistent
        else:
            return False

    # checks to see if product list is empty
    def check_if_file_empty(self):
        # empty dics eval to false
        resp = WatchList.dump_dict(self,self.list_name)
        if bool(resp) is not False :
            return False
        else:
            return True
