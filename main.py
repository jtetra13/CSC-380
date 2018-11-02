from flask import Flask,redirect, request,Response,jsonify,url_for
from flask_restful import Resource, Api,reqparse

##hello world boilerplate

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


class HelloWorld(Resource):
    def get(self):
        return {'hlll' : 'world'}
dic ={}
class GuiQuery(Resource):
    def delete(self,name ):
        dic.pop(name)
        return 201
        ##remove the requested objected
    def put(self,name):
        ##put is to add the obj
        dic[name] ="gemrany"
        return 201
    def post(self,name):
        ##request that something is done to the resource
        if name in dic:
            dic[name] ="rome"
            return 201
        else:
            return custom_error(400,"the name is not in the dict","repeat").stat_code
    def get(self,name):
        ##get the requested element
        return dic

api.add_resource(HelloWorld,'/')
api.add_resource(GuiQuery,'/order66/<string:name>')
if __name__ == '__main__':
     app.run(host='0.0.0.0',debug=True)
