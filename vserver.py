from flask import Flask, request, jsonify
import json
import time

app = Flask(__name__)

@app.route('/update_coords', methods=['POST'])
def update_coords():
    data = request.get_json()
    with open("latest_coords.json", "w") as f:
        json.dump({
            "lat": data.get("lat"),
            "lon": data.get("lon"),
            "timestamp": time.time()
        }, f)
    return jsonify({"status": "OK", "received": data}), 200

@app.route('/get_coords')
def get_coords():
    try:
        with open("latest_coords.json", "r") as f:
            return jsonify(json.load(f))
    except:
        return jsonify({"lat": 0, "lon": 0, "timestamp": None})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
