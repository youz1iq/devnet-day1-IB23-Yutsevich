import os
import json
import hashlib
import pytest
from jsonschema import validate
from dotenv import load_dotenv

load_dotenv()

def get_hash8(token):
    return hashlib.sha256(token.encode()).hexdigest()[:8]

@pytest.fixture
def summary_data():
    path = "artifacts/day5/summary.json"
    assert os.path.exists(path), f"Файл {path} не найден! Сначала запусти builder."
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def test_summary_schema_and_student(summary_data):
    # Проверка базовой структуры и студента
    assert "student" in summary_data
    assert summary_data["student"]["name"] == "Yutsevich Artem"
    
    # Проверка корректности хэша токена
    token = os.getenv("STUDENT_TOKEN", "default_token")
    expected_hash = get_hash8(token)
    assert summary_data["student"]["token_hash8"] == expected_hash

def test_yang_module(summary_data):
    yang = summary_data["modules"]["yang"]
    assert yang["ok"] is True
    assert yang["tree_valid"] is True
    assert os.path.exists("artifacts/day5/yang/pyang_tree.txt")

def test_webex_module(summary_data):
    webex = summary_data["modules"]["webex"]
    assert webex["ok"] is True
    assert webex["hash_match"] is True

def test_pt_module(summary_data):
    pt = summary_data["modules"]["pt"]
    assert pt["ok"] is True
    assert pt["external_check_passed"] is True
    assert pt["api_responses_valid"] is True

def test_status_completed(summary_data):
    assert summary_data["status"] == "COMPLETED"