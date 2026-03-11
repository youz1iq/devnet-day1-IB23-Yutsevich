# Day 2 Report — Git + Data Formats + Tests

## 1) Student
- Name: Yutsevich Artem
- Group: IB-23-5b
- Token: D1-IB-23-5b-28-F543
- Repo: https://github.com/youz1iq/devnet-day1-IB23-Yutsevich
- PR link (day2): https://github.com/youz1iq/devnet-day1-IB23-Yutsevich/pull/1

## 2) NetAcad progress
- Module 2.2 done: Yes 
- Module 3.1–3.6 done: 3.1, 3.2, 3.3, 3.4, 3.5, 3.6 

## 3) Git evidence
- File `artifacts/day2/git_log.txt` exists: Yes
- File `artifacts/day2/conflict_log.txt` exists: Yes
- Conflict note: Конфликт возник в файле README.md при попытке слияния веток feature/day2-readme-A и feature/day2-readme-B. Разрешен вручную путем объединения изменений из обеих веток.

## 4) Generated artifacts (Day2)
- normalized.json: Yes
- normalized.yaml: Yes
- normalized.xml: Yes
- normalized.csv: Yes
- summary.json: Yes

## 5) Commands output
### 5.1 Generator
```text
{
  "schema_version": "2.0",
  "generated_utc": "2026-03-11T14:46:19.224938+00:00",
  "student": {
    "token": "D1-IB-23-5b-28-F543",
    "token_hash8": "659f1a7b",
    "name": "Yutsevich Artem",
    "group": "IB-23-5b"
  },
  "input": {
    "path": "artifacts/day1/response.json",
    "sha256": "ffefdf50d54770c2a20ba143e42daa910535c20ec5ca7a1e449dac71729f00fe"
  },
  "outputs": {
    "normalized_json_sha256": "27718406db278d6d18c4fc4eb0612e26d37261d14c2e09f102052e6971ac3c2c",
    "normalized_yaml_sha256": "f11a2b8714b9f5737e2498d50c370fb705e3a399bc1d6643ecaa9a94e7dcb10f",
    "normalized_xml_sha256": "90bbaf734eb4f20e9cbf822cb5eed30f1b4fe05da1ee394209c518894b1c5f29",
    "normalized_csv_sha256": "296c09a577f1fae56ab0b678366f338a74067f7005c50489197719e5e7aac445"
  },
  "computed": {
    "title_len": 18
  }
}

5.2 tests
(.venv) devasc@labvm:~/Desktop/devnet-day1-IB23-yutsevich$ pytest -q..                                       [100%]2 passed in 0.22s

What I learned
Работа с ветками Git: создание, переключение и выполнение слияния (merge).

Разрешение конфликтов: идентификация маркеров конфликта в файлах и их ручное устранение.

Тестирование: использование pytest для автоматической проверки структуры артефактов.

7) Problems & fixes
Problem:
Скрипт не видел переменные окружения из файла .env (ошибка STUDENT_TOKEN), а файл тестов в репозитории был пустым (collected 0 items).
Fix:
Использовал команду export для прямой передачи переменных в сессию терминала. Для тестов вручную добавил проверочные функции, валидирующие наличие файлов в artifacts/day2/.