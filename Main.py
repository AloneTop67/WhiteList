from flask import Flask, request

app = Flask(__name__)

WHITELIST = [
    123456789,  # tu UserId aquí
]

@app.route("/check")
def check():
    try:
        uid = int(request.args.get("user", 0))
        if uid in WHITELIST:
            return "ok", 200
        return "no", 403
    except:
        return "no", 403

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
