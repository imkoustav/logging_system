from flask import Flask, jsonify
from log_service import read_logs, compute_log_metrics

app = Flask(__name__)

@app.route("/logs", methods=["GET"])
def fetch_logs():
    """Fetch all logs"""
    logs = read_logs()
    if logs is None:
        return jsonify({"error": "Log file not found"}), 404
    return jsonify({"logs": logs})

@app.route("/logs/metrics", methods=["GET"])
def log_metrics():
    """Compute log metrics"""
    metrics = compute_log_metrics()
    if metrics is None:
        return jsonify({"error": "Log file not found"}), 404
    return jsonify(metrics)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
