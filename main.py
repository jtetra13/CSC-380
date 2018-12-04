from flask import Flask, redirect, request, Response, jsonify, url_for, render_template
from flask_restful import Resource, Api, reqparse
from ebaysdk.finding import Connection as Finding
import WatchList, IgnoreList

app = Flask(__name__)
api = Api(app)
watch_list = WatchList.WatchList()
ignore_list = IgnoreList.IgnoreList()
# this parser is going to be depreciated but limiting additional dependecies
parser = reqparse.RequestParser()
gui_parser = reqparse.RequestParser()
order66_parser = reqparse.RequestParser()

order66_parser.add_argument('list_type', type=int)

gui_parser.add_argument('title', required=True)
gui_parser.add_argument('price', required=True)
gui_parser.add_argument('itemId', required=True)
gui_parser.add_argument('country', required=True)
gui_parser.add_argument('shipping', required=True)
gui_parser.add_argument('image_url', required=True)
gui_parser.add_argument('list_type', type=int)

parser.add_argument('search_param', action='append', required=True)  # user string
parser.add_argument('items_per_page', type=int, required=True)
parser.add_argument('page_number', type=int, required=True)


def custom_error(stat_code, msg, action):
    error_msg = jsonify({
        'status': stat_code,
        'message': msg,
        'action': action
    })
    error_msg.stat_code = stat_code  # this way we can reference it
    return error_msg


def gen_custom_search(user_param, ):
    # user_param will be a dict
    custom_search = {

        'keywords': user_param['search_terms'],
        'paginationInput': {
            'entriesPerPage': user_param['pages']['entries_per_page'],
            'pageNumber': user_param['pages']['page_number']
        },
        'sortOrderType': 'BestMatch',
        'itemFilter': {
            'name': 'HideDuplicateItems',
            'value': True},
        'descriptionSearch': 'True',
    }
    return custom_search


def parse_params_api_search():
    dikta = dict()
    returned_args = parser.parse_args()
    dikta['search_terms'] = ''.join(returned_args['search_param'])
    dikta['pages'] = dict(
        [('entries_per_page', returned_args['items_per_page']), ('page_number', returned_args['page_number'])])
    dikta['advanced'] = None  # reach goal for gui
    return dikta


def parse_order66_get():
    stalin = dict()
    ret_args = order66_parser.parse_args()
    stalin['list_type'] = ret_args['list_type']
    return stalin


def parse_params_gui_query():
    nikta = dict()
    ret_args = gui_parser.parse_args()
    nikta['itemId'] = ret_args['itemId']
    nikta['url']=ret_args['viewItemURL']
    nikta['title'] = ret_args['title']
    nikta['price'] = dict([('price_no_shipping', ret_args['price']), ('price_shipping', ret_args['shipping'])])
    nikta['country'] = ret_args['country']
    nikta['image_url'] = ret_args['image_url']
    if ret_args['list_type'] is not None:
        nikta['list_type'] = ret_args['list_type']
    else:
        nikta['list_type'] = None
    return nikta


def generate_json_for_gui(response, max_query, user_args):
    # the input will be the dict of the response from api
    # the examples are a translation to a dic
    # this block parses the result,future fields added here
    ignore_resp = GuiQuery.ignore_list_get(GuiQuery)
    parsed_dic = {}
    setty =None
    if isinstance(ignore_resp, Response):
            ignore_resp = {'item1': {'itemId': '1111111111111111111'}}
            setty = {ignore_resp['item1']['itemId']}
    else:
        ignore_list_tmp =ignore_resp.values()
        setty = {x['itemId'] for x in ignore_list_tmp}
    count=0
    for x in range(max_query):
        if setty.__contains__(response[x]['itemId']) is False:
            parsed_dic[count] = {}
            parsed_dic[count]['country'] = response[x].get("country", None)
            parsed_dic[count]['user_args'] = user_args
            parsed_dic[count]['itemId'] = response[x].get("itemId", None)
            parsed_dic[count]['url']=response[x].get('viewItemURL',None)
            parsed_dic[count]["title"] = response[x].get("title", None)
            parsed_dic[count]["price"] = response[x].get("sellingStatus", None).get("convertedCurrentPrice", None).get(
                "value", None)
            parsed_dic[count]['image_url'] = response[x].get("galleryURL", None)
            parsed_dic[count]["shippingCost"] = response[x].get("shippingInfo", None)
            count+=1
        else:
            pass
    return jsonify(parsed_dic)


def check_if_resp_empty(response):
    amount_of_products = response["searchResult"]["_count"]
    print(response['searchResult'])
    if int(amount_of_products) > 0:
        return response["searchResult"]['item'], int(amount_of_products)
    else:
        return custom_error(444, "No results found", "new_search"),0


# Ebay Sdk Pratice
class EbayTesting(Resource):
    def get(self):
        api = Finding(config_file="ebay.yaml")
        user_param = parse_params_api_search()
        custom_search = gen_custom_search(user_param)
        response = api.execute('findItemsAdvanced', custom_search)
        ebay_response = response.dict()

        if "Failure" in ebay_response['ack']:
            return custom_error(400, "Not a valid search.", "Try a different search ")
        # sandbox had some issues returning a response with no entries
        ebay_response, count = check_if_resp_empty(ebay_response)

        if isinstance(ebay_response, Response):
            return ebay_response
        else:
            return generate_json_for_gui(ebay_response, count, user_param)  # custom_search does have the dict


class GuiQuery(Resource):
    # remove the requested objected
    def watch_list_delete(self, parse_res):
        if watch_list.check_if_file_empty() is not True:
            reznov = watch_list.delete_item(parse_res)
            if reznov is True:
                return 200
            elif reznov == 444:
                return custom_error(444, "Key doesn't exist", "nothing")
            else:
                return custom_error(reznov, "The action failed to delete the item", "repeat_action")
        else:
            return custom_error(404, "the watchlist is empty. This action isnt legal", "display_empty")

    def ignore_list_delete(self, parse_res):
        if ignore_list.check_if_file_empty() is not True:
            reznov = ignore_list.delete_item(parse_res)
            if reznov is True:
                return 200
            elif reznov == 444:
                return custom_error(444, "Key doesn't exist", "nothing")
            else:
                return custom_error(reznov, "The action failed to delete the item", "repeat_action")

        else:
            return custom_error(404, "the ignorelist is empty. This action isnt legal", "display_empty")

    def delete(self):
        parse_res = parse_params_gui_query()
        if parse_res['list_type'] == 1:
            return self.watch_list_delete(parse_res)
        elif parse_res['list_type'] == 2:
            return self.ignore_list_delete(parse_res)
        else:
            return custom_error(40, "the provided values is not valid.Pick 1 for watchlist and 2 for ignoreList",
                                "repick")

    def watch_list_put(self, parse_result):
        resp = watch_list.add_item(parse_result)
        if resp is False:
            return resp
        else:
            return 200

    def ignore_list_put(self, parse_result):
        resp = ignore_list.add_item(parse_result)
        if resp is False:
            return resp
        else:
            return 200

    def put(self):
        parse_result = parse_params_gui_query()
        resp = None
        if parse_result['list_type'] == 1:
            # print(parse_result)
            resp = self.watch_list_put(parse_result)
        elif parse_result['list_type'] == 2:
            resp = self.ignore_list_put(parse_result)
        else:
            return custom_error(400, "no list picked", "no_action")
        if resp is not False:
            return resp
        else:
            return custom_error(400, "item already exists", "no_action")

    def watch_list_get(self):
        if watch_list.check_if_file_empty() is False:
            return watch_list.dump_list()
        return custom_error(404, "the dic is empty", "display_empty")

    def ignore_list_get(self):
        if ignore_list.check_if_file_empty() is False:
            return ignore_list.dump_list()
        print("ignore mate")
        zz = custom_error(404, "the dic is empty", "display_empty")
        print(zz.stat_code)
        return zz

    def get(self):
        # get the requested element
        parse_result = parse_order66_get()
        if parse_result['list_type'] == 1:
            return self.watch_list_get()
        elif parse_result['list_type'] == 2:
            return self.ignore_list_get()
        else:
            return False


api.add_resource(EbayTesting, '/search')  # this is for the watchlists
api.add_resource(GuiQuery, '/order66')  # this is for the query
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
