from python_mastering.decision import Decision


def test_construction():
    d = Decision('Database#1', 'Dataset#1')
    assert 'Database#1' == d.database
    assert 'Dataset#1' == d.dataset
