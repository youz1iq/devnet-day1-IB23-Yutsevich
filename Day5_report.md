# Day 5 Report — Module 8 Capstone

## 1) Student
- Name: Yutsevich Artem
- Group: IB-23-5b
- Token: D1-IB-23-5b-28-F543
- Repo: https://github.com/youz1iq/devnet-day1-IB23-Yutsevich

## 2) YANG (8.3.5)
- Evidence files:
  - artifacts/day5/yang/ietf-interfaces.yang
  - artifacts/day5/yang/pyang_version.txt
  ```text
  __main__.py 2.7.1
  ```


  - artifacts/day5/yang/pyang_tree.txt
  ```text
    module: ietf-interfaces
    +--rw interfaces
    |  +--rw interface* [name]
    |     +--rw name                        string
    |     +--rw description?                string
    |     +--rw type                        identityref
    |     +--rw enabled?                    boolean
    |     +--rw link-up-down-trap-enable?   enumeration {if-mib}?
    +--ro interfaces-state
        +--ro interface* [name]
            +--ro name               string
            +--ro type               identityref
            +--ro admin-status       enumeration {if-mib}?
            +--ro oper-status        enumeration
            +--ro last-change?       yang:date-and-time
            +--ro if-index           int32 {if-mib}?
            +--ro phys-address?      yang:phys-address
            +--ro higher-layer-if*   interface-state-ref
            +--ro lower-layer-if*    interface-state-ref
            +--ro speed?             yang:gauge64
            +--ro statistics
            +--ro discontinuity-time    yang:date-and-time
            +--ro in-octets?            yang:counter64
            +--ro in-unicast-pkts?      yang:counter64
            +--ro in-broadcast-pkts?    yang:counter64
            +--ro in-multicast-pkts?    yang:counter64
            +--ro in-discards?          yang:counter32
            +--ro in-errors?            yang:counter32
            +--ro in-unknown-protos?    yang:counter32
            +--ro out-octets?           yang:counter64
            +--ro out-unicast-pkts?     yang:counter64
            +--ro out-broadcast-pkts?   yang:counter64
            +--ro out-multicast-pkts?   yang:counter64
            +--ro out-discards?         yang:counter32
            +--ro out-errors?           yang:counter32

    ```
## 3) Webex (8.6.7)
- **Room title contains token_hash8:** Yes
- **Message text contains token_hash8:** Yes
- **Evidence files:**
- [me.json](./artifacts/day5/webex/me.json)
- [rooms_list.json](./artifacts/day5/webex/rooms_list.json) 
- [room_create.json](./artifacts/day5/webex/room_create.json) 
- [message_post.json](./artifacts/day5/webex/message_post.json) 
- [messages_list.json](./artifacts/day5/webex/messages_list.json) 

## 4) Packet Tracer Controller REST (8.8.3)
- external_access_check contains “empty ticket”: Yes
- serviceTicket saved: Yes
- Evidence files:
 - [external_access_check.json](./artifacts/day5/pt/external_access_check.json)
  - [network_devices.json](./artifacts/day5/pt/network_devices.json)
  - [hosts.json](./artifacts/day5/pt/hosts.json)
  - [postman_collection.json](./artifacts/day5/pt/postman_collection.json)
  - [postman_environment.json](./artifacts/day5/pt/postman_environment.json)
  - [pt_internal_output.txt](./artifacts/day5/pt/pt_internal_output.txt)

  ## 5) Commands output (paste exact)
  ```text
  PS F:\devnet-day1-IB23-yutsevich> py .\src\day5_summary_builder.py
✅ Summary rebuilt! Check artifacts/day5/summary.json
PS F:\devnet-day1-IB23-yutsevich> cat .\artifacts\day5\summary.json
{
    "student": {
        "token_hash8": "659f1a7b",
        "name": "Yutsevich Artem",
        "group": "IB-23-5b"
    },
    "modules": {
        "yang": {
            "ok": true,
            "tree_valid": true
        },
        "webex": {
            "ok": true,
            "hash_match": true
        },
        "pt": {
            "ok": true,
            "external_check_passed": true,
            "api_responses_valid": true
        }
    },
    "status": "COMPLETED"
}
  ```
  pytest
  ```bash
  PS F:\devnet-day1-IB23-yutsevich> py -m pytest -v tests/test_day5_module8.py
============================================================================= test session starts =============================================================================
platform win32 -- Python 3.14.2, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\user\AppData\Local\Python\pythoncore-3.14-64\python.exe
cachedir: .pytest_cache
rootdir: F:\devnet-day1-IB23-yutsevich
collected 5 items                                                                                                                                                              

tests/test_day5_module8.py::test_summary_schema_and_student PASSED                                                                                                       [ 20%] 
tests/test_day5_module8.py::test_yang_module PASSED                                                                                                                      [ 40%] 
tests/test_day5_module8.py::test_webex_module PASSED                                                                                                                     [ 60%] 
tests/test_day5_module8.py::test_pt_module PASSED                                                                                                                        [ 80%] 
tests/test_day5_module8.py::test_status_completed PASSED                                                                                                                 [100%] 

============================================================================== 5 passed in 0.08s ============================================================================== 
PS F:\devnet-day1-IB23-yutsevich> 
  ```
  ## 6 Problems & fixs 

**Problem 1: JSON Validation in Summary Builder**
- **Problem:** Скрипт `summary_builder.py` не мог подтвердить валидность API-ответов. Метод поиска подстроки `"version": "1.0"` в файле `network_devices.json` возвращал `False` из-за особенностей вложенности структуры JSON.
- **Fix:** Метод текстового поиска заменен на полноценный парсинг JSON через `json.load()`. Теперь скрипт обращается к ключу `data.get("version")` напрямую.
- **Proof:** Флаг `api_responses_valid` в итоговом `summary.json` принял значение `true`, тест `test_pt_module` пройден.

**Problem 2: Student Token Environment Issue**
- **Problem:** Тесты завершались ошибкой `AssertionError`, так как скрипт тестов не видел переменную `STUDENT_TOKEN` из `.env` и использовал `default_token`, что создавало неверный хэш.
- **Fix:** В файл `tests/test_day5_module8.py` добавлена загрузка переменных окружения через `load_dotenv()`.
- **Proof:** Хэш токена в тесте совпал с хэшем в отчете (`659f1a7b`), тест `test_summary_schema_and_student` успешно пройден.
