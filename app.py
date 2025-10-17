from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

ACCESS_TOKEN = "YOUR_ZALO_ACCESS_TOKEN"
TEMPLATE_ID = "YOUR_TEMPLATE_ID"

@app.route("/send", methods=["POST"])
def send_zns():
    try:
        data = request.json
        phone = data.get("phone")
        customer_name = data.get("customer_name")
        order_code = data.get("order_code")

        payload = {
            "phone": phone,
            "template_id": TEMPLATE_ID,
            "template_data": {
                "customer_name": customer_name,
                "order_code": order_code
            },
            "mode": "development"
        }

        headers = {
            "Content-Type": "application/json",
            "access_token": ACCESS_TOKEN
        }

        res = requests.post(
            "https://business.openapi.zalo.me/message/template",
            headers=headers,
            data=json.dumps(payload)
        )
        return jsonify(res.json())

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
