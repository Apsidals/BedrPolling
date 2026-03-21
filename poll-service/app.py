from flask import Flask, jsonify, request
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials, firestore
import os
import json

app = Flask(__name__)
CORS(app)

cred_json = json.loads(os.environ.get("GOOGLE_CREDENTIALS"))
cred = credentials.Certificate(cred_json)
firebase_admin.initialize_app(cred)
db = firestore.client()


@app.route("/polls", methods=["GET"])
def get_all_polls():
    polls = []
    for doc in db.collection("polls").stream():
        poll = doc.to_dict()
        poll["id"] = doc.id
        polls.append(poll)
    return jsonify(polls)


@app.route("/polls", methods=["POST"])
def create_poll():
    data = request.json
    question = data["question"]
    options = {}
    for opt in data["options"]:
        options[opt] = 0
    new_poll = {"question": question, "options": options}
    ref = db.collection("polls").add(new_poll)
    return jsonify({"id": ref[1].id}), 201


@app.route("/polls/<poll_id>", methods=["DELETE"])
def delete_poll(poll_id):
    db.collection("polls").document(poll_id).delete()
    return jsonify({"success": True})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)