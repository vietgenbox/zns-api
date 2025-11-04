from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

@app.route("/")
def home():
    return "ZNS API của Genbox đang hoạt động!"

ACCESS_TOKEN = "NxZLLzNyaLfTlT9NtlwNLLIxqr_TvV4IB_lfHzkofZ0uzwjpx-6T7pQblrMwefy4Ox-fQEsicXKFlPSPpPtMR0UAoY7KhlLh89hJFig6q6aNd_TW-BpE6GwKp1FJX_v_AwJU1lEIxb8fbQ06rAw_RLRdyH--phG9QU-KQBlhhGbsxQzBhkUA7M-kjqcLcROLPgM3NhVWeLqXnR4NgjA5NYd3bG_XmQ5NDD_l0TR1uMiVug8qxzgKU3VOWYtbdS5Q3RJL1i6SvdCBYQO6Xe-6LLF7er-0rEqdSiohB8NKwrW7p-WP_ydDGGY0qWdYf_fTO9pxKEY9sWOCikPamlh2DXFostVQn9m06_gyICJTfpWhxfjFqTdQCLd2-528WDmT0yV8Tl_jYZbz-wfQdEdmEmhZp3E1tEy_UPdBGxjmTplGvfDU"    # ✅ Thay bằng token OA
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
