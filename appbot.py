from flask import Flask, request, jsonify

app = Flask(__name__)

# Route to return student number
@app.route("/", methods=["GET"])
def home():
    return jsonify({"student_number": "123456789"})  # Replace with your actual student number

# Route to handle webhook fulfillment
@app.route("/webhook", methods=["POST"])
def webhook():
    req = request.get_json(silent=True, force=True)

    # Extract intent name from Dialogflow request
    intent_name = req.get("queryResult", {}).get("intent", {}).get("displayName")

    # Define responses for stretching exercises
    if intent_name == "Stretching Exercises":
        response_text = "Here are some stretching exercises:\n- Pre-workout: Arm circles, Leg swings\n- Post-workout: Hamstring stretch, Shoulder stretch\n- Desk Stretches: Neck rolls, Seated spinal twist."
    else:
        response_text = "Sorry, I don't have information on that."

    return jsonify({"fulfillmentText": response_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
