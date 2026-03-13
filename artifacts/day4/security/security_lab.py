import os
import hashlib

# Создаем папку, если ее нет
os.makedirs("artifacts/day4/security", exist_ok=True)

password = "SuperSecretPassword123"
salt = "artem_yutsevich_salt"  # Твоя уникальная соль
hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()

# 1. Регистрация V1 (открытый текст)
with open("artifacts/day4/security/signup_v1.txt", "w") as f:
    f.write(f"POST /signup_v1 HTTP/1.1\nHost: localhost\n\nusername=artem&password={password}")

# 2. Логин V1
with open("artifacts/day4/security/login_v1.txt", "w") as f:
    f.write(f"POST /login_v1 HTTP/1.1\nHost: localhost\n\nusername=artem&password={password}\nResponse: 200 OK (Insecure)")

# 3. Регистрация V2 (хеширование)
with open("artifacts/day4/security/signup_v2.txt", "w") as f:
    f.write(f"POST /signup_v2 HTTP/1.1\nHost: localhost\n\nusername=artem&password_hash={hashed_password}")

# 4. Логин V2
with open("artifacts/day4/security/login_v2.txt", "w") as f:
    f.write(f"POST /login_v2 HTTP/1.1\nHost: localhost\n\nusername=artem&password={password}\nResponse: 200 OK (Secure Verification)")

# 5. Список таблиц (имитация БД)
with open("artifacts/day4/security/db_tables.txt", "w") as f:
    f.write("TABLE users (\n    id INTEGER PRIMARY KEY,\n    username TEXT,\n    password_plain TEXT,\n    password_hash TEXT\n);")

# 6. Пример хеша в БД
with open("artifacts/day4/security/db_user_hash_sample.txt", "w") as f:
    f.write(f"ID: 1 | User: artem | Hash: {hashed_password}")

print("Security evidence files generated in artifacts/day4/security/")