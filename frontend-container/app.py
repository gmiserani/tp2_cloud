from flask import Flask, request, jsonify
import pickle
import datetime

app = Flask(__name__)

app.model = pickle.load(open("/model/recommendation_rules.pkl", "rb"))
with open("/model/recommendation_rules.pkl", "rb") as f:
    rules = pickle.load(f)
    for rule in rules[:5]:
        print(rule)

app.model_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@app.route("/")
def home():
    return "API is running!"

@app.route('/api/recommend', methods=["POST"])
def recommend():
    data = request.get_json()
    user_songs = set(data.get("songs", []))
    print(f"Received songs: {user_songs}")

    recommendations = []
    for antecedent, consequent, confidence in app.model:
        if antecedent.issubset(user_songs):
            print(f"Matched rule: {antecedent} -> {consequent} (confidence: {confidence})")

            recommendations.extend(consequent - user_songs)

    recommendations = list(set(recommendations))[:10]
    print(f"Generated recommendations: {recommendations}")

    response = {
        'songs': recommendations,
        'version': '0.1',
        'model_date': app.model_date
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=52021, debug=True)