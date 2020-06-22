from scripts.statement import Statement


def test_generate_monthly_statement():
    statementMonth0 = Statement(42, 0.04)
    assert statementMonth0.getMinPymt(42, 0.04) == 1.68
