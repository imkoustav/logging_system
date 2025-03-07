import os

LOG_FILE = "logs/logs.log"

def write_to_file(log_entry):
    """Writes log messages to a file."""
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

    with open(LOG_FILE, "a") as file:
        file.write(f"[{log_entry['severity']}] {log_entry['message']}\n")
