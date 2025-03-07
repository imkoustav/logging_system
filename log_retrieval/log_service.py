import os

# LOG_FILE = "logs/logs.log"
#LOG_FILE = os.path.join(os.path.dirname(__file__), "logs", "logs.log")
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # Go up one directory
# LOG_FILE = os.path.join(BASE_DIR, "log_processor", "logs", "logs.log")
#LOG_FILE = "/app/logs/logs.log"

if os.getenv("DOCKER_ENV"):  # If running inside Docker
    LOG_FILE = "/app/logs/logs.log"
else:  # Running locally
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # Go up one directory
    LOG_FILE = os.path.join(BASE_DIR, "log_processor", "logs", "logs.log")


def read_logs():
    """Reads logs from file."""
    if not os.path.exists(LOG_FILE):
        return None
    with open(LOG_FILE, "r") as file:
        return file.readlines()

def compute_log_metrics():
    """Computes log metrics (count per severity)."""
    logs = read_logs()
    if logs is None:
        return None

    severity_count = {"INFO": 0, "WARNING": 0, "ERROR": 0}

    for line in logs:
        if "[INFO]" in line:
            severity_count["INFO"] += 1
        elif "[WARNING]" in line:
            severity_count["WARNING"] += 1
        elif "[ERROR]" in line:
            severity_count["ERROR"] += 1

    return severity_count
