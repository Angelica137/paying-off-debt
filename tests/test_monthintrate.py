from scripts.monthintrate import MonthlyIntRate


def test_month_int_rate():
    monthRate = MonthlyIntRate(0.2)
    assert monthRate.calcMonthRate() == 0.2 / 12
