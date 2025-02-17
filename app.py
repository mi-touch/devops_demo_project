from flask import Flask, jsonify
import time

app = Flask(__name__)

def get_greeting():
    """Returns a greeting message based on the current time of day."""
    hour = time.localtime().tm_hour
    if 5 <= hour < 12:
        return "Good Morning!"
    elif 12 <= hour < 18:
        return "Good Afternoon!"
    else:
        return "Good Evening!"

@app.route("/")
def get_current_time():
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    response = {
        "message": get_greeting(),
        "service2Response": "Hello from Service-2!",
        "currentTime": current_time
    }

    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
