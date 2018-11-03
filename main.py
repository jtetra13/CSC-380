from flask import Flask, redirect, request, Response, jsonify, url_for
from flask_restful import Resource, Api, reqparse
from ebaysdk.finding import Connection as Finding

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
    error_msg.stat_code = stat_code  #this way we can reference it
    return error_msg



def generate_request_dict(key_words):
    # this will be to craft custom search query
    print("placeholder")


def generate_json_for_gui(response, max_query):
    # the input will be the dict of the response from api
    custom_search = {
    }
    parsed_dic = {}
    returned_args = parser.parse_args()
    if returned_args['search_param'] is not None:
        listy = returned_args['search_param'].split(',')
    else:
        listy = None
    for x in range(max_query):
        parsed_dic[x] = {}
        parsed_dic[x]['parsed'] = listy
        parsed_dic[x]["title"] = response[x].get("title", None)
        parsed_dic[x]["price"] = response[x].get("sellingStatus", None).get("convertedCurrentPrice", None).get("value",
                                                                                                               None)
        parsed_dic[x]["totalPrice"] = response[x].get("shippingInfo", None).get("shippingServiceCost", None).get(
            "value", None)
    return jsonify(parsed_dic)


#Ebay Sdk Pratice
class EbayTesting(Resource):
    def get(self, search_term):
        # this will be changed since we will get query from the gui,parse it from the endpoint
        # craft the custom api request , parse the response from ebay and pass the dict/json to gui
        api = Finding(config_file=None, appid="AdrianNa-CSC380-SBX-ec22ddb1d-3bd0ef52", domain='svcs.sandbox.ebay.com')
##Ebay Sdk Pratice
class HelloWorld(Resource):
    def get(self,search_term):
        #remove the following from appid,drgerGERGeergewrgSdfwegfoiergi
        #added the appid since its for the sandbox mode and doesn't pose a major risk
        api = Finding(domain='svcs.sandbox.ebay.com',appid="drgerGERGeergewrgSdfwegfoiergiAdrianNa-CSC380-SBX-ec22ddb1d-3bd0ef52" ,config_file="ebay.yaml")

        response = api.execute('findItemsAdvanced', {'keywords': search_term})
        response = response.dict()
        response = response["searchResult"]["item"]
        return generate_json_for_gui(response, 4)


# this is our primary endpoint for the gui
dic = {}


class GuiQuery(Resource):
    #remove the requested objected
    def delete(self, name):
        dic.pop(name)
        return 200
        #put is to add the obj

    def put(self, name):
        dic[name] = "gemrany"
        return 200

    def post(self, name):
        #request that something is done to the resource
        if name in dic:
            dic[name] = "rome"
            return 200
        else:
            return custom_error(404, "the name is not in the dict", "repeat")

    def get(self, name):
        #get the requested element
        if dic is None:
            return custom_error(404, "the dic is empty", "create")
        return dic


api.add_resource(EbayTesting, '/<string:search_term>')
api.add_resource(GuiQuery, '/order66/<string:name>')
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
