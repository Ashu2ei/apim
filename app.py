from flask import Flask,request

app = Flask(__name__)

from flask import jsonify



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
import logging
# logger = logging.getLogger()
# logger.setLevel(logging.INFO)
#console_handler = logging.StreamHandler()
# console_handler.setFormatter(logging.INFO)
# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# console_handler.setFormatter(formatter)
# logger.addHandler(console_handler)

# logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
# logger = logging.getLogger(__name__)

############################
# logger = logging.getLogger('ashutosh')
# logger.setLevel(logging.INFO)  # Use INFO level here
# logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
# sh = logging.StreamHandler()
# sh.setLevel(logging.INFO)
# logger.addHandler(sh)
####################################

# @app.route("/api1")
# def api1():
#     print("hello data is getting printed")
#     logger.info("API1 endpoint called. Hello, data is getting printed.")
#     logger.debug("This is a debug message.")  # Add more log messages as needed
#     logger.warning("Warning: Something might need attention.")
#     return jsonify(large_json1)

#####################
from logging.handlers import RotatingFileHandler
log_level, format, datefmt = logging.INFO, '%(asctime)s - %(levelname)s - %(message)s', '%d-%b-%Y %H:%M:%S %p'
import os
# Create the log directory if it does not exist


# file_handler = RotatingFileHandler("new.log", mode='a', maxBytes=5*1024*1024, backupCount=1, encoding=None, delay=0)
# # Set the log level and format
# file_handler.setLevel(log_level)
# file_handler.setFormatter(logging.Formatter(format, datefmt=datefmt))

# logger = logging.getLogger(__name__)
# logger.setLevel(log_level)
# logger.addHandler(file_handler)


#logger = logging.getLogger('ashutosh')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)  # Use INFO level here
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
stream_handler = logging.StreamHandler()

# Set the log level and format
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(logging.Formatter(format, datefmt=datefmt))

#logger.addHandler(stream_handler)

# Your existing /api1 route
@app.route("/api1")
def api1():
    logger.info("API1 endpoint called. Hello, data is getting printed.")
    logger.debug("Debugigng is ON")
    logger.warning("warning is on")
    logger.error("something is wrong")
    return jsonify(large_json1)
################################################################
@app.route("/api2")
def api2():
    try:
        # Get the data from the request
        data = request.data.decode("utf-8")
        print("hello data is getting printed")
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


# if __name__ == "__main__":
#     app.run()



import logging
from flask import Flask
app = Flask(__name__)
if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
else:
    logging.basicConfig(level=logging.DEBUG)
    app.logger.setLevel(logging.DEBUG)

####
# import logging
# LOG_FORMATTER = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")
# handler = logging.StreamHandler()
# handler.setFormatter(LOG_FORMATTER)
# logger = logging.getLogger(__name__)
# logger.addHandler(handler)
# logger.setLevel(logging.INFO)
#  logger.propagate= False

########
@app.route("/api1")
def hello():
    app.logger.info('Hello world log entry')
    app.logger.debug('it is a debug message')
    app.logger.error('it is a error message')
    app.logger.warning('it is a warning message')
    return jsonify(large_json1)

from dotenv import load_dotenv
load_dotenv()
import pymongo
@app.route("/cosmos")
def hello_cosmos():
    CONNECTION_STRING  = os.environ.get("MONGODB_CONNECTION_ENDPOINT")
    client = pymongo.MongoClient(CONNECTION_STRING)
    database = client.get_database("Testing")
    collection =  database.get_collection("test_table")
    all_documents = list(collection.find())
    return jsonify(str(all_documents))
if __name__ == "__main__":
    app.run()
