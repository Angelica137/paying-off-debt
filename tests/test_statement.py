from scripts.statement import Statement


def test_generate_monthly_statement():
    statementMonth0 = Statement(42, 0.04)
    assert statementMonth0.getMinPmt(42, 0.04) == 1.68


def test_print_statement():
    statementMonth0 = Statement(42, 0.04)
    assert statementMonth0.printStatement(
        42, 1.68) == "Balance: 42; Minimum Payment: 1.68"
