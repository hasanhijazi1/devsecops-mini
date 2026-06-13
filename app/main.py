from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify({"status": "ok"}), 200

@app.get("/ping")
def ping():
    return jsonify({"message": "pong!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # nosec

