from LocalFile import LocalFile as Locally


class IgnoreList(Locally):
    def __init__(self):
        super().init_file( "ignore_list.txt")
        self.list_type = "ignore_list.txt"

    def add_item(self, item_dict):
        if IgnoreList.check_item_exist(self, item_dict['itemId'], "ignore_list.txt") is not True:
            resp = IgnoreList.add(self, item_dict, "ignore_list.txt")
            if resp is True:
                return resp
            else:
                return resp
        else:
            return False

    def delete_item(self, item_dict):
        tmp_id = item_dict['itemId']
        if self.check_item_exist(tmp_id, self.list_type) is not True:
            self.delete( item_dict['itemId'], "ignore_list.txt")
            if self.check_item_exist( tmp_id, "ignore_list.txt") is True:
                return False
            else:
                return True
        else:
            return False


    def dump_list(self):
        resp = self.dump_dict(self.list_type)
        if resp is not False:
            return resp  # keep it consistent
        else:
            return dict()

    def check_if_file_empty(self):
        # empty dics eval to false
        resp = IgnoreList.dump_dict(self,self.list_type)
        if resp is not False:
            return False
        else:
            return True
