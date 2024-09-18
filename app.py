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
logger = logging.getLogger()
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
# logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
# logger = logging.getLogger(__name__)
@app.route("/api1")
def api1():
    print("hello data is getting printed")
    logger.info("API1 endpoint called. Hello, data is getting printed.")
    # logger.debug("This is a debug message.")  # Add more log messages as needed
    # logger.warning("Warning: Something might need attention.")
    return jsonify(large_json1)

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


if __name__ == "__main__":
    app.run()
