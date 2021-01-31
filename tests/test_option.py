from python_mastering.option import Option


def test_construction():
    o = Option('Database#1', 'Dataset#1')
    assert 'Database#1' == o.database
    assert 'Dataset#1' == o.dataset
