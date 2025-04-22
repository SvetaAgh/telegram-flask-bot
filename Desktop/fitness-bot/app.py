from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

TOKEN = "7970079450:AAG12CN17jNLdshh8hg368VAxVk5hrlR9Ds"
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
                'caption': 'Мы запускаем фитнес-марафон, который поможет тебе достичь желаемого рельефа, укрепить здоровье, повысить уровень энергии и улучшить общее самочувствие!\n\nНа протяжении 30 дней тебя будет поддерживать наша команда: опытные фитнес-тренеры, врач-реабилитолог и специалист нутрициолог.🌿\n\nЭксперты помогут тебе подобрать эффективные упражнения, разобраться в правильном питании, расскажут о паттернах движения — все это для того, чтобы ты заметила первые изменения уже к июню.\n\nБлагодаря комплексному подходу ты сформируешь правильные привычки, построишь здоровое, гибкое, рельефное тело и достигнешь поставленной цели. 🔥\n\nНу что, поехали? 😎'
            },
            files={'photo': photo_file}
        )
    return jsonify({"status": response.status_code})

@app.route('/invite', methods=['POST'])
def handle_invite():
    chat_id = request.get_json(force=True)
    invite_link = "https://t.me/+m5vpHkG0q5M4MjFi"
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
    app.run(host="0.0.0.0", port=5000)


