from scripts.balance import Balance


def test_constructor():
    b = Balance(42, 0, 0)
    assert b._outsBalance == 42


def test_calcOutsBalance():
    b = Balance(42, 40.32, 0.2/12)
    assert b.calcOutsBalance() == 40.99
