from flask import Flask, jsonify
import os
import socket
import redis
import time

app = Flask(__name__)

REDIS_HOST = os.environ.get("REDIS_HOST", "redis")
REDIS_PORT = int(os.environ.get("REDIS_PORT", "6379"))
r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

@app.route("/")
def index():
    # increment a shared counter to show cross-container state
    count = r.incr("hits")
    return jsonify({
        "message": "Hello from Flask container (message changed)",
        "hostname": socket.gethostname(),
        "container_ip": socket.gethostbyname(socket.gethostname()),
        "hits_total": count
    })

@app.route("/health")
def health():
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
