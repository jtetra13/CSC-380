from flask import Flask, redirect, request, Response, jsonify, url_for
from flask_restful import Resource, Api, reqparse
from ebaysdk.finding import Connection as Finding
import json

app = Flask(__name__)
api = Api(app)
# this parser is going to be depreciated but limiting additional dependecies
parser = reqparse.RequestParser()
parser.add_argument('search_param', type=str)


def custom_error(stat_code, msg, action):
    error_msg = jsonify({
        'status': stat_code,
        'message': msg,
        'action': action
    })
    error_msg.stat_code = stat_code  # this way we can reference it
    return error_msg


def generate_request_dict(key_words):
    # this will be to craft custom search query
    print(key_words)

def gen_custom_search(user_param):
        #user_param will be a dict
        custom_search = {

        'keywords' : '(ball,harry)',
        'paginationInput':{
            'entriesPerPage':50,
            'pageNumber':1
        },
        'itemFilter':{
            "name":"FreeShippingOnly",
            "value":"true"
            },
       "testing":user_param }
        return custom_search

def parse_params():
    returned_args = parser.parse_args()
    if returned_args['search_param'] is not None:
        listy = returned_args['search_param'].split(',')
        dikta = dict.fromkeys(listy)
        return  dikta
    else:
        listy = None
        return listy
def generate_json_for_gui(response, max_query):
    # the input will be the dict of the response from api
    # the examples are a translation to a dic
    parsed_dic = {}
    for x in range(max_query):
        parsed_dic[x] = {}
        parsed_dic[x]['parsed'] = None
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
        # remove the following from appid,drgerGERGeergewrgSdfwegfoiergi
        # added the appid since its for the sandbox mode and doesn't pose a major risk
        api = Finding(domain='svcs.sandbox.ebay.com', appid="AdrianNa-CSC380-SBX-ec22ddb1d-3bd0ef52",
                      config_file="myebay.yaml")
        user_param = parse_params()
        custom_search = gen_custom_search(user_param)

        response = api.execute('findItemsAdvanced',custom_search )
        if response is None:
            return 400
        response = response.dict()
        response = response["searchResult"]["item"]
        return generate_json_for_gui(response, 10) #custom_search does have the dict


dic = {}


class GuiQuery(Resource):
    # remove the requested objected
    def delete(self, name):
        dic.pop(name)
        return 200
        # put is to add the obj

    def put(self, name):
        dic[name] = "gemrany"
        return 200

    def post(self, name):
        # request that something is done to the resource
        if name in dic:
            dic[name] = "rome"
            return 200
        else:
            return custom_error(404, "the name is not in the dict", "repeat")

    def get(self, name):
        # get the requested element
        if dic is None:
            return custom_error(404, "the dic is empty", "create")
        return dic


api.add_resource(EbayTesting, '/<string:search_term>')
api.add_resource(GuiQuery, '/order66/<string:name>')
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
