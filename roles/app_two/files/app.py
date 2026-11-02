import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Application Two!"

@app.route("/health")
def health():
    return "App Two is running!"

if __name__ == "__main__":
    port = int(os.environ.get("APP_PORT", 5002))
    app.run(host="0.0.0.0", port=port)
