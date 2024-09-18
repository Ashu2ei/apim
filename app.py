from flask import Flask,request

app = Flask(__name__)

from flask import jsonify
import logging
import os
# Ensure the logs directory exists
# if not os.path.exists('logs'):
#     os.makedirs('logs')

# Configure logging
# logging.basicConfig(filename='logs/app.log', level=logging.INFO,
#                     format='%(asctime)s %(levelname)s %(name)s %(message)s')
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
    try:
        # Get the data from the request
        data = request.data.decode("utf-8")
        
        # Get the bearer token from the Authorization header
        bearer = request.headers.get("Authorization").split()[1]
        
        # Process the data (you can modify this part based on your requirements)
        # For now, we'll just return the received data
        return data
    except Exception as e:
        return str(e), 500
    

@app.route('/')
def home2():
    return "Welcome to the Flask App!"

@app.route("/api3")
def api3():
    return jsonify(large_json3)

@app.route("/app")
def home():
    #return jsonify(large_json3)
    header = request.headers.get("Authorization")
    print(header)
    data = request.get_json('https://api.coindesk.com/v1/bpi/currentprice.json')
    return jsonify(data)

# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# @app.route('/log', methods=['POST'])
# def log_message():
#     data = request.json
#     message = data.get('message')
#     level = data.get('level', 'info').upper()
#     logging.info("User 'Ravi' logged in successfully.")
#     if level == 'DEBUG':
#         app.logger.debug(message)
#     elif level == 'INFO':
#         app.logger.info(message)
#     elif level == 'WARNING':
#         app.logger.warning(message)
#     elif level == 'ERROR':
#         app.logger.error(message)
#     elif level == 'CRITICAL':
#         app.logger.critical(message)
#     else:
#         return jsonify({"error": "Invalid log level"}), 400

#     return jsonify({"status": "Logged successfully"}), 200

import logging
from logging.handlers import RotatingFileHandler
from azure.storage.blob import BlobServiceClient
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Azure Blob Storage configuration
connect_str = "your_connection_string"
container_name = "logs"
blob_name = "api_call_logs.log"

# Create a BlobServiceClient
# blob_service_client = BlobServiceClient.from_connection_string("hello")
# container_client = blob_service_client.get_container_client(container_name)

# # Ensure the container exists
# try:
#     container_client.create_container()
# except Exception as e:
#     pass  # Container already exists
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# Create a local log file
log_file = "api_call_logs.log"
handler = RotatingFileHandler(log_file, maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
app.logger.addHandler(handler)

@app.route('/log', methods=['POST'])
def log_message():
    data = request.json
    message = data.get('message')
    level = data.get('level', 'info').upper()

    app.logger.info(f"API call with message: {message} and level: {level}")
    
    if level == 'DEBUG':
        app.logger.debug(message)
    elif level == 'INFO':
        app.logger.info(message)
    elif level == 'WARNING':
        app.logger.warning(message)
    elif level == 'ERROR':
        app.logger.error(message)
    elif level == 'CRITICAL':
        app.logger.critical(message)
    else:
        return jsonify({"error": "Invalid log level"}), 400

    # Upload the log file to Azure Blob Storage
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    # with open(log_file, "rb") as data:
    #     blob_client.upload_blob(data, overwrite=True)

    return jsonify({"status": "Logged successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)


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



##################

# <policies>
#     <inbound>
#         <base />
#         <!-- Extract the Bearer token from the Authorization header -->
#         <set-variable name="Bearer Token" value="@(context.Request.Headers.GetValueOrDefault("Authorization", "").Substring(7))" />
#         <!-- Retrieve the secret from Key Vault -->
#         <set-variable name="KeyVaultSecret" value="12345" />
#         <!-- Check if both the Bearer token and the Key Vault secret are strings and have the same length -->
#         <choose>
#             <when condition="@(context.Variables["Bearer Token"] is string && context.Variables["KeyVaultSecret"] is string && ((string)context.Variables["Bearer Token"]).Length == ((string)context.Variables["KeyVaultSecret"]).Length)">
#                 <!-- Compare the Bearer token with the Key Vault secret -->
#                 <choose>
#                     <!-- <when condition="@(context.Variables["Bearer Token"] == context.Variables["KeyVaultSecret"])">
#                         <return-response>
#                             <set-status code="200" reason="OK" />
#                             <set-body>Bearer token matches the secret.</set-body>
#                         </return-response>
#                     </when> -->
#                     <when condition="@($"{context.Variables["Bearer Token"]}" == $"{context.Variables["KeyVaultSecret"]}")" />
#                     <otherwise>
#                         <return-response>
#                             <set-status code="401" reason="Unauthorized" />
#                             <set-body>@($"Bearer token does not matches the secret. Bearer Token: {context.Variables["Bearer Token"]}, Key Vault Secret: {context.Variables["KeyVaultSecret"]}/5")</set-body>
#                         </return-response>
#                     </otherwise>
#                 </choose>
#             </when>
#             <otherwise>
#                 <return-response>
#                     <set-status code="400" reason="Bad Request" />
#                     <set-body>@($"Bearer token does not matches the secret. Bearer Token: {context.Variables["Bearer Token"]}, Key Vault Secret: {context.Variables["KeyVaultSecret"]}")</set-body>
#                 </return-response>
#             </otherwise>
#         </choose>
#     </inbound>
#     <backend>
#         <base />
#     </backend>
#     <outbound>
#         <base />
#     </outbound>
#     <on-error>
#         <base />
#     </on-error>
# </policies>