from flask import Flask, request, jsonify
from dhanhq import dhanhq

app = Flask(__name__)


@app.route("/")
def index():
    return "Server is working"


@app.route("/holdings")
def get_holdings():
    try:
        client_id = request.args.get("clientId", "")
        access_token = request.args.get("accessToken", "")

        dhan = dhanhq(client_id, access_token)
        holding_data = dhan.get_holdings()
        return jsonify(holding_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/positions")
def get_positions():
    try:
        client_id = request.args.get("clientId", "")
        access_token = request.args.get("accessToken", "")

        dhan = dhanhq(client_id, access_token)
        position_data = dhan.get_positions()
        return jsonify(position_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/get_trade_book")
def get_trade_book():
    try:
        client_id = request.args.get("clientId", "")
        access_token = request.args.get("accessToken", "")
        dhan = dhanhq(client_id, access_token)
        position_data = dhan.get_trade_book()
        return jsonify(position_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/get_funds")
def get_funds():
    try:
        client_id = request.args.get("clientId", "")
        access_token = request.args.get("accessToken", "")
        dhan = dhanhq(client_id, access_token)
        position_data = dhan.get_fund_limits()
        return jsonify(position_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
