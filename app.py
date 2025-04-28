from flask import Flask, jsonify
import json
import yaml
 
app = Flask(__name__)
 
# Load data from local JSON/YAML files
def load_events():
    with open("data/events.json") as f:
        return json.load(f)
 
def load_news():
    with open("data/news.yaml") as f:
        return yaml.safe_load(f)
 
@app.route("/api/events", methods=["GET"])
def get_events():
    return jsonify(load_events())
 
@app.route("/api/news", methods=["GET"])
def get_news():
    return jsonify(load_news())
 
@app.route("/")
def index():
    return jsonify({
        "events": load_events(),
        "news": load_news()
    })
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)