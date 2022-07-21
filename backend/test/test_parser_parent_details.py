from backend.src.parser_patient_details import PatientDetailsParser
from backend.src.util import Extract
import pytest


@pytest.fixture()
def doc_1():
    _parser = Extract("../resources/patient_details/pd_1.pdf","patient_details").extract_text()
    return _parser

@pytest.fixture()
def doc_2():
    _parser = Extract("../resources/patient_details/pd_2.pdf","patient_details").extract_text()
    return _parser

def test_get_name(doc_1,doc_2):
    assert doc_1['patient_name'] == "Kathy Crawford"
    assert doc_2['patient_name'] == "Jerry Lucas"

def test_get_phone_no(doc_1,doc_2):
    assert doc_1['patient_phone_no'] == "(737) 988-0851"
    assert doc_2['patient_phone_no'] == "(279) 920-8204"

def test_get_medical_problems(doc_1,doc_2):
    assert doc_1['medical_problems'] == "Migraine"
    assert "N/A" in doc_2['medical_problems']

def test_get_vaccination(doc_1,doc_2):
    assert doc_1['vaccination'] == "No"
    assert doc_2['vaccination'] == "Yes"

