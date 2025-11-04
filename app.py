from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

@app.route("/")
def home():
    return "ZNS API của Genbox đang hoạt động!"

ACCESS_TOKEN = "EdoXN_XFunuuUQPVyqtb4J5_frVmLg1ESMQpJTPNz0fH0DCSqNNh6d88s0VpV_r8Ip3STUz7oZKf2Tnph4FlNGOts1p70UW6PtRBIDD0YtnP0Cb1ucRC1sSEnHJNM8qNQJ3D4-fQYIbyFxDcnt6HF4Olj3_FQhCyJYYw0iT6-q1J6TXMwd3cJ6WXtr3sJkb0V3hGHST__a958TTiq4tkRqnofYtB9P4GQr2dEFaoW0nIPRmobG2f9obWg1oLKPSX0HwhDvbpbp4BHT9hg1Vn93vfuXk2B_i-57pp9uWLo1S-FzqtYt3Y0K0smH7Y0zGKUKlA9jW_-JfeGSuPztVu6Km0vbw6SlLvHHJiO-0-hI9QM8HWy2p5GdfD_q_-0RvFFLQuOgy5l6mJHhrvWIABDo1wpWYO1FbDH_C7SNVzLU4Q"    # ✅ Thay bằng token OA
TEMPLATE_ID = "495480"           # ✅ Thay bằng ID template được duyệt

@app.route("/send", methods=["POST"])
def send_zns():
    try:
        data = request.json

        phone = data.get("phone")
        account_name = data.get("account_name")
        sale_order_no = data.get("sale_order_no")
        shipping_address = data.get("shipping_address")
        sale_order_amount = data.get("sale_order_amount")

        payload = {
            "phone": phone,
            "template_id": TEMPLATE_ID,
            "template_data": {
                "account_name": account_name,
                "sale_order_no": sale_order_no,
                "shipping_address": shipping_address,
                "sale_order_amount": sale_order_amount
            },
            "mode": "development"   # ✅ Khi chạy thật bạn đổi thành "production"
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
