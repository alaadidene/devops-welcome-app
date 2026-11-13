import os
from flask import Flask

app = Flask(__name__)
MESSAGE = os.environ.get("GREETING", "Bonjour depuis Docker, version 1.0.1 !")

@app.route("/")
def index():
    return MESSAGE

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
# Test du cache Docker
