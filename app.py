from flask import Flask,request

app = Flask(__name__)

from flask import jsonify
import requests
# Sample large JSON data for API 1
large_json1 = {
    "message": "Welcome to API 1",
    "data": {
        "user_count": 1000,
        "average_age": 32,
        "active_users": ["Alice", "Bob", "Charlie"],
        "metadata": {
            "version": "v1",
            "timestamp": "2024-08-20T10:34:02"
        }
    }
}

# Sample large JSON data for API 2
large_json2 = {
    "message": "Greetings from API 2",
    "data": {
        "products": [
            {
                "id": 1,
                "name": "Widget A",
                "price": 19.99
            },
            {
                "id": 2,
                "name": "Widget B",
                "price": 24.99
            }
        ],
        "categories": ["Electronics", "Home", "Fashion"]
    }
}

# Sample large JSON data for API 3
large_json3 = {
    "message": "Data from API 3",
    "data": [
        {
            "id": 101,
            "title": "Post 1",
            "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        },
        {
            "id": 102,
            "title": "Post 2",
            "content": "Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas."
        }
    ]
}

@app.route("/api1")
def api1():
    return jsonify(large_json1)

@app.route("/api2")
def api2():
    return jsonify(large_json2)

@app.route("/api3")
def api3():
    return jsonify(large_json3)

@app.route("/app")
def home():
    #return jsonify(large_json3)
    data = request.get_json('https://api.coindesk.com/v1/bpi/currentprice.json')
    return jsonify(data)

# @app.route("/")
# def home():
#     # return jsonify(large_json3)
#     # data = request.get_json('https://api.coindesk.com/v1/bpi/currentprice.json')
#     # return data
#     data = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

#     return jsonify(str(data.json()))

# @app.route("/query_example")
# def home():
#     try:
#         client_name = request.args.get('client_name')
#         if client_name == "tata":
#             response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
#         elif client_name == "usa":
#             response = requests.get('https://datausa.io/api/data?drilldowns=Nation&measures=Population',verify = False)
#         elif client_name == "fake_user":
#             response = requests.get('https://randomuser.me/api/',verify = False)
#         elif client_name == "usa_universities":
#             response = requests.get('http://universities.hipolabs.com/search?country=United+States',verify = False)
#         data = response.json()

#         return jsonify(data)
#     except requests.RequestException as e:
#         return jsonify({"error": f"Request error: {str(e)}"}), 500
CLIENT_APIS = {
    "tata": "https://api.coindesk.com/v1/bpi/currentprice.json",
    "usa": "https://datausa.io/api/data?drilldowns=Nation&measures=Population",
    "fake_user": "https://randomuser.me/api/",
    "usa_universities": "http://universities.hipolabs.com/search?country=United+States",
}

# @app.route("/query_example")
# def home():
#     try:
#         client_name = request.args.get("client_name")
#         if client_name not in CLIENT_APIS:
#             return jsonify({"error": "Invalid client name"}), 400

#         api_url = CLIENT_APIS.get(client_name)
#         response = requests.get(api_url, verify=False)

#         data = response.json()
        
#         return jsonify(data)
#     except requests.RequestException as e:
#         return jsonify({"error": f"Request error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run()
