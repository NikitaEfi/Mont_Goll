import random
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/play/", methods=["POST"])
def play():
    data = request.get_json()
    choose_option = data["choose_option"]
    attempts = data["attempts"]

    wins = 0

    for _ in range(attempts):
        car = random.randint(1, 3)
        pick = random.randint(1, 3)
        open_dore = random.choice([x for x in (1, 2, 3) if x != car and x != pick])
        if choose_option == "change":
            pick = ({1, 2, 3} - {pick, open_dore}).pop()
        if pick == car:
            wins += 1
    return jsonify({"wins": wins, "loose": attempts - wins})

if __name__ == "__main__":
    app.run(port=8000, debug=True)
