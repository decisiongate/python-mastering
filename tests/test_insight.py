# import pytest

from python_mastering.insight import Insight
from python_mastering.decision import Decision


def test_construction():
    i = Insight('Database#1', 'Dataset#1')
    assert 'Database#1' == i.database
    assert 'Dataset#1' == i.dataset
    assert [] == i.decisions


def test_add_decision():
    d = Decision('Database#2', "Dataset#1")
    i = Insight('Database#1', "Dataset#1")
    i.add_decision(d)
    assert [d] == i.decisions


# @pytest.mark.skip(reason='not yet implemented')
def test_add_decisions():
    i = Insight('Database#1', "Dataset#1")
    d1 = Decision('Database#2', "Dataset#1")
    i.add_decision(d1)
    d2 = Decision('Database#3', "Dataset#1")
    d3 = Decision('Database#4', "Dataset#1")
    i.add_decisions((d2, d3))
    assert [d1, d2, d3] == i.decisions


# @pytest.mark.skip()
def test_primary_decision():
    i = Insight('Database#1', "Dataset#1")
    d1 = Decision('Database#2', "Dataset#1")
    i.add_decision(d1)
    d2 = Decision('Database#3', "Dataset#1")
    d3 = Decision('Database#4', "Dataset#1")
    i.add_decisions((d2, d3))
    assert d1 == i.primary_decision
