from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route("/helloworld")
def helloworld():
    now = datetime.now()
    formatted_now = now.strftime("%Y-%m-%dT%H:%M:%S")
    return {"message": "hello world", "datetime": formatted_now}


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
