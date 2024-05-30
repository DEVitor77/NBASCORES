from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/games', methods=['GET'])
def get_games():
    games = [
        {"game": 1, "team1": "Lakers", "team2": "Heat", "score": "102-96"},
        {"game": 2, "team1": "Celtics", "team2": "Warriors", "score": "98-103"},
        {"game": 3, "team1": "Nets", "team2": "Bucks", "score": "110-115"}
    ]
    return jsonify(games)

if __name__ == '__main__':
    app.run(debug=True)
