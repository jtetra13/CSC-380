from flask import Flask, redirect, request, Response, jsonify, url_for
from flask_restful import Resource, Api, reqparse
from ebaysdk.finding import Connection as Finding
import json, WatchList

app = Flask(__name__)
api = Api(app)
watch_list = WatchList.watchList()
# this parser is going to be depreciated but limiting additional dependecies
parser = reqparse.RequestParser()
gui_parser = reqparse.RequestParser()

gui_parser.add_argument('title', required=True)
gui_parser.add_argument('price', required=True)
gui_parser.add_argument('itemId', required=True)
gui_parser.add_argument('country', required=True)
gui_parser.add_argument('shipping', required=True)

parser.add_argument('search_param', action='append', required=True)  # user string
parser.add_argument('items_per_page', type=int, required=False)
parser.add_argument('page_number', type=int, required=False)


def custom_error(stat_code, msg, action):
    error_msg = jsonify({
        'status': stat_code,
        'message': msg,
        'action': action
    })
    error_msg.stat_code = stat_code  # this way we can reference it
    return error_msg


def gen_custom_search(user_param):
    # user_param will be a dict
    custom_search = {

        'keywords': '(ball,harry)',
        'paginationInput': {
            'entriesPerPage': 50,
            'pageNumber': 2
        },
        'itemFilter': {
            "name": "FreeShippingOnly",
            "value": "true"
        }
    }
    return custom_search


def parse_params_api_search():
    dikta = dict()
    returned_args = parser.parse_args()
    dikta['search_terms'] = (dict(enumerate(returned_args['search_param'])))
    dikta['pages'] = dict(
        [('entries_per_page', returned_args['items_per_page']), ('page_number', returned_args['page_number'])])
    dikta['advanced'] = None;  # reach goal for gui
    return dikta


def parse_params_gui_query():
    nikta = dict()
    ret_args = gui_parser.parse_args()
    nikta['title'] = ret_args['title']
    nikta['price'] = dict([('price_no_shipping', ret_args['price']), ('price_shipping', ret_args['shipping'])])
    nikta['itemId'] = ret_args['itemId']
    nikta['country'] = ret_args['country']
    return nikta


def generate_json_for_gui(response, max_query, user_args):
    # the input will be the dict of the response from api
    # the examples are a translation to a dic
    parsed_dic = {}
    for x in range(max_query):
        parsed_dic[x] = {}
        parsed_dic[x]['user_args'] = user_args
        parsed_dic[x]["title"] = response[x].get("title", None)
        parsed_dic[x]["price"] = response[x].get("sellingStatus", None).get("convertedCurrentPrice", None).get("value",
                                                                                                               None)
        parsed_dic[x]["totalPrice"] = response[x].get("shippingInfo", None).get("shippingServiceCost", None).get(
            "value", None)
    return jsonify(parsed_dic)


# Ebay Sdk Pratice
class EbayTesting(Resource):
    def get(self, search_term):
        # this will be changed since we will get query from the gui,parse it from the endpoint
        # craft the custom api request , parse the response from ebay and pass the dict/json to gui
        # added the appid since its for the sandbox mode and doesn't pose a major risk
        api = Finding(domain='svcs.sandbox.ebay.com', appid="AdrianNa-CSC380-SBX-ec22ddb1d-3bd0ef52",
                      config_file="myebay.yaml")
        user_param = parse_params_api_search()
        custom_search = gen_custom_search(user_param)
        response = api.execute('findItemsAdvanced', custom_search)
        if response is None:
            return custom_error(400, "Couldn't connect to Ebay", "check your connection")
        response = response.dict()
        response = response["searchResult"]["item"]
        with open('dummyJson.txt', 'w') as outy:
            json.dump(response, outy)
        return generate_json_for_gui(response, 20, user_param)  # custom_search does have the dict


dic = {"asdas": "ASfwregfef"}


class GuiQuery(Resource):
    # remove the requested objected
    def delete(self, name):
        parse_res = parse_params_gui_query()
        if watch_list.check_if_empty():
            return custom_error(404,"the watchlist is empty. This action isnt legal","display_empty")
        else:
            reznov = watch_list.delete_item(parse_res)
            if reznov is True:
                return 200
            elif reznov == 444: return custom_error(444,"Key doesn't exist","nothing")
            else:return custom_error(reznov,"The action failed to delete the item","repeat_action")


    def put(self, name):
        parse_result = parse_params_gui_query()
        watch_list.add_item(parse_result)
        return 200

    def get(self, name):
        # get the requested element
        if watch_list.check_if_empty():
            return custom_error(404, "the dic is empty", "display_empty")
        return watch_list.dump_list()


api.add_resource(EbayTesting, '/<string:search_term>')
api.add_resource(GuiQuery, '/order66/<string:name>')
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
