# import os

# # LOG_FILE = "logs/logs.log"
# #LOG_FILE = os.path.join(os.path.dirname(__file__), "logs", "logs.log")
# # BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # Go up one directory
# # LOG_FILE = os.path.join(BASE_DIR, "log_processor", "logs", "logs.log")
# #LOG_FILE = "/app/logs/logs.log"

# if os.getenv("DOCKER_ENV"):  # If running inside Docker
#     LOG_FILE = "/app/logs/logs.log"
# else:  # Running locally
#     BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # Go up one directory
#     LOG_FILE = os.path.join(BASE_DIR, "log_processor", "logs", "logs.log")


# def read_logs():
#     """Reads logs from file."""
#     if not os.path.exists(LOG_FILE):
#         return None
#     with open(LOG_FILE, "r") as file:
#         return file.readlines()

# def compute_log_metrics():
#     """Computes log metrics (count per severity)."""
#     logs = read_logs()
#     if logs is None:
#         return None

#     severity_count = {"INFO": 0, "WARNING": 0, "ERROR": 0}

#     for line in logs:
#         if "[INFO]" in line:
#             severity_count["INFO"] += 1
#         elif "[WARNING]" in line:
#             severity_count["WARNING"] += 1
#         elif "[ERROR]" in line:
#             severity_count["ERROR"] += 1

#     return severity_count

import os
import logging
import subprocess
from logging.handlers import RotatingFileHandler, SysLogHandler

LOG_FILE = "/app/logs/logs.log"  # Ensure this path matches your container's volume

# Ensure logs directory exists
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

# Configure log rotation
log_handler = RotatingFileHandler(LOG_FILE, maxBytes=5*1024*1024, backupCount=3)  # 5MB per file, keeps 3 backups
log_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

# Configure syslog logging (for Linux)
syslog_handler = SysLogHandler(address="/dev/log")
syslog_handler.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))

logger = logging.getLogger("LogService")
logger.setLevel(logging.INFO)
logger.addHandler(log_handler)
logger.addHandler(syslog_handler)

def log_to_file(message, severity="INFO"):
    """Logs a message to file and syslog"""
    if severity == "INFO":
        logger.info(message)
    elif severity == "WARNING":
        logger.warning(message)
    elif severity == "ERROR":
        logger.error(message)

def rotate_logs():
    """Forces log rotation"""
    logger.handlers[0].doRollover()
    return "Logs rotated successfully"

def execute_command(command):
    """Safely executes a shell command and returns output or error."""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        return {"output": result.stdout.strip()}
    except subprocess.CalledProcessError as e:
        return {"error": e.stderr.strip()}

def get_recent_logs(lines=10):
    """Fetches recent log lines using 'tail'."""
    return execute_command(f"tail -n {lines} {LOG_FILE}")

def search_logs(keyword):
    """Searches logs for a specific keyword using 'grep'."""
    return execute_command(f"grep '{keyword}' {LOG_FILE}")

# def filter_logs(date=None, severity=None):
#     """Filters logs using 'journalctl' based on date and severity."""
#     command = "journalctl"
#     if date:
#         command += f" --since='{date}'"
#     if severity:
#         command += f" -p {severity}"
#     return execute_command(command)

def filter_logs(date=None, severity=None):
    """Filters logs based on date and severity from the log file."""
    if not os.path.exists(LOG_FILE):
        return {"error": "Log file not found"}

    command = f"cat {LOG_FILE}"
    
    if date:
        command += f" | grep '{date}'"
    if severity:
        severity_map = {"INFO": "INFO", "WARNING": "WARNING", "ERROR": "ERROR"}
        severity_str = severity_map.get(severity, None)
        if severity_str:
            command += f" | grep '[{severity_str}]'"

    return execute_command(command)

