from scripts.debtprojection import DebtProjection


def test_minimum_monthly_payment():
    projection1 = DebtProjection(42, 0.04)
    assert projection1.getMinMonPmt(42, 0.04) == 1.68


def test_monthly_unpaid_balance():
    projection1 = DebtProjection(42, 0.04)
    projection1.getMinMonPmt(42, 0.04)
    assert projection1.getMonUnpaidBalance(42, 1.68) == 40.32


def test_next_month_balance():
    projection1 = DebtProjection(42, 0.04)
    projection1.getMinMonPmt(42, 0.04)
    projection1.getMonUnpaidBalance(42, 1.68)
    projection1.monthlyIntRate(0.2)
    assert projection1.getNextMonthBalance(40.32, 0.0166666) == 40.99
