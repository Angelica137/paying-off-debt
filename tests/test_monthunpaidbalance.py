from scripts.monthunpaidbalance import MonthUnpaidBalance


def test_calculate_month_unpaid_balance():
    mub = MonthUnpaidBalance(42, 1.68)
    assert mub.calcMonthUnpaidBalance(42, 1.68) == 40.32
