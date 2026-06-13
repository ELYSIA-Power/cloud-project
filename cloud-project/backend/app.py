from flask import Flask, jsonify
import redis
import os

app = Flask(__name__)

# 从环境变量读取Redis配置
redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_port = int(os.getenv('REDIS_PORT', 6379))
redis_password = os.getenv('REDIS_PASSWORD', None)

redis_client = redis.Redis(
    host=redis_host,
    port=redis_port,
    password=redis_password,
    decode_responses=True
)

@app.route('/api/ping')
def ping():
    return jsonify({"status": "ok"})

@app.route('/api/set/<key>/<value>')
def set_value(key, value):
    redis_client.set(key, value)
    return jsonify({"key": key, "value": value})

@app.route('/api/get/<key>')
def get_value(key):
    value = redis_client.get(key)
    return jsonify({"key": key, "value": value})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
