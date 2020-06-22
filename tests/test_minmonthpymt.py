from scripts.minmonthpymt import MinMonthPymt


def test_calculate_min_monthly_payment():
    minMoPmt = MinMonthPymt(0.04, 42)
    assert minMoPmt.calcMinMonPymt(0.04, 42) == 1.68
