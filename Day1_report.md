# Day 1 Report — DevNet Sprint

## 1. Student
- Name: Юцевич Артем
- Group: IB-23-5b
- GitHub repo: https://github.com/youz1iq/devnet-day1-IB23-Yutsevich
- Day1 Token: D1-IB-23-5b-28-F543

## 2. NetAcad progress (Module 1)
- Completed items: 1.1 / 1.2 / 1.3 

## 3. VM evidence
- File: `artifacts/day1/env.txt` exists: Yes
```bash
(.venv) devasc@labvm:~/Desktop/devnet-day1-IB23-yutsevich$ hostnamectl && date   Static hostname: labvm
         Icon name: computer-vm
           Chassis: vm
        Machine ID: c6a52afed8564edfa075a362c20348b8
           Boot ID: 46a9d1bd50ae4ed99e65c208e0d60efe
    Virtualization: vmware
  Operating System: Ubuntu 20.04 LTS
            Kernel: Linux 5.4.0-37-generic
      Architecture: x86-64
Tue 10 Mar 2026 10:51:45 AM UTC
```
## 4. Repo structure (must match assignment)
- `src/day1_api_hello.py` : Yes
- `tests/test_day1_api_hello.py` : Yes
- `schemas/day1_summary.schema.json` : Yes
- `artifacts/day1/summary.json` : Yes
- `artifacts/day1/response.json` : Yes

## 5. Commands run (paste EXACT output)
### 5.1 Script run
``` bash 
{
  "api": {
    "response_sha256": "ffefdf50d54770c2a20ba143e42daa910535c20ec5ca7a1e449dac71729f00fe",
    "status_code": 200,
    "url": "https://jsonplaceholder.typicode.com/todos/1",
    "validation_errors": [],
    "validation_passed": true
  },
  "generated_utc": "2026-03-10T10:32:32.941859+00:00",
  "run": {
    "platform": "linux",
    "python": "3.8.2"
  },
  "schema_version": "1.0",
  "student": {
    "group": "IB-23-5b",
    "name": "Yutsevich",
    "token": "D1-IB-23-5b-28-F543"
  }
}
```

## 6. What i learned today 
Научился работать с переменными окружения через файл .env 

Понял важность сохранения JSON (sort_keys=True) для получения стабильных хэш-сумм SHA-256.

Освоил процесс автоматизированного тестирования API с помощью pytest и валидацию данных через JSON Schema.

Разобрался с управлением зависимостями в Python через виртуальные окружения (venv) и requirements.txt.

Закрепил навыки работы с Git: использование .gitignore и фиксация изменений мелкими логическими коммитами.

## 7. Problems & fixes 
Problem: При запуске скрипта возникала ошибка TypeError: 'type' object is not subscriptable. Это произошло из-за того, что в VM установлена версия Python 3.8.2, которая не поддерживает современный синтаксис

Fix: Добавил в начало скрипта from __future__ import annotations и упростил сигнатуры функций (удалил уточняющие типы в скобках), чтобы обеспечить совместимость со старой версией интерпретатора.