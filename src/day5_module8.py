import os
import json
import hashlib
import requests
from dotenv import load_dotenv

# Загружаем переменные из .env (если они там есть)
load_dotenv()

# Берем токен из переменной окружения
TOKEN = os.getenv("WEBEX_TOKEN")
S_TOKEN = os.getenv("STUDENT_TOKEN", "default")
S_NAME = os.getenv("STUDENT_NAME", "Artem Yutsevich")
S_GROUP = os.getenv("STUDENT_GROUP", "IB-23-5b")

# Генерируем тот самый хеш (первые 8 символов sha256)
token_hash8 = hashlib.sha256(S_TOKEN.encode()).hexdigest()[:8]

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}
base_url = "https://webexapis.com/v1"

def save_json(path, data):
    """Удобная функция для сохранения ответов API в папку artifacts"""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def run_webex_lab():
    if not TOKEN:
        print("ОШИБКА: WEBEX_TOKEN не найден. Сделай $env:WEBEX_TOKEN = 'твой_токен'")
        return

    print(f"--- Запуск Webex Lab для {S_NAME} ---")
    
    try:
        # 1. Получаем инфо о себе (me.json)
        me = requests.get(f"{base_url}/people/me", headers=headers).json()
        save_json("artifacts/day5/webex/me.json", me)
        print("[OK] Сохранен me.json")

        # 2. Список комнат (rooms_list.json)
        rooms = requests.get(f"{base_url}/rooms", headers=headers).json()
        save_json("artifacts/day5/webex/rooms_list.json", rooms)
        print("[OK] Сохранен rooms_list.json")

        # 3. Создаем комнату с хешем в названии (room_create.json)
        room_title = f"DevNet_Capstone_{token_hash8}"
        room_payload = {"title": room_title}
        new_room = requests.post(f"{base_url}/rooms", headers=headers, json=room_payload).json()
        save_json("artifacts/day5/webex/room_create.json", new_room)
        room_id = new_room.get("id")
        print(f"[OK] Создана комната: {room_title}")

        # 4. Отправляем сообщение (message_post.json)
        msg_payload = {
            "roomId": room_id,
            "text": f"Lab 8.6.7 completed. Student: {S_NAME}. Hash: {token_hash8}"
        }
        msg = requests.post(f"{base_url}/messages", headers=headers, json=msg_payload).json()
        save_json("artifacts/day5/webex/message_post.json", msg)
        print("[OK] Сообщение отправлено")

        # 5. Получаем список сообщений из этой комнаты (messages_list.json)
        msgs_list = requests.get(f"{base_url}/messages", headers=headers, params={"roomId": room_id}).json()
        save_json("artifacts/day5/webex/messages_list.json", msgs_list)
        print("[OK] Сохранен messages_list.json")

    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    run_webex_lab()