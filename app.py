from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/notify/email', methods=['POST'])
def send_email_notification():
    data = request.get_json()

    to = data.get('to')
    message = data.get('message')

    if not to or not message:
        return jsonify({"error": "Missing 'to' or 'message' field"}), 400

    # Simulate sending email (replace with actual logic or log it)
    print(f"Sending email to {to}: {message}")

    return jsonify({"status": "success", "to": to, "message": message}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
