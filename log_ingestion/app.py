from flask import Flask, request, jsonify
from redis_service import publish_log

app = Flask(__name__)

@app.route("/logs/write", methods=["POST"])
def write_log():
    """Receives log messages and publishes them to Redis"""
    data = request.json
    message = data.get("message")
    severity = data.get("severity", "INFO")

    if not message:
        return jsonify({"error": "Message is required"}), 400

    publish_log(message, severity)

    return jsonify({"status": "success", "message": "Log published to Redis"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
