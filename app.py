from flask import Flask, jsonify, request
from flask_restful import Api, Resource


# Flask has a built in server i.e. app
app = Flask(__name__)
api = Api(app)


def checkPostedData(postedData, functionName):
    if (functionName == "subtract"):
        if "x" not in postedData or "y" not in postedData:
            return 301
        else:
            return 200


class Subtract(Resource):
    def post(self):
        postedData = request.get_json()

        status_code = checkPostedData(postedData, "subtract")

        if (status_code != 200):
            retJson = {
                "Message": "An error happened",
                "Status Code": status_code
            }

            return jsonify(retJson)

        x = int(postedData["x"])
        y = int(postedData["y"])

        ret = x-y
        print(ret)
        retMap = {
            'Message': ret,
            'Status Code': 200
        }

        return jsonify(retMap)


api.add_resource(Subtract, "/subtract")


@app.route('/')
def hello_world():
    return "hello world"


@app.route('/hithere')
def hi_there_everyone():
    # prepare a response for the request that came to/bye
    return "I just hit /hithere"


@app.route('/add_two_nums', methods=['POST'])
def add_two_nums():
    # get x, y from the posted data
    dataDict = request.get_json()
    # add x+y store in z
    if "y" not in dataDict:
        return "ERROR", 305

    z = dataDict['x'] + dataDict['y']

    retJSON = {
        'z': z
    }
    return jsonify(retJSON), 200

    # prepare a JSON, 'z': z
    # return jsonify(z)


if __name__ == "__main__":
    # specify where app should run inside app.run else defaults to 127.0.0.1.. etc.
    # debug = True when developing
    app.run(debug=True)


# to run this file and have the endpoints show up:
# be in the folder with app.py
# export FLASK_APP=app.py
# flask run
