import os
import json
import hashlib
from dotenv import load_dotenv

load_dotenv()

def get_hash8(token):
    return hashlib.sha256(token.encode()).hexdigest()[:8]

def check_file_contains(path, pattern):
    if not os.path.exists(path): 
        return False
    try:
        with open(path, 'rb') as f:
            content = f.read().decode('utf-8', errors='ignore').replace(" ", "").lower()
            return pattern.replace(" ", "").lower() in content
    except Exception:
        return False

def build_summary():
    token = os.getenv("STUDENT_TOKEN", "default_token")
    hash8 = get_hash8(token)
    
    # Прямая проверка версии в JSON
    pt_valid = False
    pt_path = "artifacts/day5/pt/network_devices.json"
    if os.path.exists(pt_path):
        try:
            with open(pt_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if data.get("version") == "1.0":
                    pt_valid = True
        except:
            # Если не распарсилось, пробуем найти строку грубой силой
            pt_valid = check_file_contains(pt_path, '"version":"1.0"')

    summary = {
        "student": {
            "token_hash8": hash8,
            "name": os.getenv("STUDENT_NAME", "Yutsevich Artem"),
            "group": os.getenv("STUDENT_GROUP", "IB-23-5b")
        },
        "modules": {
            "yang": {
                "ok": os.path.exists("artifacts/day5/yang/pyang_tree.txt"),
                "tree_valid": check_file_contains("artifacts/day5/yang/pyang_tree.txt", "+--rw interfaces")
            },
            "webex": {
                "ok": os.path.exists("artifacts/day5/webex/message_post.json"),
                "hash_match": check_file_contains("artifacts/day5/webex/room_create.json", hash8)
            },
            "pt": {
                "ok": os.path.exists("artifacts/day5/pt/pt_internal_output.txt"),
                "external_check_passed": check_file_contains("artifacts/day5/pt/external_access_check.json", "empty ticket"),
                "api_responses_valid": pt_valid
            }
        },
        "status": "COMPLETED"
    }

    os.makedirs("artifacts/day5", exist_ok=True)
    with open("artifacts/day5/summary.json", "w", encoding='utf-8') as f:
        json.dump(summary, f, indent=4, ensure_ascii=False)
    print("✅ Summary rebuilt! Check artifacts/day5/summary.json")

if __name__ == "__main__":
    build_summary()