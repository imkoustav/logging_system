import redis
import json
import os
from log_writer import write_to_file

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
#REDIS_HOST = os.getenv("REDIS_HOST", "localhost")  # Change from "redis" to "localhost"
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_CHANNEL = "log_channel"

redis_client = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
pubsub = redis_client.pubsub()
pubsub.subscribe(REDIS_CHANNEL)

def listen_for_logs():
    """Listens to Redis Pub/Sub and processes logs"""
    print("Listening for logs on Redis...")
    for message in pubsub.listen():
        if message["type"] == "message":
            log_entry = json.loads(message["data"])
            write_to_file(log_entry)
            print(f"Logged: {log_entry}")

if __name__ == "__main__":
    listen_for_logs()
