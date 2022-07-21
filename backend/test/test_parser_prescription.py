import pytest
from backend.src.util import Extract

@pytest.fixture()
def doc_1():
    _parser = Extract("../resources/prescription/pre_1.pdf", "prescription").extract_text()
    return _parser


@pytest.fixture()
def doc_2():
    _parser = Extract("../resources/prescription/pre_2.pdf", "prescription").extract_text()
    return _parser


def test_patient_name(doc_1, doc_2):
    assert doc_1['patient_name'] == "Marta Sharapova"
    assert doc_2['patient_name'] == "Virat Kohli"


def test_get_address(doc_1, doc_2):
    assert doc_1['patient_address'] == "9 tennis court, new Russia, DC"
    assert doc_2['patient_address'] == "2 cricket blvd, New Delhi"


def test_get_medicines(doc_1, doc_2):
    assert doc_1['medicines'] == "K\n\nPrednisone 20 mg\nLialda 2.4 gram"
    assert doc_2['medicines'] == "| Omeprazole 40 mg"


def test_get_directions(doc_1, doc_2):
    assert doc_1[
               'directions'] == "Prednisone, Taper 5 mg every 3 days,\nFinish in 2.5 weeks a\nLialda - take 2 pill everyday for 1 month"

    assert doc_2['directions'] == "Use two tablets daily for three months"


def test_get_refill(doc_1, doc_2):
    assert doc_2['refill'] == "3 times"
    assert doc_1['refill'] == "2 times"
