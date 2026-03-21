from flask import Flask, jsonify, request
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)
CORS(app)

cred = credentials.Certificate("/app/firebase-key.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


@app.route("/vote", methods=["POST"])
def vote():
    data = request.json
    poll_id = data["poll_id"]
    option = data["option"]

    poll_ref = db.collection("polls").document(poll_id)
    doc = poll_ref.get()

    if not doc.exists:
        return jsonify({"error": "Poll not found"}), 404

    current = doc.to_dict()
    current["options"][option] = current["options"][option] + 1
    poll_ref.update({"options": current["options"]})

    return jsonify({"success": True})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
