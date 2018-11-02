from flask import Flask,redirect, request,Response,jsonify,url_for
from flask_restful import Resource, Api,reqparse
from ebaysdk.finding import Connection as Finding

app = Flask(__name__)
api= Api(app)

def custom_error(stat_code,msg,action):
    error_msg = jsonify({
        'status' :stat_code,
        'message' :msg,
        'action' :action
        })
    error_msg.stat_code = stat_code ##this way we can reference it
    return error_msg

##Ebay Sdk Pratice
class HelloWorld(Resource):
    def get(self,search_term):
        api = Finding(domain='svcs.sandbox.ebay.com',appid="AdrianNa-CSC380-SBX-ec22ddb1d-3bd0ef52" ,config_file="ebay.yaml")
        response = api.execute('findItemsAdvanced', {'keywords': search_term})
        return jsonify(response.dict())


##this is our primary endpoint for the gui
dic ={}
class GuiQuery(Resource):
    ##remove the requested objected
    def delete(self,name ):
        dic.pop(name)
        return 200
           ##put is to add the obj
    def put(self,name):
        dic[name] ="gemrany"
        return 200
    def post(self,name):
        ##request that something is done to the resource
        if name in dic:
            dic[name] ="rome"
            return 200
        else:
            return custom_error(404,"the name is not in the dict","repeat")
    def get(self,name):
        ##get the requested element
        if dic == None:
            return custom_error(404,"the dic is empty","create")
        return dic

api.add_resource(HelloWorld,'/<string:search_term>')
api.add_resource(GuiQuery,'/order66/<string:name>')
if __name__ == '__main__':
     app.run(host='0.0.0.0',debug=True)
