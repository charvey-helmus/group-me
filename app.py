from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_ID = os.getenv("GROUPME_BOT_ID")

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    if not data:
        return "no data", 400

    text = data.get("text", "").lower()

    if "league info" in text:
        send_message("Here’s the league info: [insert link or details here]")

    return "ok", 200


def send_message(msg):
    url = "https://api.groupme.com/v3/bots/post"
    payload = {
        "bot_id": BOT_ID,
        "text": msg
    }
    requests.post(url, json=payload)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
