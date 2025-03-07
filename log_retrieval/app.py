# from flask import Flask, jsonify
# from log_service import read_logs, compute_log_metrics

# app = Flask(__name__)

# @app.route("/logs", methods=["GET"])
# def fetch_logs():
#     """Fetch all logs"""
#     logs = read_logs()
#     if logs is None:
#         return jsonify({"error": "Log file not found"}), 404
#     return jsonify({"logs": logs})

# @app.route("/logs/metrics", methods=["GET"])
# def log_metrics():
#     """Compute log metrics"""
#     metrics = compute_log_metrics()
#     if metrics is None:
#         return jsonify({"error": "Log file not found"}), 404
#     return jsonify(metrics)

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5001)


from flask import Flask, request, jsonify
from log_service import get_recent_logs, search_logs, filter_logs

app = Flask(__name__)

@app.route("/logs/recent", methods=["GET"])
def fetch_recent_logs():
    """Fetch recent logs."""
    lines = request.args.get("lines", default=10, type=int)
    return jsonify(get_recent_logs(lines))

@app.route("/logs/search", methods=["GET"])
def search_log_entries():
    """Search logs for a keyword."""
    keyword = request.args.get("keyword")
    if not keyword:
        return jsonify({"error": "Keyword is required"}), 400
    return jsonify(search_logs(keyword))

@app.route("/logs/filter", methods=["GET"])
def filter_log_entries():
    """Filter logs based on date and severity."""
    date = request.args.get("date")
    severity = request.args.get("severity")
    return jsonify(filter_logs(date, severity))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
