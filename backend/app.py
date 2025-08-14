from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/data")
def get_data():
    # 模拟返回套利数据
    return jsonify({"pair": "BTC/USD", "exchangeA": 40000, "exchangeB": 40200})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
