from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():
    th8 = os.getenv("TOKEN_HASH8", "659f1a7b")
    return f"TOKEN_HASH8={th8}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)