from flask import Flask, send_file
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials, firestore
import os
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io

app = Flask(__name__)
CORS(app)

cred_json = json.loads(os.environ.get("GOOGLE_CREDENTIALS"))
cred = credentials.Certificate(cred_json)
firebase_admin.initialize_app(cred)
db = firestore.client()


@app.route("/stats/<poll_id>", methods=["GET"])
def get_stats(poll_id):
    doc = db.collection("polls").document(poll_id).get()

    if not doc.exists:
        return "Poll not found", 404

    poll = doc.to_dict()
    options = list(poll["options"].keys())
    votes = list(poll["options"].values())

    fig, ax = plt.subplots()
    ax.bar(options, votes)
    ax.set_title(poll["question"])
    ax.set_xlabel("Options")
    ax.set_ylabel("Votes")

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    plt.close()

    return send_file(buf, mimetype="image/png")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5002))
    app.run(host="0.0.0.0", port=port)