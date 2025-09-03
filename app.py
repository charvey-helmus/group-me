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
        send_message('''Here’s the info: https://docs.google.com/spreadsheets/d/1KWEgkyaAIMJ1DCkkSpQ65ZzELJGEjvw0Hr_LcMQgL5E/edit?usp=sharing
        
                     Description	Answer
Buy-In	$50
Pay-Out	1=400, 2=150, 3 =50
Number Keepers	2
Keeper Cost	Ascending Cost (1st time kept same as original draft cost, then up 2 each subsequent year)
Undrafted Keeper Cost	Manager's first undrafted kept is 13th round, 2nd 12th round, 3rd 11th round, etc.
Dropped Keeper Cost	Same as original draft round
Draft Order	Randomized Snake Draft
Draft time	
IR spots	2''')

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
