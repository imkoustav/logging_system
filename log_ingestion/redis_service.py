import redis
import json
import os

# Redis configuration
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
#REDIS_HOST = os.getenv("REDIS_HOST", "localhost")  # Use localhost for local execution
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_CHANNEL = "log_channel"

redis_client = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

def publish_log(message, severity="INFO"):
    """Publishes a log message to Redis Pub/Sub"""
    log_entry = json.dumps({"severity": severity, "message": message})
    redis_client.publish(REDIS_CHANNEL, log_entry)
