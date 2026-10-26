import json

import pytest
from approvaltests import verify
from approval_utilities.utils import get_adjacent_file

from statement import statement


def test_example_statement():
    with open(get_adjacent_file("invoice.json")) as f:
        invoice = json.loads(f.read())
    with open(get_adjacent_file("plays.json")) as f:
        plays = json.loads(f.read())
    verify(statement(invoice, plays))


def test_statement_with_new_play_types():
    with open(get_adjacent_file("invoice_new_plays.json")) as f:
        invoice = json.loads(f.read())
    with open(get_adjacent_file("new_plays.json")) as f:
        plays = json.loads(f.read())
    with pytest.raises(ValueError) as exception_info:
        statement(invoice, plays)
    assert "unknown type" in str(exception_info.value)

def test_statement_with_small_audience():
    invoice = {
        "customer": "Amazon",
        "performances": [
            {"playID": "othello", "audience": 13}
        ]
    }

    with open(get_adjacent_file("plays.json")) as f:
        plays = json.loads(f.read())

    result = statement(invoice, plays)

    assert "Othello" in result
    assert "$400.00" in result
    assert "You earned 0 credits" in result
    
def test_tragedy_at_30_audience_member_boundary():
    invoice = {
        "customer": "Microsoft",
        "performances": [
            {"playID": "hamlet", "audience": 30}
        ]
    }

    with open(get_adjacent_file("plays.json")) as f:
        plays = json.loads(f.read())
            
    result = statement(invoice, plays)

    assert "$400.00" in result
    
def test_historical_case():
    invoice = {
        "customer": "Target",
        "performances": [
            {"playID": "henry-V", "audience": 35}
        ]
    }
    
    with open(get_adjacent_file("plays.json")) as f:
        plays = json.loads(f.read())
            
    result = statement(invoice, plays)

    assert "$725.00" in result
    assert "You earned 7 credits" in result
    assert "Henry V" in result
    
    
def test_historical_case_with_volume_credit_rounded_down():
    invoice = {
        "customer": "Verison",
        "performances": [
            {"playID": "henry-V", "audience": 14}
        ]
    }
    
    with open(get_adjacent_file("plays.json")) as f:
        plays = json.loads(f.read())
            
    result = statement(invoice, plays)

    assert "$500.00" in result
    assert "You earned 2 credits" in result
    assert "Henry V" in result