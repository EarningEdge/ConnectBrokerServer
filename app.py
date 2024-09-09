from flask import Flask, request, jsonify
from dhanhq import dhanhq
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def requests_retry_session(
    retries=3,
    backoff_factor=0.3,
    status_forcelist=(500, 502, 504),
    session=None,
):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session

@app.route("/")
def index():
    return "Server is working"

@app.route("/holdings")
def get_holdings():
    try:
        client_id = request.args.get("clientId", "")
        access_token = request.args.get("accessToken", "")

        dhan = dhanhq(client_id, access_token)
        dhan._session = requests_retry_session()  # Use retry session
        holding_data = dhan.get_holdings()
        return jsonify(holding_data)
    except Exception as e:
        logger.error(f"Error in get_holdings: {str(e)}", exc_info=True)
        return jsonify({"error": "Failed to retrieve holdings. Please try again later."}), 500

@app.route("/positions")
def get_positions():
    try:
        client_id = request.args.get("clientId", "")
        access_token = request.args.get("accessToken", "")

        dhan = dhanhq(client_id, access_token)
        dhan._session = requests_retry_session()  # Use retry session
        position_data = dhan.get_positions()
        return jsonify(position_data)
    except Exception as e:
        logger.error(f"Error in get_positions: {str(e)}", exc_info=True)
        return jsonify({"error": "Failed to retrieve positions. Please try again later."}), 500

@app.route("/get_trade_book")
def get_trade_book():
    try:
        client_id = request.args.get("clientId", "")
        access_token = request.args.get("accessToken", "")
        dhan = dhanhq(client_id, access_token)
        dhan._session = requests_retry_session()  # Use retry session
        trade_book_data = dhan.get_trade_book()
        return jsonify(trade_book_data)
    except Exception as e:
        logger.error(f"Error in get_trade_book: {str(e)}", exc_info=True)
        return jsonify({"error": "Failed to retrieve trade book. Please try again later."}), 500

@app.route("/get_funds")
def get_funds():
    try:
        client_id = request.args.get("clientId", "")
        access_token = request.args.get("accessToken", "")
        dhan = dhanhq(client_id, access_token)
        dhan._session = requests_retry_session()  # Use retry session
        fund_data = dhan.get_fund_limits()
        return jsonify(fund_data)
    except Exception as e:
        logger.error(f"Error in get_funds: {str(e)}", exc_info=True)
        return jsonify({"error": "Failed to retrieve fund limits. Please try again later."}), 500

if __name__ == "__main__":
    app.run(debug=True)