from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

TOKEN = "твой_бот_токен"
PHOTO_PATH = "welcome.jpg"

@app.route('/start', methods=['POST'])
def handle_start():
    chat_id = request.get_json(force=True)
    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"

    with open(PHOTO_PATH, 'rb') as photo_file:
        response = requests.post(
            url,
            data={
                'chat_id': chat_id,
                'caption': 'Твой текст-приглашение'
            },
            files={'photo': photo_file}
        )
    return jsonify({"status": response.status_code})

@app.route('/invite', methods=['POST'])
def handle_invite():
    chat_id = request.get_json(force=True)
    invite_link = "https://t.me/твой_канал"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    payload = {
        "chat_id": chat_id,
        "text": "Нажми на кнопку ниже, чтобы перейти в закрытый канал 👇",
        "reply_markup": {
            "inline_keyboard": [[
                {"text": "Перейти в канал", "url": invite_link}
            ]]
        }
    }

    response = requests.post(url, json=payload)
    return jsonify({"status": response.status_code})

@app.route('/ping')
def ping():
    return "pong"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)  # <-- ЭТО ВАЖНО ДЛЯ RENDER






