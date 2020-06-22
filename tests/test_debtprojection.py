from scripts.debtprojection import Statement
from scripts.debtprojection import DebtProjection


def test_generate_monthly_statement():
    statementMonth0 = Statement(42, 0.04)
    assert statementMonth0.getMinPmt(42, 0.04) == 1.68


def test_print_statement():
    statementMonth0 = Statement(42, 0.04)
    assert statementMonth0.printStatement(
        42, 1.68) == "Balance: 42; Minimum Payment: 1.68"


def test_minimum_monthly_payment():
    projection1 = DebtProjection(42, 0.04)
    assert projection1.getMinMonPmt(42, 0.04) == 1.68
